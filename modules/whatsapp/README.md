# Código da integração WhatsApp

Este diretório contém uma fotografia do núcleo do coletor examinado em 14/11/2026. Não é um pacote de implantação integral nem uma nova versão instalada no host. Os arquivos de ingestão foram copiados do código real; a configuração de ambiente e dados reais não foram copiados.

| Arquivo | Responsabilidade |
| --- | --- |
| [server.py](ingest/server.py) | Webhook, persistência, mutações, projeção interna |
| [sync_names.py](ingest/sync_names.py) | Consulta GET e atualização de nomes |
| [validate.py](ingest/validate.py) | Conferência de correspondência DB/Markdown |
| [import_export.py](ingest/import_export.py) | Importação de TXT oficial, com identidade separada |
| [Dockerfile](ingest/Dockerfile) | Imagem do coletor |

## Scripts existentes ainda não portados para o repositório público

publish.sh, publish.py, init_groups.py, test_publish.py, backfill_extract.py e backfill_import.py: seleção, renderização de publicação, verificação e recuperação histórica. Os originais dependem de caminhos, destino, catálogo e decisões da instalação específica. Foram mantidos no ambiente privado; serão parametrizados e revisados antes da inclusão pública. Scripts de migração e autorização inicial são histórico operacional, não interfaces estáveis de produto.

Não usar configurações ou exemplos reais como fixtures. Não incluir .env, tokens, catálogos privados, arquivos de sessão, mensagens, dumps ou logs. Para executar o núcleo, configurar Docker Compose, PostgreSQL, variáveis de ambiente e mounts conforme a [implantação técnica](../../docs/integracoes/whatsapp/implantacao.md). O validador usa /data/markdown como caminho de referência. O código não foi reimplantado a partir deste snapshot.

## Relações

- [Integração WhatsApp](../../docs/integracoes/watchtower-whatsapp.md)
- [Dados](../../docs/integracoes/whatsapp/dados.md)
