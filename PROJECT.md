# ASPONE — contexto e regras do projeto

## REGRAS FIXAS (ler antes de qualquer trabalho)

Regras confirmadas pelo responsável na concepção do ASPONE; revisar somente mediante autorização.

- **Independência:** base de conhecimento não subordinada a uma aplicação ou interface.
- **Reutilização e governança:** diferentes aplicações e pessoas podem consumir conhecimento conforme permissões.
- **Preservação e rastreabilidade:** manter fontes originais, versões e referências, separadas de extrações, inferências e validações.
- **Evolução auditável:** permitir complementar, corrigir, contradizer e substituir informações, preservando o que mudou, quando, por quem e por quê.
- **Curadoria humana:** correções durante o uso devem poder realimentar o conhecimento sem exigir edição manual de Markdown como interface final.
- **Evolução incremental:** hipóteses não são decisões; avaliar soluções existentes antes de construir componentes próprios.
- **Confidencialidade:** este GitHub é público; não registrar dados, credenciais ou conteúdo profissional restrito.

Referência: [README de concepção](README.md); [consolidação e correção](docs/conhecimento/README.md).

## QUESTÃO CENTRAL

Como organizar e manter conhecimento confiável, rastreável, evolutivo e reutilizável a partir de fontes heterogêneas, independentemente das aplicações consumidoras?

## Finalidade

Desenvolver progressivamente uma infraestrutura para ingestão, processamento, organização, manutenção e recuperação de informações e conhecimentos, servindo a RAG, agentes e aplicações como Watchtower, Chapa e Chefe de Gabinete.

## Escopo

**Capacidades:** (1) acervo documental para localizar, consultar e comparar fontes históricas; (2) memória de conhecimento para acontecimentos, projetos, decisões, premissas, responsabilidades, correções e pendências.

**Fontes possíveis:** documentos, PDFs, planilhas, apresentações, e-mails, mensagens, atas, transcrições e anotações. Ata e transcrição são fontes diferentes e relacionadas.

**Fora de compromisso nesta fase:** arquitetura de produção definitiva, plataforma multiusuário completa, ingestão indiscriminada de dados e aprovação automática de conhecimento pela IA.

## Situação documentada

O repositório já possui documentação de produto e engenharia em `docs/` e um núcleo experimental de ingestão de WhatsApp em `modules/whatsapp/`. O README informa validação da primeira integração em laboratório, não a existência de plataforma integrada. Consultar `docs/evolucao.md` para maturidade e limites, e verificar o ambiente autorizado antes de afirmar estado operacional.

## Pastas e fontes de verdade

| Local | Responsabilidade |
| --- | --- |
| `README.md` | Apresentação e navegação pública |
| `docs/` | Documentação canônica de produto, arquitetura e engenharia; [índice](docs/README.md) |
| `modules/` | Código experimental versionado, quando existente |
| `PROJECT.md`, `NOW.md`, `TASKS.md` | Memória de desenvolvimento: fundamentos, situação e continuidade |
| `_wiki/` | Pesquisas e conhecimento reutilizável **sobre o desenvolvimento**; [índice](_wiki/INDEX.md) |
| `history/` | Decisões e trajetória de desenvolvimento |
| `z.old/` | Arquivos substituídos, quando autorizada a movimentação; não apagar sem decisão humana |

`TASKS.md` não concorre com o [backlog detalhado](docs/backlog.md).

## Configuração da memória

- Referência adotada: **Project Memory 3.1.0**, estrutura `history/`, inicialização autorizada em 20/11/2026.
- Frontmatter: **perfil**.
- Domain: A definir.
- Cliente: A definir.
- Contrato / engagement: A definir.
- Organização: A definir.
- Achados: `_wiki/achados.md` (criar apenas quando necessário).
- Novas páginas da wiki e registros de history: usar `type`, `date_created`, `date_modified`, `related`, `domain`, `client`, `engagement` e `organization`.

## Pessoas e validações

A pessoa responsável define decisões e valida conteúdo. Agentes podem pesquisar, sugerir e registrar propostas como `REQUIRES_REVIEW`; não presumir validação humana.

## Referências de continuidade

- [Documentação existente](docs/README.md)
- [Situação documentada e critérios](docs/evolucao.md)
- [Backlog canônico](docs/backlog.md)
- [Memória de desenvolvimento](_wiki/INDEX.md)
- [Registro de inicialização](history/2026-11-20-inicializacao-memoria.md)
