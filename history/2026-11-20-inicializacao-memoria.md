---
domain: A definir
type: Project History
client: A definir
engagement: A definir
organization: A definir
date_created: 20/11/2026
date_modified: 20/11/2026
related:
  - "[[project-memory]]"
  - "[[framework-avaliacao]]"
---

# 20/11/2026 — Inicialização da memória de desenvolvimento

**`HUMAN_VALIDATED` para a autorização da estrutura.** Avaliações e propostas editoriais criadas nesta rodada são `REQUIRES_REVIEW`.

## 1. Onde estávamos

O ASPONE é uma infraestrutura de conhecimento em desenvolvimento, com documentação e módulo experimental WhatsApp já registrados no GitHub. A conversa identificou a necessidade de preservar também a evolução das ideias, pesquisas, hipóteses e decisões entre sessões e agentes.

## 2. Decisão da pessoa

> "Quero criar uma espécie de project memory, a minha skill de memória, wiki etc nele, para irmos construindo a ideia, registrando por la a evolução das ideias, do conhecimento, etc"

Ao ser proposta a inicialização pelo padrão da Project Memory 3.1.0 no repositório do ASPONE:

> "Sim, pode"

O consentimento cobre a inicialização e o registro inicial; não aprova escolhas futuras de arquitetura para a infraestrutura ASPONE.

## 3. O que encontramos

- O repositório já contém documentação canônica em `docs/` e código experimental em `modules/whatsapp/`, além de `README.md`.
- O repositório da skill encontra-se hoje na versão 3.2.0, com pasta `_history/`. Esta inicialização mantém a estrutura `history/` da versão 3.1.0 expressamente combinada; eventual migração depende de nova decisão.
- Como o repositório ASPONE é público e a skill fonte atualmente é privada, não se copiou o conteúdo da skill para o projeto público. Em vez disso, adotaram-se regras operacionais suficientes em `AGENTS.md`.

## 4. Arquivos criados

`AGENTS.md`, `CLAUDE.md`, `PROJECT.md`, `NOW.md`, `TASKS.md`, `_wiki/INDEX.md`, modelos de páginas, notas de pesquisa em `_wiki/solucoes/` e registros em `history/`. Nenhum arquivo preexistente foi substituído nesta inicialização.

## 5. O que permanece aberto

- Revisar conteúdo analítico com marca `REQUIRES_REVIEW`.
- Deliberar apenas quando necessário sobre futura convergência com a convenção 3.2.0.
- Manter `docs/backlog.md` como backlog de produto e engenharia, evitando tarefas duplicadas.
