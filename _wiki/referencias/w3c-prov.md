---
type: Project Wiki
date_created: 20/11/2026
date_modified: 20/11/2026
related:
  - "[[conceitos-fundamentais-confianca-conhecimento]]"
  - "[[fonte-afirmacao-conhecimento]]"
  - "[[historico-bitemporal]]"
domain: ASPONE
client: A definir
engagement: A definir
organization: A definir
status: REQUIRES_REVIEW
---

# W3C PROV — modelo padronizado de proveniência

**Natureza:** estudo de padrão existente; **não** decisão de adotar PROV-O, RDF, grafo ou qualquer tecnologia. **Estado do artigo:** `REQUIRES_REVIEW`.

## 1. Que problema resolve?

Proveniência é a informação sobre **como um recurso foi produzido, utilizado, derivado e associado a responsáveis**. Em sistemas com muitos documentos, mensagens, extrações e intervenções humanas, é insuficiente preservar apenas “fonte: arquivo X”. Queremos reconstruir a cadeia: fonte original → atividade de extração → informação derivada → revisão → conhecimento apresentado.

O **W3C PROV** é uma família de especificações do World Wide Web Consortium (W3C) para representar e intercambiar descrições de proveniência. Seu modelo central é o **PROV-DM**; a família inclui uma ontologia (PROV-O), uma notação (PROV-N), restrições de consistência e materiais introdutórios.

Essa família não é uma tecnologia de armazenamento ou um sistema de gestão de conhecimento pronto.

## 2. Três conceitos centrais

| Conceito PROV | Significado | Exemplo no ASPONE |
| --- | --- | --- |
| **Entity — entidade** | Coisa física, digital ou conceitual da qual se acompanha a proveniência | Mensagem original, ata V2, trecho extraído, síntese gerada |
| **Activity — atividade** | Processo ou operação que utiliza e/ou produz entidades | Coleta, transcrição, extração, revisão humana, geração de síntese |
| **Agent — agente** | Pessoa, organização ou software responsável ou envolvido | Autor de documento, revisor autorizado, serviço de extração |

Relações relevantes do vocabulário: **used** (atividade usou entidade); **wasGeneratedBy** (entidade gerada por atividade); **wasDerivedFrom** (derivada de outra entidade); **wasAssociatedWith** (atividade associada a agente); **wasAttributedTo** (entidade atribuída a agente). O modelo permite ainda qualificar relações e atribuições.

Não é preciso, nesta etapa, decidir que todos esses conceitos se tornem tabelas ou nós físicos.

## 3. Exemplo aplicado ao ASPONE

*Cenário fictício: uma ata de reunião embasa uma afirmação sobre o prazo de entrega.*

~~~mermaid
flowchart LR
    M["Ata V2<br/>(entidade)"] -->|usada por| EX["Extração<br/>(atividade)"]
    EX -->|gera| A["Afirmação extraída<br/>(entidade)"]
    A -->|usada por| RV["Revisão<br/>(atividade)"]
    P["Revisor autorizado<br/>(agente)"] -. associado a .-> RV
    RV -->|gera| C["Registro revisado<br/>(entidade)"]
~~~

O valor do modelo é permitir que alguém que encontra “prazo: 15/12” possa seguir a proveniência até o **registro revisado**, a atividade que o gerou, o responsável e a **ata original**.

O padrão também permite descrever a proveniência de uma descrição de proveniência (por exemplo, *bundles*). Isso pode ser relevante para histórico de revisões, sem substituir o procedimento de auditoria do ASPONE.

## 4. O que traz de interessante para a camada de conhecimento

- **Vocabulário compartilhado:** evita inventar termos incompatíveis para origem, atividade, responsabilidade e derivação.
- **Separação de papéis:** a mensagem original, a operação da IA e a revisão humana não viram um único objeto indiferenciado.
- **Rastreabilidade entre fontes:** permite expressar cadeias quando uma conclusão reúne várias fontes.
- **Interoperabilidade conceitual:** outras ferramentas podem interpretar relações de proveniência sem conhecer a aplicação que produziu a informação.
- **Base para avaliações:** a proveniência permite investigar confiabilidade, origem e responsabilidade, quando há evidências e regras de avaliação adicionais.

O interesse inicial no ASPONE é **estudar o modelo conceitual** e mapear correspondências com os registros já existentes, antes de escolher uma serialização.

## 5. O que o PROV não resolve

1. **Não declara que a afirmação é verdadeira.** Diz como foi produzida e a que está relacionada.
2. **Não confere autoridade automaticamente.** Registrar um agente não é provar competência para aprovar uma decisão.
3. **Não determina vigência de uma premissa.** Para isso, precisamos de modelagem temporal apropriada.
4. **Não implementa controle de acesso, preservação de originais ou auditoria completa**, embora ajude a descrever processos e rastros.
5. **Não produz a extração nem resolve conflitos:** essas atividades exigem processos, regras e validações adicionais.

A especificação **PROV-CONSTRAINTS** trata de consistência de representações de proveniência; uma instância consistente não é certificado de veracidade factual.

## 6. Aplicação potencial no ASPONE — sem adoção antecipada

Investigar se o fluxo já existente de WhatsApp pode ser descrito com a cadeia conceitual: mensagem → coleta → projeção MD → extração de afirmação → revisão → conhecimento apresentado. Testar se é possível reconstruir os elos e identificar alterações humanas. Somente depois avaliar requisitos de formalização, formatos e ferramentas.

**Pontos abertos:** identidade estável dos recursos; granularidade da fonte (arquivo/trecho/mensagem); representação de múltiplas evidências; proveniência de correções; autoria e permissões. Ver [fonte, afirmação e conhecimento](../conceitos/fonte-afirmacao-conhecimento.md) e [definição da camada](../../docs/conhecimento/camada-conhecimento-verdade.md).

## 7. Referências primárias — W3C

1. **[PROV-Overview](https://www.w3.org/TR/prov-overview/)** — mapa oficial da família de especificações; *W3C Working Group Note*, 30/04/2013.
2. **[PROV Model Primer](https://www.w3.org/TR/prov-primer/)** — introdução didática a agentes, entidades, atividades e relações; *W3C Working Group Note*, 30/04/2013.
3. **[PROV-DM: The PROV Data Model](https://www.w3.org/TR/prov-dm/)** — modelo de dados conceitual; *W3C Recommendation*, 30/04/2013.
4. **[PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/)** — representação ontológica dos conceitos PROV; *W3C Recommendation*, 30/04/2013.
5. **[Constraints of the PROV Data Model](https://www.w3.org/TR/prov-constraints/)** — regras de consistência aplicáveis a descrições PROV; *W3C Recommendation*, 30/04/2013.

**Recomendação de leitura:** começar por *Primer*, depois *Overview* e *PROV-DM*. Não confundir o modelo conceitual PROV-DM com a decisão, ainda aberta, de usar PROV-O como ontologia técnica.
