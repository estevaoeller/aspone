"""Monta o protótipo da Visão geral do console num HTML único, que abre sem internet.

Esquema de montagem: o modelo traz os marcadores
/*__DADOS__*/null (onde entram os dados) e <!--__ECHARTS__--> (onde entra a biblioteca),
e este script só faz a substituição. Python padrão, sem dependências.

Uso:
  python gerar_sinteticos.py   # primeiro, se ainda não houver dados
  python montar_painel.py      # grava saida/painel-visao-geral.html
  python montar_painel.py --dados outro.json --saida painel.html
"""

import argparse
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
MODELO = AQUI / "painel_modelo.html"
ECHARTS = AQUI / "vendor" / "echarts.min.js"
MARCA_DADOS = "/*__DADOS__*/null"
MARCA_ECHARTS = "<!--__ECHARTS__-->"


def montar(dados: dict) -> str:
    html = MODELO.read_text(encoding="utf-8")
    for marca in (MARCA_DADOS, MARCA_ECHARTS):
        if html.count(marca) != 1:
            raise SystemExit(f"O modelo precisa ter o marcador {marca} exatamente uma vez.")
    # "</" escapado para que nenhum texto dos dados feche a tag <script> antes da hora
    js = json.dumps(dados, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    biblioteca = f"<script>{ECHARTS.read_text(encoding='utf-8')}</script>" if ECHARTS.exists() else ""
    return html.replace(MARCA_ECHARTS, biblioteca).replace(MARCA_DADOS, js)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dados", type=Path, default=AQUI / "dados_sinteticos.json")
    ap.add_argument("--saida", type=Path, default=AQUI / "saida" / "painel-visao-geral.html")
    a = ap.parse_args()
    dados = json.loads(a.dados.read_text(encoding="utf-8"))
    if not ECHARTS.exists():
        print(f"Aviso: {ECHARTS} não encontrado; o painel abre sem os gráficos.")
    a.saida.parent.mkdir(parents=True, exist_ok=True)
    a.saida.write_text(montar(dados), encoding="utf-8")
    print(f"Gravado {a.saida} ({a.saida.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
