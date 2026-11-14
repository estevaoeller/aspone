# Modelo de dados, identidade e proveniência

## PostgreSQL

| Tabela | Função | Identidade |
| --- | --- | --- |
| raw_events | Eventos recebidos e importados, payload JSONB, data de recepção, fonte e tipo | fingerprint único |
| messages | Estado materializado da mensagem, conversa, remetente, data original, corpo, mídia, edição e revogação | sessão + message_id |
| chat_names | Nomes de conversas | sessão + chat_id |
| contact_names | Nomes de remetentes e nomes públicos | sessão + contact_id |

A identidade de conversa é sessão + conversation_id. Não usar nome do grupo como chave. O dia de publicação é derivado de sent_at no fuso America/Sao_Paulo. Os dados brutos incluem conteúdo pessoal e não devem ser distribuídos integralmente.

## Mutações

O GOWS pode fornecer identificadores curtos em editedMessageId e revokedMessageId. O coletor resolve o alvo por sessão, contexto da conversa e componente do ID, exige correspondência única, reconcilia eventos em ordem de recepção e mantém revogação persistente. Edições tardias podem exigir ordenação melhor; eventos ambíguos ou sem correspondência precisam de investigação. A publicação oculta o corpo revogado; o evento original permanece na base restrita. Isso não apaga cópias ou versões remotas.

## Histórico

O piloto de backfill lê SQLite GOWS em modo somente leitura, valida identidade e horário, exclui conservadoramente eventos e alvos de mutação, conteúdo efêmero/de visualização única e formatos não suportados, importa em lotes de até 50 e registra proveniência history.import e hash da origem. Não substitui registros existentes. A importação TXT oficial, implementada em script distinto, usa identidade de exportação separada; não unificar automaticamente com registros live.

## Projeções

Markdown interno: conversa/dia, hash de sessão e ID, nome, remetente, ID original e corpo quando permitido. Markdown compartilhado: conversa/dia, texto e horário, marcação de edição/revogação, indicação de mídia, sem IDs técnicos ou remetentes por padrão. Ambos são derivados, mas possuem públicos e finalidades diferentes. O contrato para referência rastreável por aplicações consumidoras sem expor identificadores pessoais ainda não está definido.

## Relações

- [Implantação](implantacao.md)
- [Distribuição](sharepoint.md)
- [Código do coletor](../../../modules/whatsapp/README.md)
