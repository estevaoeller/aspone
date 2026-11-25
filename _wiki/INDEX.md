# Índice da memória de desenvolvimento do ASPONE

**Questão central:** como construir uma infraestrutura independente, confiável, rastreável, evolutiva e reutilizável de conhecimento?

**Regras fixas:** [PROJECT.md](../PROJECT.md). **Estado:** [NOW.md](../NOW.md). **Pendências:** [TASKS.md](../TASKS.md). **Histórico:** [history/](../history/README.md).

## Documentação canônica já existente

A documentação de produto e engenharia continua em `docs/`; estas páginas são fontes de referência, não devem ser copiadas sem necessidade.

- [Mapa da documentação](../docs/README.md): entrada principal para documentação existente.
- [Arquitetura](../docs/arquitetura.md): fronteiras entre ingestão, acervo, memória e consumidores.
- [Alimentação multifuente](../docs/alimentacao/README.md): fontes e preservação de originais.
- [Contexto e vínculos](../docs/contexto/README.md): projetos, equipes, calendário e reuniões.
- [Consolidação e correções](../docs/conhecimento/README.md): proposta de conhecimento vigente e corrigível.
- [Evolução](../docs/evolucao.md): estágio documentado das frentes.
- [Backlog](../docs/backlog.md): tarefas de produto e engenharia com IDs e critérios.

## Pesquisas, referências e método de memória

- [Project Memory aplicada ao ASPONE](solucoes/project-memory.md): convenções, fronteiras da wiki e manutenção entre agentes. `REQUIRES_REVIEW`
- [AI Memory — referência de pesquisa](solucoes/ai-memory.md): registro da solução externa e questões de avaliação, ainda sem validação de implementação. `REQUIRES_REVIEW`
- [Ariso / TRAM — referência de pesquisa](solucoes/ariso-tram.md): ciclo TRAM, aspectos aproveitáveis e diferenças frente ao ASPONE. `REQUIRES_REVIEW`
- [Framework para avaliar soluções](solucoes/framework-avaliacao.md): critérios comparativos propostos, sem decisão tecnológica. `REQUIRES_REVIEW`

## Conceitos e referências teóricas

- [Open Knowledge Format (OKF) — fundamentos, estrutura e semântica](referencias/okf-open-knowledge-format.md): especificação, metadados, proveniência e limites do formato. `REQUIRES_REVIEW`
- [Conceitos fundamentais para a confiança e evolução do conhecimento](referencias/conceitos-fundamentais-confianca-conhecimento.md): proveniência, verificação, validade temporal, histórico, versionamento, rastreabilidade e auditabilidade; correspondências ao glossário e à ontologia. `REQUIRES_REVIEW`

**Relação com a wiki do Homelab:** esta `_wiki/` pública é a referência de trabalho e compartilhamento dos estudos conceituais do ASPONE. A wiki operacional privada do Homelab mantém cópias de consulta e registros de experimentos e implantação, não versões automaticamente sincronizadas nem autoridade sobre as definições deste projeto. Em divergências conceituais futuras, consultar primeiro esta wiki e registrar o conflito antes de corrigir qualquer cópia. O repositório de glossário e ontologia da FGV Projetos é fonte institucional externa a harmonizar, sem dependência estrutural.

## Camada de Conhecimento e Verdade dos Projetos — discussão iniciada em 20/11/2026

- **[Definição e três camadas do ASPONE](../docs/conhecimento/camada-conhecimento-verdade.md)** — artigo canônico de produto: armazenar, recuperar e manter conhecimento; ingestão, conhecimento e consumo. `REQUIRES_REVIEW`
- [Fonte, afirmação, evidência e validação](conceitos/fonte-afirmacao-conhecimento.md) — o que um registro permite afirmar e o que exige confirmação. `REQUIRES_REVIEW`
- [Gestão do conhecimento durante o ciclo do projeto](conceitos/gestao-conhecimento-ciclo-vida.md) — memória cotidiana, pós-projeto e relação conceitual com Knowledge Advisor. `REQUIRES_REVIEW`
- [W3C PROV](referencias/w3c-prov.md) — padrão de proveniência, suas relações e limites, com referências oficiais. `REQUIRES_REVIEW`
- [Histórico bitemporal](referencias/historico-bitemporal.md) — validade e tempo do registro, com referências de Fowler, SQL:2011, IBM e Snodgrass. `REQUIRES_REVIEW`

## Trajetória

- [20/11/2026 — Camada de Conhecimento e Verdade](../history/2026-11-20-camada-conhecimento-verdade.md): definição inicial, artigos ligados, referências W3C PROV e bitemporal. Orientação documental `HUMAN_VALIDATED`; textos `REQUIRES_REVIEW`.
- [20/11/2026 — Referências teóricas e fronteira entre wikis](../history/2026-11-20-referencias-aspone-e-homelab.md): publicação de artigos e distinção entre wiki pública e wiki privada. `HUMAN_VALIDATED` para a orientação de localização; conteúdo técnico `REQUIRES_REVIEW`.
- [20/11/2026 — Inicialização da memória](../history/2026-11-20-inicializacao-memoria.md): autorização, escolhas, preservação de documentos e pendências. `HUMAN_VALIDATED` para a autorização; análises `REQUIRES_REVIEW`.

## Convenções

Marcar o que é proposto pela IA como `AI_PROPOSED` / `REQUIRES_REVIEW`. Somente decisão humana justifica `HUMAN_VALIDATED`. Atualizar páginas existentes em vez de criar duplicatas. A revisão de um entendimento deve manter referência ao registro anterior e ao motivo da mudança.

## Identidade e dados anotados (25/11/2026)

- [Identidade e cadastro compartilhado](../docs/contexto/identidade-e-cadastro.md)
- [Anotações e proveniência](../docs/conhecimento/anotacoes-e-proveniencia.md)
- [Implementação incremental](../docs/conhecimento/implementacao-camada-estruturada.md)
- [Registro histórico](../history/2026-11-25-identidade-e-dados-anotados.md)

Documentos canônicos de concepção, `REQUIRES_REVIEW`.
