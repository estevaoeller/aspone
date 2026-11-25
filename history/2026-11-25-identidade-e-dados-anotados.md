---
type: Documentation
date_created: 25/11/2026
date_modified: 25/11/2026
related:
  - ../docs/contexto/identidade-e-cadastro.md
  - ../docs/conhecimento/anotacoes-e-proveniencia.md
  - ../docs/conhecimento/implementacao-camada-estruturada.md
domain: A definir
client: A definir
engagement: A definir
organization: A definir
---

# 25/11/2026: identidade e dados anotados

## Contexto e direcionamento

A discussão partiu da descoberta de projetos em fontes heterogêneas e da dificuldade de repetir a resolução de identidade em cada análise. O responsável solicitou pensar em código compartilhado para dar consistência à camada anotada e explicitou que identificadores curtos são insuficientes para pessoas, documentos e evidências. Solicitou consolidar os entendimentos e explicações no GitHub.

## Distinção de estados

- HUMAN_VALIDATED quanto ao direcionamento de documentar e à exigência de capacidade adequada de identificadores.
- REQUIRES_REVIEW quanto à escolha ULID, prefixos, modelo de entidades, representação de anotações, tabelas e fases.
- Princípios preexistentes preservados: independência, originais, proveniência, curadoria e evolução auditável.
- Alternativas consideradas: sequência curta, Base36, ULID, UUIDv7; armazenamento estruturado versus projeções de consulta. Não houve seleção tecnológica definitiva.

## Evidência e limites

Discussão de concepção em 25/11/2026, precedida por exploração somente leitura de fontes autorizadas. Este registro público não contém nomes de projetos reais, mensagens, caminhos privados, identificadores de origem ou links profissionais. Os exemplos dos novos documentos são sintéticos. A exploração não equivale a validação do modelo nem a implantação. Não foram modificados banco, fontes ou cadastro de projetos por esta consolidação.

## Continuidade

Revisar identidade, granularidade, permissões, estados e opções técnicas; em seguida propor piloto sintético com testes de idempotência e correção. Ver documentos relacionados no frontmatter e o backlog existente.
