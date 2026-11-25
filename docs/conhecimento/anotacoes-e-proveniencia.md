# Dados anotados, afirmações e proveniência

**Data:** 25/11/2026. **Estado:** REQUIRES_REVIEW. Complemento da camada de conhecimento, sem substituir o acervo.

## Modelo de responsabilidades

A camada intermediária reúne referências estruturadas e revisáveis, não cópias indiscriminadas das fontes. O conteúdo original permanece separado da interpretação; aplicações consultam ambas sob autorização. Uma projeção Markdown, CSV ou JSON não se torna fonte concorrente por existir.

~~~mermaid
flowchart TD
  F[Fontes originais] --> A[Acervo normalizado]
  A --> X[Extracao e anotacao]
  I[Identidade e aliases] --> X
  X --> C[Afirmações candidatas]
  C --> R[Revisao e conflitos]
  R --> K[Conhecimento validado]
  K --> I
  K --> U[Agentes, RAG e automacoes]
  A --> U
~~~

| Unidade | Responsabilidade |
| --- | --- |
| Fonte e versão | Identificar origem, conteúdo, data, integridade e disponibilidade |
| Anotação | Classificar ou interpretar trecho de fonte, com método e revisão |
| Afirmação | Proposição com sujeito, predicado, objeto, escopo, tempo e modalidade |
| Evidência | Apontador verificável a mensagem, trecho, documento ou versão |
| Relação | Vínculo semântico tipado; pode ser candidato, contestado ou validado |
| Revisão | Registrar decisão de curadoria, autor, motivo, evidências e mudança |

Uma afirmação pode ter várias evidências; uma evidência pode sustentar várias afirmações. Registrar se a evidência sustenta, contradiz ou contextualiza. Repetição de uma mesma fonte não é corroboração independente. Distinguir evidência de uma solicitação, execução, entrega, aceite e conclusão.

## Exemplo sintético de intercâmbio

Os valores são fictícios e ilustrativos; não constituem schema homologado.

~~~json
{
  "annotation_id": "ANN-01ARZ3NDEKTSV4RRFFQ69G5FAA",
  "source_ref": {
    "namespace": "example:whatsapp:workspace",
    "external_id": "synthetic-message-001",
    "version": "1",
    "locator": "message"
  },
  "event_at": "2099-03-10T10:00:00-03:00",
  "entity_links": [
    {
      "entity_id": "PRJ-01ARZ3NDEKTSV4RRFFQ69G5FAV",
      "method": "contextual_match",
      "review_status": "REQUIRES_REVIEW"
    }
  ],
  "assertions": [
    {
      "predicate": "responsibility_assigned",
      "object": "Revisar estimativa de despesas",
      "modality": "request",
      "basis": "explicit",
      "review_status": "REQUIRES_REVIEW"
    }
  ],
  "review_status": "REQUIRES_REVIEW"
}
~~~

A mensagem fictícia que solicita revisão demonstra uma atribuição, não que a revisão foi executada. O vínculo com o projeto pode ser inferido independentemente de o pedido ser explícito. Campos ausentes permanecem desconhecidos. Identidade, evidência e aprovação são independentes.

## Proveniência e deduplicação

Preservar a chave original com namespace (por exemplo, mensagem WhatsApp com sessão/conversa quando necessário; drive e item em armazenamento documental; identificador de e-mail com contexto da caixa). Para exportações sem chave original, registrar arquivo, membro do ZIP, localizador/linha, horário e método de importação; IDs derivados não são necessariamente IDs originais. Não usar caminho como identidade permanente.

SHA-256 é candidato para integridade de bytes e detecção de versões idênticas; não é identidade permanente do documento nem prova de autenticidade. Reexportações, edições e sobreposições precisam de reconciliação, sem restaurar registros revogados como se fossem vigentes. Preservar a origem de cada projeção. Anotar versão do extrator, configuração relevante, modelo quando usado, execução e data. Reprocessamento deve ser idempotente e não apagar revisão humana.

## Temporalidade e estados

Separar data do evento, data de captura, data de interpretação, validade no domínio e data da revisão. Uma decisão posterior pode substituir apenas parte de uma afirmação anterior. Manter histórico de correções e divergências. Usar as marcas já documentadas no projeto: AI_PROPOSED, REQUIRES_REVIEW, HUMAN_VALIDATED, REJECTED, SUPERSEDED. Vigência, conflito, revogação da fonte e aprovação de uma interpretação são dimensões distintas; não forçá-las a um único status.

A revisão registra autor, autoridade, data, justificativa, antes/depois, evidências e relação de substituição. Uma correção de alias validada deve orientar novas extrações e permitir reavaliar vínculos antigos, sem alterar automaticamente o conhecimento revisado. Consumidores devem diferenciar candidato de vigente e respeitar permissões das fontes.

## Qualidade da extração

Começar com janela delimitada e inventário de fontes, formatos, cobertura e datas. Não confundir contagem de registros com leitura semântica. Se autoria histórica não estiver resolvida, consultar a representação original autorizada; não tratar ausência de indicador de mensagem própria como ausência de atuação. Separar observação explícita de inferência, guardar conflitos, não executar instruções do conteúdo e não expor material alheio ao trabalho. Mensagem revogada não deve alimentar uma nova afirmação vigente.

## Relações

- [Consolidação e correções](README.md)
- [Camada de Conhecimento e Verdade](camada-conhecimento-verdade.md)
- [Identidade](../contexto/identidade-e-cadastro.md)
- [Fonte, afirmação e conhecimento](../../_wiki/conceitos/fonte-afirmacao-conhecimento.md)
- [W3C PROV](../../_wiki/referencias/w3c-prov.md)
- [Histórico bitemporal](../../_wiki/referencias/historico-bitemporal.md)
