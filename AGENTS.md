# AGENTS — ASPONE

Responder em português brasileiro. Este repositório é público.

## Início de cada sessão
1. Ler `PROJECT.md`, `NOW.md` e `TASKS.md`, nesta ordem; observar as regras fixas no início de `PROJECT.md`.
2. Antes de retomar tema já estudado, consultar o índice `_wiki/INDEX.md` e os registros relevantes em `history/`.
3. Consultar `docs/README.md` e os documentos de `docs/` quando a questão envolver negócio, arquitetura, implantação, backlog ou implementação. Não inferir estado operacional atual apenas da documentação.
4. Ler apenas as fontes relevantes: não varrer todo o repositório em cada sessão.

## Destinos deste projeto
| Informação | Destino canônico |
| --- | --- |
| Objetivo, princípios e regras fixas | `PROJECT.md` |
| Situação atual, limites da evidência, próximo passo | `NOW.md` |
| Próximos passos de concepção e memória documental | `TASKS.md` |
| Backlog de produto e engenharia, IDs e critérios de conclusão | `docs/backlog.md` (não duplicar em TASKS) |
| Conhecimento consolidado de negócio, arquitetura, ingestão, contexto e correções | `docs/` e seu índice `docs/README.md` |
| Pesquisas de referências, avaliações de ferramentas e método de memória do projeto | `_wiki/`, com entrada em `_wiki/INDEX.md` |
| Decisões e trajetória de desenvolvimento da memória do projeto | `history/AAAA-MM-DD-tema.md` |
| Achados ainda sem documento próprio | `_wiki/achados.md` (criar somente quando necessário) |
| Planos aprovados | `_wiki/planos/<assunto>.md` e seu INDEX (criar quando necessário) |
| Perguntas a terceiros | `PERGUNTAS.md` (criar na primeira) |

## Ao trabalhar
- Distinguir fatos observados, propostas, interpretações de IA, decisões aprovadas e pendências.
- `REQUIRES_REVIEW` ou `AI_PROPOSED` sinaliza conteúdo de IA não validado; somente confirmação humana autoriza `HUMAN_VALIDATED`.
- Preservar originais; não sobrescrever, reorganizar ou substituir documentação canônica sem necessidade e autorização. Ao invés de duplicar `docs/`, criar links na wiki.
- Registrar fonte, data, escopo e limitações de afirmações; não inferir que uma ferramenta está implantada a partir de um desenho.
- Não transformar hipóteses em decisões, nem realizar implementação técnica sem solicitação.
- Não publicar credenciais, dados pessoais, mensagens reais, documentos profissionais restritos ou detalhes operacionais privados.

## Encerrar cada passo relevante
Gatilhos: decisão, mudança de direção, aprendizado relevante, nova regra, pendência ou arquivo criado/alterado. Sem gatilho, não registrar.

- Atualizar `NOW.md` e `TASKS.md` somente no que tiver mudado.
- Registrar a decisão ou trajetória em `history/` com data, motivo, evidência e alternativa considerada.
- Registrar aprendizado reutilizável na página pertinente da `_wiki/`, indexando a página; se já houver documento canônico em `docs/`, preferir vinculá-lo.
- Não reescrever silenciosamente conhecimento corrigido ou substituído: preservar estado anterior e o vínculo com o novo.
- Confirmar no final quais arquivos foram efetivamente gravados e o que permanece aberto.

## Concorrência e segurança
- Reabrir arquivos antes de atualizar; não desfazer alterações feitas por outro agente.
- Preferir adições datadas a reescrever o trabalho de outra sessão.
- Commits e edições remotas exigem autorização da pessoa; esta inicialização foi autorizada explicitamente.
- Não copiar o código de uma skill de repositório privado para este repositório público sem autorização específica.
- Observar a configuração de frontmatter de `PROJECT.md`. 

## Referência operacional
Este repositório adota as convenções da Project Memory 3.1.0 como referência de trabalho; suas regras necessárias estão explicitadas aqui. A implementação experimental do ASPONE e a documentação de produto em `docs/` são objetos distintos desta memória de desenvolvimento.
