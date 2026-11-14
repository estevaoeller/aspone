# To-do list do ASPONE

**Atualizado:** 14/11/2026. **Natureza:** backlog vivo de produto e engenharia. Não representa estado operacional. A ordem dos grupos abaixo é uma organização proposta, não compromisso de prazo ou implementação.

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
- [ ] **ENG-02 — Publicação periódica:** instalar e validar agendamento, logs, bloqueios e tratamento de falhas; periodicidade proposta de uma hora.
- [ ] **ENG-03 — Backup e recuperação:** definir destino autorizado, política, retenção, periodicidade e restauração testada; dumps pontuais não bastam.
- [ ] **ENG-04 — Observabilidade e qualidade:** medir coleta, lacunas, mutações não reconciliadas, duplicidade, integridade, atualização e disponibilidade.
- [ ] **ENG-05 — Governança:** mapear acesso por fonte e finalidade, proteção de dados, retenção, retirada, revisão de permissões e responsabilidade pela publicação.

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
