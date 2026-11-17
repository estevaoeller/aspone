# Protótipo da Visão geral do console (dados sintéticos)

Protótipo da tela "Visão geral" descrita em [docs/console/especificacao.md](../../../docs/console/especificacao.md) (UI-02), feito com **dados sintéticos**. Não lê o ambiente real, não executa ações e não escolhe o framework do console: a pesquisa UI-01 continua aberta. O que se aproveita daqui em qualquer framework são o contrato de dados (abaixo) e as opções dos gráficos ECharts.

## Como gerar

```bash
python gerar_sinteticos.py --hoje 2026-11-17   # grava dados_sinteticos.json
python montar_painel.py                         # grava saida/painel-visao-geral.html
```

Python 3.12, só biblioteca padrão. O HTML gerado é um arquivo único, com ECharts e dados embutidos; abre sem internet. A pasta `saida/` fica fora do git.

## O que a tela mostra

| Bloco | Pergunta que responde |
|---|---|
| Saúde dos componentes | WAHA, coletor, PostgreSQL e publicador estão operando? Verificação velha (acima de 30 min) vira "Desatualizado"; sem dado, "Desconhecido". |
| Grupos, acervo e publicação | Quantos grupos foram descobertos, selecionados e habilitados; mensagens no banco, MD locais e MD publicados (contagens distintas); última publicação verificada, próxima execução, último evento, mutações pendentes. |
| Mensagens por dia, por fonte | Barras empilhadas: ao vivo (webhook), histórico GOWS, exportação TXT. Queda num dia recente sinaliza falha de coleta. |
| Cobertura por grupo e dia | Mapa de calor; células vazias com contorno tracejado são dias sem mensagem (silêncio ou lacuna). |
| Edições e revogações por dia | Mutações resolvidas contra a mensagem original. |
| Execuções do publicador | Arquivos preparados e verificados por execução, e tabela com estado, erro sanitizado e identificador. "Disparo não equivale a sucesso". |

Nenhum conteúdo de conversa aparece. Cada gráfico tem "Ver tabela" com os mesmos números.

## Contrato de dados

O adaptador real (a escrever, depois da aprovação da arquitetura) deve produzir este JSON a partir do PostgreSQL e do registro de execuções. Os nomes seguem `gerar_sinteticos.py`.

| Chave | Conteúdo |
|---|---|
| `sintetico` | `true` exibe o aviso de protótipo; o adaptador real grava `false`. |
| `gerado_em`, `fuso` | instante da coleta das métricas, ISO 8601 com fuso; `America/Sao_Paulo`. |
| `saude[]` | `componente`, `estado` (`ok`, `falha`, `desconhecido`), `verificado_em`, `detalhe` sanitizado. |
| `grupos` | `descobertos`, `selecionados`, `habilitados`. |
| `acervo` | `mensagens`, `md_locais`, `md_publicados`, `historico_recuperado`, `retidos`. |
| `publicacao` | `agendamento` (texto), `ultima_verificada`, `proxima_execucao`, `ultimo_evento`, `mutacoes_pendentes`. |
| `fontes` | rótulo de cada fonte; a ordem define a cor (fixa). |
| `mensagens_por_dia[]` | `dia` e uma contagem por fonte. |
| `mutacoes_por_dia[]` | `dia`, `edicoes`, `revogacoes`. |
| `cobertura` | `grupos` (rótulos), `dias`, `valores` como `[índice do grupo, índice do dia, mensagens]`. |
| `execucoes[]` | `id`, `tipo` (`automática`, `manual`, `simulação`), `inicio`, `fim`, `duracao_s`, `estado` (`pendente`, `executando`, `verificada`, `falhou`, `bloqueada`, `parcial`, `desconhecida`), `grupos`, `mensagens`, `arquivos_preparados`, `arquivos_verificados`, `erro`. |

Fontes prováveis no adaptador real, a confirmar: `messages.sent_at` agrupado por dia em `America/Sao_Paulo`; `raw_events.source` para separar webhook, `history.import` e exportação; `messages` com edição ou revogação para mutações; registro de execuções do publicador (formato ainda não definido, ver ENG-02). Rótulos de grupo no painel real vêm do catálogo autorizado, nunca do ID técnico.

## Cores

Tokens do FGV Projetos Design System. As três séries foram validadas com o validador de paleta (claro e escuro, separação para daltonismo, contraste):

| Série | Claro | Escuro |
|---|---|---|
| Ao vivo (webhook) | `#008bc9` | `#1597d4` |
| Histórico GOWS | `#6f9a3a` | `#6a9e34` |
| Exportação TXT | `#5b4fb0` | `#9a7fe0` |

A ordem é fixa: azul e roxo ficam separados pelo verde, porque lado a lado não passam no modo escuro. Estados (operando, falha, alerta) usam as cores de status com ícone e rótulo, nunca a cor sozinha.

`vendor/echarts.min.js` é o Apache ECharts 5.5.1 (licença Apache 2.0, cabeçalho preservado no arquivo).
