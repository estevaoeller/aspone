"""Gera dados sintéticos para o protótipo da Visão geral do console (UI-02).

Nenhum dado real: grupos se chamam "Grupo A", "Grupo B"..., números são sorteados
com semente fixa, e o resultado é reprodutível. O formato do JSON é o contrato que o
adaptador real (leitura do PostgreSQL e dos logs do publicador) deverá produzir.

Uso:
  python gerar_sinteticos.py                    # grava dados_sinteticos.json, hoje como referência
  python gerar_sinteticos.py --hoje 2026-11-17  # data de referência fixa
"""

import argparse
import json
import random
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path

SP = timezone(timedelta(hours=-3))  # America/Sao_Paulo, sem horário de verão desde 2019
DIAS = 45
JANELA_WAHA = 30  # dias cobertos pelo webhook ao vivo
GRUPOS = [  # (nome fictício, mensagens médias por dia, chance de dia sem mensagem)
    ("Grupo A", 38, 0.05),
    ("Grupo B", 22, 0.10),
    ("Grupo C", 12, 0.20),
    ("Grupo D", 6, 0.45),
    ("Grupo E", 3, 0.60),
    ("Grupo F", 15, 0.15),
]


def iso(dt):
    return dt.isoformat(timespec="minutes")


def gerar(hoje: date, semente: int = 17) -> dict:
    rnd = random.Random(semente)
    dias = [hoje - timedelta(days=DIAS - 1 - i) for i in range(DIAS)]
    queda = hoje - timedelta(days=9)  # coletor fora do ar neste dia (lacuna proposital)
    agora = datetime.combine(hoje, time(9, 40), SP)

    cobertura, por_dia, mutacoes = [], [], []
    for di, d in enumerate(dias):
        idade = (hoje - d).days
        fontes = {"webhook": 0, "historico_gows": 0, "exportacao_txt": 0}
        for gi, (_, media, silencio) in enumerate(GRUPOS):
            n = 0 if rnd.random() < silencio else max(0, int(rnd.gauss(media, media * 0.35)))
            if d.weekday() >= 5:
                n //= 3
            if idade < JANELA_WAHA:
                fonte = "webhook"
                if d == queda:
                    # webhook perdeu o dia; o backfill GOWS recuperou parte depois
                    n, fonte = n // 2, "historico_gows"
            elif gi < 3:
                fonte = "historico_gows"  # backfill só para os grupos com piloto
            else:
                fonte = "exportacao_txt"  # exportação oficial importada
            fontes[fonte] += n
            cobertura.append([gi, di, n])
        por_dia.append({"dia": d.isoformat(), **fontes})
        total = sum(fontes.values())
        mutacoes.append({"dia": d.isoformat(),
                         "edicoes": rnd.randint(0, max(1, total // 25)),
                         "revogacoes": rnd.randint(0, max(1, total // 60))})

    execucoes = []
    for k in range(14, 0, -1):
        d = hoje - timedelta(days=k - 1)
        inicio = datetime.combine(d, time(3, 0), SP) + timedelta(seconds=rnd.randint(2, 40))
        estado, erro, prep = "verificada", None, rnd.randint(4, 9)
        verif = prep
        if k == 6:
            estado, erro, verif = "falhou", "Destino remoto não respondeu (tempo esgotado na conferência).", 0
        elif k == 5:
            estado, erro, prep, verif = "bloqueada", "Bloqueio ativo após a falha anterior; aguarda revisão.", 0, 0
        elif k == 3:
            estado, erro, verif = "parcial", "Dois arquivos divergiram na conferência; reenviados na execução seguinte.", prep - 2
        dur = rnd.randint(40, 140) if estado != "bloqueada" else 1
        execucoes.append({"id": f"pub-{d:%Y%m%d}-0300", "tipo": "automática", "inicio": iso(inicio),
                          "fim": iso(inicio + timedelta(seconds=dur)), "duracao_s": dur, "estado": estado,
                          "grupos": 0 if estado == "bloqueada" else 4, "mensagens": 0 if estado == "bloqueada" else rnd.randint(40, 160),
                          "arquivos_preparados": prep, "arquivos_verificados": verif, "erro": erro})
        if k == 5:
            ini = datetime.combine(d, time(10, 12), SP)
            execucoes.append({"id": f"pub-{d:%Y%m%d}-1012", "tipo": "manual", "inicio": iso(ini),
                              "fim": iso(ini + timedelta(seconds=212)), "duracao_s": 212, "estado": "verificada",
                              "grupos": 4, "mensagens": 231, "arquivos_preparados": 16, "arquivos_verificados": 16, "erro": None})
    ini = agora - timedelta(minutes=8)
    execucoes.append({"id": f"sim-{hoje:%Y%m%d}-0932", "tipo": "simulação", "inicio": iso(ini), "fim": iso(ini + timedelta(seconds=35)),
                      "duracao_s": 35, "estado": "verificada", "grupos": 4, "mensagens": 52,
                      "arquivos_preparados": 5, "arquivos_verificados": 0, "erro": None})
    execucoes.reverse()  # mais recente primeiro

    ultima_pub = next(e for e in execucoes if e["tipo"] != "simulação" and e["estado"] == "verificada")
    total_msgs = sum(c[2] for c in cobertura)
    return {
        "sintetico": True,
        "gerado_em": iso(agora),
        "fuso": "America/Sao_Paulo",
        "saude": [
            {"componente": "WAHA", "estado": "ok", "verificado_em": iso(agora - timedelta(minutes=2)), "detalhe": "Sessão conectada"},
            {"componente": "Coletor", "estado": "ok", "verificado_em": iso(agora - timedelta(minutes=2)), "detalhe": "Último webhook há 4 min"},
            {"componente": "PostgreSQL", "estado": "ok", "verificado_em": iso(agora - timedelta(minutes=2)), "detalhe": "Aceitando conexões"},
            {"componente": "Publicador", "estado": "desconhecido", "verificado_em": iso(agora - timedelta(hours=6, minutes=38)),
             "detalhe": "Sem verificação desde a última execução"},
        ],
        "grupos": {"descobertos": 23, "selecionados": len(GRUPOS), "habilitados": 4},
        "acervo": {"mensagens": total_msgs, "md_locais": sum(1 for c in cobertura if c[2] > 0),
                   "md_publicados": sum(1 for c in cobertura if c[2] > 0 and c[0] < 4) - 3,
                   "historico_recuperado": sum(p["historico_gows"] + p["exportacao_txt"] for p in por_dia), "retidos": 41},
        "publicacao": {"agendamento": "Diária às 03:00 (America/Sao_Paulo)",
                       "ultima_verificada": ultima_pub["fim"],
                       "proxima_execucao": iso(datetime.combine(hoje + timedelta(days=1), time(3, 0), SP)),
                       "mutacoes_pendentes": 3,
                       "ultimo_evento": iso(agora - timedelta(minutes=4))},
        "fontes": {"webhook": "Ao vivo (webhook)", "historico_gows": "Histórico GOWS", "exportacao_txt": "Exportação TXT"},
        "mensagens_por_dia": por_dia,
        "mutacoes_por_dia": mutacoes,
        "cobertura": {"grupos": [g[0] for g in GRUPOS], "dias": [d.isoformat() for d in dias], "valores": cobertura},
        "execucoes": execucoes,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--hoje", type=date.fromisoformat, default=date.today())
    ap.add_argument("--saida", type=Path, default=Path(__file__).with_name("dados_sinteticos.json"))
    a = ap.parse_args()
    dados = gerar(a.hoje)
    a.saida.write_text(json.dumps(dados, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Gravado {a.saida} ({len(dados['mensagens_por_dia'])} dias, {len(dados['execucoes'])} execuções)")


if __name__ == "__main__":
    main()
