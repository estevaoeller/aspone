# To-do list do ASPONE

**Atualizado:** 15/11/2026. **Natureza:** backlog vivo de produto e engenharia. Não representa estado operacional. A ordem dos grupos abaixo é uma organização proposta, não compromisso de prazo ou implementação.

## Como manter

Cada item possui ID estável, entregável e critério de conclusão. Marcar como concluído apenas quando houver evidência ou documento ligado ao item. Novas ideias entram como descoberta; decisões tecnológicas, prioridades e implantação são deliberadas separadamente. Não incluir dados reais de projetos, reuniões ou equipes neste repositório público.

## A. Alimentação de fontes

- [x] **ALI-01 — Piloto WhatsApp:** coleta, persistência, projeção diária e primeira publicação seletiva verificadas. Evidência: [integração WhatsApp](integracoes/watchtower-whatsapp.md).
- [ ] **ALI-02 — Recuperação histórica WhatsApp:** generalizar backfill por grupos e lotes, checkpoint, identidade, mutações e validação. Piloto de um lote concluído; generalização pendente.
- [ ] **ALI-03 — Transcrições de reunião:** descobrir onde o Teams armazena e disponibiliza os artefatos, por tipo de reunião; testar acesso autorizado, registro da origem, recuperação e distribuição no acervo comum. Relacionar transcrição à reunião correspondente (CTX-03/04).
- [ ] **ALI-04 — Atas:** definir aquisição de atas existentes e processo de elaboração/revisão a partir de transcrições, mantendo minuta, versão aprovada e fontes separadas. Depende de ALI-03 e CTX-03/04 para geração a partir de reuniões.
- [ ] **ALI-05 — E-mails:** investigar seleção, contas/caixas/pastas autorizadas, threads, anexos, metadados e associação aos projetos. Não importar indiscriminadamente caixas completas.
- [ ] **ALI-06 — Documentos e anotações:** mapear locais de origem, versões, registro de recebimento/envio, classificação e disponibilidade para consumidores.
- [ ] **ALI-07 — Contrato comum de ingestão:** definir identidade da fonte, localização original, aquisição, versão, permissões, proveniência, atualização e tratamento de falhas; testar em WhatsApp e uma segunda fonte.

## B. Contexto e cadastros compartilhados

- [ ] **CTX-01 — Cadastro de projetos:** definir identificador estável, nome, situação, período, referências e vínculos; distinguir projeto de grupo de conversa, pasta, reunião e assunto. Critério: exemplo fictício completo e relações testáveis.
- [ ] **CTX-02 — Equipes e pessoas:** definir papéis, participação por projeto e vigência das relações; distinguir participantes, responsáveis e autorizadores. Não inferir permissões apenas pela equipe.
- [ ] **CTX-03 — Calendário comum:** investigar agenda compartilhada e/ou visão federada das agendas autorizadas; definir fonte de verdade, responsáveis, acesso e como identificar reuniões de projetos.
- [ ] **CTX-04 — Registro de reuniões:** relacionar evento de calendário, ocorrência efetiva, projeto(s), participantes e artefatos; diferenciar agendada, realizada, cancelada e não confirmada. Tratar reuniões recorrentes, remarcações e transcrições tardias.
- [ ] **CTX-05 — Associação de fontes:** definir processo para relacionar conversas, e-mails, atas, documentos e reuniões aos projetos, inclusive relações múltiplas e revisão humana.

## C. Consolidação, correção e memória de conhecimento

- [ ] **MEM-01 — Modelo de conhecimento:** distinguir evidência, afirmação, interpretação, decisão, premissa, regra, pendência, dúvida e anotação; definir campos mínimos e relações.
- [ ] **MEM-02 — Correção de anotações:** desenhar fluxo para registrar proposta de correção, evidência, autor, data, motivo, revisão e resultado; preservar versão anterior e permitir nova correção. Não depender de edição manual de Markdown como interface final.
- [ ] **MEM-03 — Vigência e autoridade:** estabelecer como identificar o que está valendo, o que foi substituído, o que foi rejeitado e o que permanece em discussão; definir quem pode validar cada tipo de informação e em qual contexto.
- [ ] **MEM-04 — Consolidação por projeto e assunto:** definir os artefatos de consulta (decisões, regras vigentes, premissas, pendências e histórico), local de armazenamento e responsável por atualização. Testar com um projeto fictício.
- [ ] **MEM-05 — Processamento e revisão:** definir como IA propõe extrações, conflitos e relacionamentos, como humanos validam ou corrigem e como mudanças chegam a consumidores. Não promover automaticamente texto de conversa a decisão.
- [ ] **MEM-06 — Referências e rastreabilidade:** permitir voltar de uma afirmação consolidada à fonte e sua versão, mesmo após correções; testar conflitos, substituição parcial e reprocessamento.

## D. Distribuição e consumo

- [ ] **DIS-01 — Repositório comum SharePoint:** definir organização por tipo de fonte, navegação, permissões e critérios para referenciar original ou copiar representação autorizada; não pressupor acesso universal.
- [ ] **DIS-02 — Contrato de consumo:** definir como aplicações detectam novos documentos, alterações, retirada e versões, e como citam as evidências. Validar com dois consumidores.
- [ ] **DIS-03 — Revisão de produtos:** desenhar piloto de uso do acervo como evidência contextual para revisão, sem substituir fontes oficiais nem aprovação humana.
- [ ] **DIS-04 — Memória de projetos e demais sistemas:** definir integração com Watchtower, Chapa, Chefe de Gabinete e outros consumidores conforme necessidades reais.

## E. Engenharia e continuidade

- [ ] **ENG-01 — Versionar publicador e backfill:** parametrizar código, remover dependências privadas, testar e documentar Compose reproduzível.
- [ ] **ENG-02 — Publicação periódica:** instalar e validar agendamento, logs, bloqueios e tratamento de falhas; periodicidade diária às 03h00 (horário do servidor), definida em 16/11/2026; agendamento instalado e teste manual concluído. Confirmar primeira execução automática e alertas.
- [ ] **ENG-03 — Backup e recuperação:** definir destino autorizado, política, retenção, periodicidade e restauração testada; dumps pontuais não bastam.
- [ ] **ENG-04 — Observabilidade e qualidade:** medir coleta, lacunas, mutações não reconciliadas, duplicidade, integridade, atualização e disponibilidade.
- [ ] **ENG-05 — Governança:** mapear acesso por fonte e finalidade, proteção de dados, retenção, retirada, revisão de permissões e responsabilidade pela publicação.

## F. Evolução da integração WhatsApp (ASPONE / Watchtower)

Detalhamento das frentes WH, vinculado aos itens gerais de alimentação, distribuição e engenharia. As prioridades abaixo indicam sequência de discussão, não implantação.

### P0 — Histórico e continuidade

- [ ] **WH-01 — Recepção de ZIP/TXT:** identificar a exportação enviada à conversa consigo mesmo; baixar apenas documentos explicitamente selecionados, preservar arquivo original e hash, extrair TXT de ZIP com limites de tamanho e proteção contra caminhos externos. Não exigir descompactação manual no celular. Critério: uma exportação real recebida e validada sem captura indiscriminada de mídia. Piloto manual de download seletivo concluído e integridade do ZIP verificada; rotina de processamento em lote com download seletivo, tentativas limitadas e registro por arquivo implementada em 15/11/2026; agendamento permanente ainda pendente.
- [ ] **WH-02 — Histórico oficial (ALI-02):** importar exportações sem mídia, associar a conversa ao cadastro, reconciliar sobreposição com WAHA, preservar proveniência e tratar ambiguidades, edições e revogações. Processar um ZIP completo por grupo quando o arquivo já estiver disponível localmente, sem limite mensal artificial; limitar e controlar separadamente as requisições externas ao WhatsApp, sem reconfigurar a sessão corrente. Critério: importação repetível, sem duplicidades, com publicação somente de histórico autorizado. Piloto de importação de um mês anterior à janela WAHA concluído em 15/11/2026, com proveniência, IDs sintéticos, teste de reexecução e projeção diária validados; importação integral do primeiro ZIP validada em 15/11/2026, sem duplicidade na reexecução; rotina de lote para múltiplos ZIPs autorizados validada em 15/11/2026, inclusive arquivos com cartões VCF auxiliares preservados sem extração, reutilização de cache por hash e teste de reexecução; reconciliação da sobreposição e reexportações distintas permanecem pendentes.
- [ ] **WH-03 — Sincronização diária às 03h00 (ENG-02):** atualização incremental do SharePoint, inclusive dias históricos corrigidos; lock, logs, alertas e verificação de transferência, sem exclusão automática. Critério: execução periódica comprovada e rollback documentado. Agendamento diário instalado em 16/11/2026, teste manual com nomes de exibição autorizados e verificação remota concluídos; comprovação da primeira execução automática e alertas pendentes.

### P1 — Arquivos e proteção de dados

- [ ] **WH-04 — Download seletivo:** política por origem, autorização e tipo (documento, áudio, imagem, exportação), com limites, falhas e retenção do cache.
- [ ] **WH-05 — Armazenamento:** distinguir entrada temporária, processamento, originais, derivados e quarentena; separar acervo pessoal e profissional, identidade de origem, permissões, checksum e retenção. Definir destino persistente antes da migração.
- [ ] **WH-06 — Backup (ENG-03):** avaliar replicação com rclone e backup versionado, destinos autorizados e separados por classificação, criptografia, verificação e restauração testada. A projeção no SharePoint não substitui backup integral.
- [ ] **WH-07 — Documentos:** definir extração de texto, OCR, metadados, indexação, associação a fontes e projetos, fila idempotente e reprocessamento.

### P2 — Áudio e processamento distribuído

- [ ] **WH-08 — Áudio:** captura seletiva, preservação do original, transcrição com timestamps e proveniência, revisão, vínculo à mensagem e publicação autorizada.
- [ ] **WH-09 — Workers de transcrição:** priorizar GPU local, avaliar ambiente alternativo como fallback e distribuir tarefas distintas entre workers simultaneamente disponíveis. Definir modelos, capacidade, custo, privacidade, retry e idempotência.
- [ ] **WH-10 — Worker externo:** avaliar pacote/script executado em computador autorizado, com intercâmbio de tarefas e resultados via SharePoint, sem exigir acesso à rede privada. Validar política de TI, permissões, autenticação, isolamento e auditoria antes da implantação.
- [ ] **WH-11 — Orquestração:** estudar fila, leases, roteamento por disponibilidade e capacidade, recuperação de falhas e prevenção de duplicidades; reutilizar a capacidade para OCR, embeddings e extração de documentos.

Nenhum arquivo de conversa, catálogo privado, nome de grupo, credencial ou configuração de ambiente integra este backlog público.

## G. Console de configuração e operação do Watchtower / ASPONE

- [ ] **UI-01 — Exploração e arquitetura:** mapear componentes existentes, fontes de verdade, permissões, fronteira administrativa e opções de implementação; propor wireframes e plano antes de alterar o runtime.
- [ ] **UI-02 — Console somente leitura:** visão geral, grupos descobertos/selecionados/publicados, estado da coleta, horário efetivo, última/próxima publicação e histórico de execuções.
- [ ] **UI-03 — Configuração e operação:** editar seleção, escopo autorizado e horário com validação, backup, lock e auditoria; simular/publicar manualmente pelo publicador existente, acompanhar jobs e falhas sanitizadas; não criar segundo coletor ou agendador.
- [ ] **UI-04 — Histórico e arquivos:** acompanhar exportações autorizadas, importação integral por grupo, retenções e reconciliação; evoluir para políticas de arquivos e workers somente após o MVP.

A interface administrativa deve permanecer privada, sem credenciais, comandos arbitrários ou dados reais no repositório. Não substituir a configuração efetiva nem interromper a coleta. Integrações com histórico e publicação preservam autorização explícita.

## Sequência sugerida de descoberta

1. Continuar estabilizando WhatsApp e distribuição; não interromper a alimentação já demonstrada.
2. Em paralelo, definir cadastro mínimo de projetos/equipes e vínculo reunião-calendário; investigar onde as transcrições Teams realmente ficam.
3. Pilotar reunião → transcrição → minuta de ata → validação → acervo comum.
4. Explorar e-mail e documentos, usando o mesmo contrato de fonte.
5. Pilotar consolidação e correção com evidências cruzadas antes de ampliar automação ou definir tecnologia definitiva de memória.

A sequência é proposta para revisão. Não existe prazo ou prioridade de entrega formalmente aprovado.

## Relações

- [Evolução e critérios](evolucao.md)
- [Alimentação multifuente](alimentacao/README.md)
- [Contexto compartilhado](contexto/README.md)
- [Consolidação e correção](conhecimento/README.md)
- [Arquitetura](arquitetura.md)
