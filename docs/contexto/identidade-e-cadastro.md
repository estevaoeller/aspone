# Identidade persistente e cadastro compartilhado

**Data:** 25/11/2026. **Estado:** REQUIRES_REVIEW. Proposta de contrato lógico, não implementação.

## Motivação

Uma mesma entidade pode aparecer em mensagens, atas, documentos e sistemas com nomes distintos. Uma conversa pode tratar de vários projetos; um projeto pode aparecer em várias conversas. A identidade compartilhada evita que cada agente reconstrua seu próprio cadastro. Ela não resolve sozinha a veracidade ou a autorização de acesso.

## Entidades e fronteiras

| Tipo | Prefixo candidato | Significado |
| --- | --- | --- |
| Organização | ORG | Instituição, cliente, contratante, parceiro |
| Contrato | CTR | Instrumento contratual, com número externo e emissor |
| Projeto | PRJ | Objeto de trabalho identificado |
| Pessoa | PES | Identidade, separada do papel |
| Equipe | EQP | Unidade coletiva de atuação |
| Participação | PAR | Vínculo pessoa, projeto, papel e vigência |
| Proposta comercial | PRP | Oportunidade, não necessariamente contrato |
| Responsabilidade | RSP | Atribuição de trabalho, não projeto |
| Atividade | ATV | Ocorrência ou ação |
| Reunião | REU | Ocorrência, distinta do evento de agenda |
| Documento | DOC | Objeto documental, distinto de versões |
| Conversa | CNV | Contexto de comunicação |
| Mensagem | MSG | Registro individual de comunicação |
| Fonte | SRC | Origem ou objeto de origem, conforme granularidade |
| Evidência | EVD | Referência delimitada que sustenta ou contraria uma afirmação |
| Anotação | ANN | Interpretação associada a uma fonte |
| Afirmação | AST | Proposição contextualizada e revisável |
| Relação | REL | Associação tipada entre entidades |
| Decisão | DEC | Escolha com autoridade e escopo |
| Revisão | REV | Evento de curadoria |
| Execução | RUN | Atividade de processamento |

Lista extensível, não enumeração definitiva. Contratos e projetos possuem identidade própria: um contrato pode abranger vários projetos; um projeto pode envolver mais de um instrumento ao longo do tempo. Relações possuem papéis e vigência. Setor, organização, rotina, assunto pontual e proposta não são automaticamente projetos.

## Identificadores

Requisitos estabelecidos na discussão: capacidade suficiente para pessoas, documentos, mensagens e evidências; ausência de limite artificial de quatro dígitos; estabilidade; geração reutilizável por código; independência de nomes, clientes, contratos e situação. O padrão exato permanece aberto.

| Alternativa | Avaliação |
| --- | --- |
| Sequencial curto | Simples, mas capacidade limitada e coordenação central |
| Base36 aleatório de 8 caracteres | 36^8 possibilidades; espaço não equivale a número seguro de gerações sem colisões |
| ULID | 128 bits, 26 caracteres Crockford Base32; 48 bits de tempo e 80 de aleatoriedade |
| UUIDv7 | 128 bits, padrão RFC 9562; timestamp de 48 bits, campos de versão e variante, 74 bits restantes para aleatoriedade ou estratégias permitidas |

**Hipótese preferencial:** ULID com representação externa tipada, por exemplo `PRJ-01ARZ3NDEKTSV4RRFFQ69G5FAV` (exemplo fictício). UUIDv7 deve ser comparado antes da escolha física, especialmente pelo tipo UUID nativo do PostgreSQL. Não confundir ordenação por geração com data do acontecimento; geração distribuída não garante ausência de colisões. Impor unicidade e tratamento de colisões. Não usar o identificador como segredo ou autorização. O prefixo deve ser validado contra o tipo; separar tipo e identificador no armazenamento é uma alternativa.

Referências de especificação para avaliação: [ULID](https://github.com/ulid/spec), [RFC 9562](https://www.rfc-editor.org/rfc/rfc9562.html). A seleção não foi homologada nem testada nesta sessão.

## Três formas de referência

- ID interno estável: usado em vínculos, nunca reciclado.
- Nome principal, slug e aliases: legíveis e alteráveis, com histórico; slug não é identidade.
- Identificador externo: namespace da fonte, conta/tenant quando necessário, tipo e chave original. Número de contrato isolado pode não ser único.

Exemplos fictícios: projeto Escola Alfa, contrato 99/2099, alias UEI Alfa, conversa Equipe Alfa. O alias é uma hipótese de correspondência; o grupo não é alias inequívoco do projeto.

## Resolução de entidades

~~~mermaid
flowchart LR
  S[Referencia encontrada] --> N[Normalizar e consultar]
  N --> M{Correspondencia segura?}
  M -->|Sim| L[Vincular ID existente]
  M -->|Incerta| R[Propor vinculo para revisao]
  M -->|Nenhuma| C[Candidato a nova entidade]
  R --> V[Revisao autorizada]
  C --> V
  V --> K[Cadastro compartilhado]
  K --> N
~~~

Normalizar para comparação sem destruir grafia original. Aliases possuem escopo, fonte, método e confirmação. Correspondência textual ambígua exige contexto: setor, município, contrato, organização, equipe, período. Não promover mera menção a participação. Registrar conflitos sem escolher silenciosamente. Fusões preservam IDs anteriores, referências e motivo; desfazer uma fusão deve ser possível. Identidade e deduplicação de conteúdo são problemas diferentes.

## Cadastro candidato de projetos

Campos mínimos: ID candidato, nome principal, aliases, organização de atuação, cliente/contratante e parceiros em papéis distintos, contrato, escopo, participação e papel, situação, evidências datadas, pessoas/conversas relacionadas, referências documentais, divergências, lacunas e revisão. Situação do projeto e situação da participação são distintas. Atividade recente da equipe não prova atuação pessoal; falta de mensagens não prova conclusão. Registrar informação explícita e inferência separadamente.

A saída do extrator deve distinguir projetos, rotinas/responsabilidades, propostas, candidatos insuficientes, perguntas e cobertura. Preservar o cadastro existente até revisão; não atribuir IDs canônicos automaticamente a cada hipótese extraída.

## Relações

- [Contexto compartilhado](README.md)
- [Camada de Conhecimento e Verdade](../conhecimento/camada-conhecimento-verdade.md)
- [Anotações e proveniência](../conhecimento/anotacoes-e-proveniencia.md)
- [Implementação incremental](../conhecimento/implementacao-camada-estruturada.md)
