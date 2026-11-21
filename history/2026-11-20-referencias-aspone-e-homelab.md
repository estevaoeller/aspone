---
domain: ASPONE
type: Project History
client: A definir
engagement: A definir
organization: A definir
date_created: 20/11/2026
date_modified: 20/11/2026
related:
  - "[[okf-open-knowledge-format]]"
  - "[[conceitos-fundamentais-confianca-conhecimento]]"
  - "[[ai-memory]]"
---

# 20/11/2026 — Referências teóricas e fronteira entre a wiki do ASPONE e a do Homelab

**Estado da orientação documental:** `HUMAN_VALIDATED`, conforme pedido expresso da pessoa responsável. **Estado das análises técnicas:** `REQUIRES_REVIEW`. Não há decisão de implementar OKF ou AI Memory.

## Contexto e motivação

Dois estudos — OKF e conceitos de proveniência, verificação, validade temporal, histórico e auditoria — foram inicialmente registrados na wiki central privada do Homelab, usada para conhecimento operacional. O usuário esclareceu que essas referências também precisam estar na wiki de trabalho do ASPONE, mantida no GitHub e compartilhável com outras pessoas.

## Encaminhamento confirmado

- `_wiki/` no repositório público ASPONE passa a ser a **referência documental de trabalho** para esses dois artigos conceituais e suas próximas revisões.
- `docs/` continua responsável pela documentação de produto, arquitetura e engenharia; as páginas existentes devem apenas remeter aos estudos para evitar duplicação de definições.
- A wiki privada do Homelab pode manter cópias de consulta e conhecimento específico de ambiente/implementação. Não há sincronização automática nem equivalência de versões.
- A ontologia institucional da FGV Projetos é outra fonte conceitual útil, mas não está subordinada ao ASPONE; diferenças terminológicas devem ser documentadas e discutidas antes de unificação.

## Arquivos de referência

- [Estudo OKF](../_wiki/referencias/okf-open-knowledge-format.md).
- [Conceitos fundamentais de confiança e evolução do conhecimento](../_wiki/referencias/conceitos-fundamentais-confianca-conhecimento.md).
- [Índice da wiki de trabalho](../_wiki/INDEX.md).
- [Consolidação e correção](../docs/conhecimento/README.md).

## Verificação e pendências

Os dois artigos foram publicados no repositório público, com remissões internas ao material de memória e documentação de produto. Permanecem pendentes revisão conceitual humana e eventual harmonização com o glossário e a ontologia. A simples transferência de textos não constitui teste do software, validação técnica ou compromisso de adoção.

**Alternativa não adotada:** manter os artigos apenas na wiki privada do Homelab. Isso dificultaria leitura pelos colaboradores e misturaria pesquisa comum com documentação operacional privada.
