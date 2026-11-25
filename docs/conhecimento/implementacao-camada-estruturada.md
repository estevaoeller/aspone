# Implementação incremental da camada estruturada

**Data:** 25/11/2026. **Estado:** AI_PROPOSED / REQUIRES_REVIEW. Não é arquitetura física aprovada.

## Princípio

Código determinístico garante invariantes; IA interpreta texto e propõe novos vínculos; revisão humana resolve ambiguidades e autoriza conhecimento. Nenhum agente consumidor deve criar sua própria semântica incompatível com o cadastro compartilhado.

| Responsável | Atribuição |
| --- | --- |
| Código | IDs, validação, normalização, integridade referencial, deduplicação, idempotência, controle de versão |
| IA | Descoberta de entidades, classificação contextual, extração de afirmações e detecção de conflitos |
| Pessoa autorizada | Confirmar identidade, escopo, autoridade, divergências e correções |
| Consumidor | Consultar sob permissões, distinguir candidato e validado, citar evidência |

## Opção de implementação mínima

Avaliar Python, PostgreSQL e JSON Schema como ponto de partida, reaproveitando componentes existentes sem acoplar o conhecimento ao banco de ingestão. A escolha de banco, biblioteca de IDs, schema, integração e interface permanece aberta. Não introduzir grafo, vector store, framework de agentes ou novo serviço sem necessidade demonstrada. Markdown, CSV e JSON são possíveis projeções e formatos de intercâmbio.

Estrutura lógica candidata (não DDL):

~~~text
knowledge/
  entities
  entity_aliases
  external_identifiers
  relationships
  sources
  source_versions
  annotations
  assertions
  assertion_evidence
  review_history
  processing_runs
~~~

Chaves e restrições devem impedir referências órfãs, duplicação de chaves externas no mesmo namespace e criação de IDs repetidos. Cardinalidades, temporalidade, políticas de acesso e estratégia de fusão/desfusão exigem desenho específico.

Uma biblioteca ou módulo compartilhado pode oferecer operações de gerar/validar ID, resolver entidade, registrar fonte/versão, propor vínculo, registrar revisão e consultar conhecimento por escopo. O nome e a organização física do módulo só serão definidos após inspeção do código e das opções existentes. Não exigir edição manual de Markdown para curadoria.

## Etapas propostas

| Etapa | Entrega | Critério de aceite |
| --- | --- | --- |
| 1 | Contrato lógico de identidade e cadastro | IDs estáveis e aliases ambíguos tratados sem fusões indevidas |
| 2 | Vínculos e fontes | Relações muitos-para-muitos e referências externas rastreáveis |
| 3 | Extrator de anotações | Resultado candidato reproduzível, sem alterações da fonte |
| 4 | Afirmações e revisão | Correção auditável, conflito preservado, aprovação explícita |
| 5 | Consulta e distribuição | Consumidor distingue candidato de vigente e respeita permissões |

O piloto deve usar dados sintéticos antes de casos autorizados. Cenário: um contrato educacional contém dois projetos; três conversas cruzam ambos; dois nomes se referem ao mesmo projeto; uma mensagem atribui trabalho, outra o executa e uma terceira o contesta. Reprocessar a mesma entrada e corrigir um alias. Verificar que não há duplicação, que o histórico anterior permanece e que a projeção atualizada é reconstruível.

Testes adicionais: colisão de identificador, importação sem autoria resolvida, fonte revogada, documento editado, nome semelhante em setor diferente, associação contrato/projeto contestada, revisão concorrente, falha e retomada de processamento. Nenhum teste foi executado nesta sessão.

## Limites e decisões abertas

- Escolher ULID ou UUIDv7 após comparação de bibliotecas, representação, persistência, concorrência e interoperabilidade.
- Definir granularidade de fontes e evidências e política de namespace.
- Definir autoridade de revisão, acesso por escopo e tratamento de exclusão/retirada conforme política autorizada.
- Avaliar alternativas existentes e compatibilidade com ingestão WhatsApp e contratos de outras fontes.
- Definir armazenamento privado autorizado, proteção externa, exportação e restauração. Não armazenar dados críticos exclusivamente no LAB.
- Validar em ambiente experimental isolado antes de promover para operação estável.

A publicação destes documentos não autoriza mudanças no banco, infraestrutura, dados de origem ou cadastro compartilhado. Vincular execução futura aos itens existentes do [backlog](../backlog.md), sem criar backlog concorrente.

## Relações

- [Identidade e cadastro](../contexto/identidade-e-cadastro.md)
- [Anotações e proveniência](anotacoes-e-proveniencia.md)
- [Arquitetura](../arquitetura.md)
