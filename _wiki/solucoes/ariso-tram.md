---
domain: A definir
type: Project Wiki
client: A definir
engagement: A definir
organization: A definir
date_created: 20/11/2026
date_modified: 20/11/2026
related:
  - "[[ai-memory]]"
  - "[[framework-avaliacao]]"
---

# Ariso e TRAM — referência para o ASPONE

`REQUIRES_REVIEW`. Síntese da avaliação discutida, não decisão de implementação.

## Fontes de referência

- Guia: https://ariso.ai/guides/build-your-own-chief-of-staff
- Ensaio: https://ariso.ai/blog/the-hardest-thing-about-work-isnt-the-work
- Especificação `tram-product-spec.md` e `chief-of-staff-starter-kit.zip` fornecidos na conversa de pesquisa; **não publicados aqui**. Links públicos acima não substituem a verificação desses anexos se houver revisão detalhada.

## Conceito útil

TRAM = Track (acompanhar), Report (comunicar), Align (alinhar), Measure (avaliar). É um ciclo de assistência ao acompanhamento do trabalho, não uma infraestrutura completa de acervo e memória federada.

A especificação distingue fonte bruta (`SourceItem`) de item de trabalho extraído (`WorkItem`), relacionando decisões, compromissos, riscos, pessoas e projetos. Propõe funções separadas para extrair, relacionar, relatar, avaliar alinhamento e refletir.

## O que pode inspirar o ASPONE

- Eventos e compromissos como dados relacionados às fontes, em vez de apenas resumos.
- Distinção entre **tarefa sugerida**, **compromisso assumido** e **decisão validada**.
- Preparação de reuniões, relatórios e acompanhamento como **aplicações consumidoras** de uma memória independente.
- Rastreamento de relações com fonte e revisão humana de extrações.

## Limitações em relação ao ASPONE

- Enfoque principalmente pessoal e operacional; não resolve sozinho governança de conhecimento multiusuário.
- Associação de itens à fonte não equivale a versionamento auditável completo de afirmações e decisões.
- Diário / linha do tempo não substituem documento, e-mail, ata ou transcrição original.
- Não aborda integralmente o histórico de circulação documental (recebimento, envio, versões e respostas).

## Situação

Referência conceitual e funcional; sem adoção da arquitetura ou do armazenamento proposto. Discussão ligada a [fontes e acervo](../../docs/alimentacao/README.md), [contexto](../../docs/contexto/README.md) e [consolidação](../../docs/conhecimento/README.md).
