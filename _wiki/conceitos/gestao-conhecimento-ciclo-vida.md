---
type: Project Wiki
date_created: 20/11/2026
date_modified: 20/11/2026
related:
  - "[[camada-conhecimento-verdade]]"
  - "[[fonte-afirmacao-conhecimento]]"
  - "[[INDEX]]"
domain: ASPONE
client: A definir
engagement: A definir
organization: A definir
status: REQUIRES_REVIEW
---

# Gestão do conhecimento durante o ciclo de vida de um projeto

**Estado:** interpretação conceitual inicial (`REQUIRES_REVIEW`). Não descreve integração técnica implantada.

## 1. Gestão do conhecimento não é só pós-projeto

A expressão **gestão do conhecimento** (*knowledge management*, KM) abrange criação, aquisição, compartilhamento, organização, aplicação, retenção e evolução do conhecimento. Em projetos, essas atividades podem acontecer **antes, durante e depois** da execução.

A distinção relevante para o ASPONE não é “gestão do conhecimento agora ou depois”, mas **conhecimento operacional e decisório enquanto o projeto acontece** versus **conhecimento retrospectivo e reutilizável após entregas e encerramento**.

| Momento | Perguntas | Valor da memória |
| --- | --- | --- |
| Preparação | Qual contexto anterior? Quais regras e referências se aplicam? | Recuperar antecedentes |
| Execução cotidiana | O que aconteceu? Quem decidiu? Quais premissas e prazos valem? | Continuidade, coordenação e redução de perda de contexto |
| Entregas | O que foi efetivamente enviado, aprovado ou aceito? | Rastrear versões e estados distintos |
| Encerramento | Que resultados, justificativas e lições ficaram? | Consolidar trajetória e memória do projeto |
| Projetos futuros | Quais precedentes são úteis e em que contexto? | Reutilização contextual, sem copiar premissas sem avaliação |

O projeto ASPONE prioriza, nesta nova frente, o **acompanhamento vivo do conhecimento durante a execução**; deve, contudo, preservar condições para memória histórica e reutilização posterior.

## 2. Memória do projeto não se reduz à documentação final

Um relatório final não costuma conter todos os motivos de uma decisão, alternativas rejeitadas, responsáveis pela validação, circunstâncias de uma revisão, trocas de mensagens ou pendências que foram resolvidas. Uma memória viva pode ligar esse percurso a documentos e entregas, com acesso autorizado.

Exemplo fictício: a premissa de CAPEX foi alterada na reunião de 12/11, esclarecida no e-mail de 13/11 e incorporada à planilha V4 em 15/11. A memória operacional deve preservar essa sequência **antes** do relatório definitivo; depois, ela ajuda a compreender por que o resultado final difere de estimativas anteriores.

Isso não exige que cada ato vire um documento Markdown próprio. O acervo preserva fontes; a camada de conhecimento mantém relações, estados e fundamentos; os consumidores apresentam visões e consultas.

## 3. ASPONE e Knowledge Advisor: relação sem identidade

| Questão | ASPONE — camada de conhecimento | Knowledge Advisor |
| --- | --- | --- |
| Foco desta discussão | Estado vivo e história contextualizada dos projetos | Pesquisa de processos documentais, evidências, RAG, agentes e conhecimento institucional |
| Material de interesse | Comunicações, reuniões, decisões, premissas, tarefas, entregas e documentos | Versões documentais, relatórios, propostas, referências, insumos, normas e correções |
| Abrangência | Infraestrutura geral e independente de consumidores | Projeto especializado de pesquisa e experimentação institucional |
| Ponto de contato | Proveniência, afirmações, validação, histórico, autoridade e permissões | Os mesmos fundamentos podem ser reutilizados, respeitando os escopos |
| Estado de integração | **Não há integração comprovada ou contrato comum aprovado** | Propostas e experimentos, não plataforma homologada |

A documentação do Knowledge Advisor já trata de *Semantic Knowledge*, fontes e evidências, correções auditáveis e ciclo completo de elaboração e entrega. Portanto, chamá-lo apenas de “RAG para relatórios” seria simplificar demais seu escopo. Ver [README](https://github.com/FGV-Projetos-IA/knowledge-advisor) e [roadmap de referência](https://github.com/FGV-Projetos-IA/knowledge-advisor/blob/main/docs/arquitetura-roadmap-knowledge-worker.md) (acesso conforme permissões).

**Hipótese a explorar:** serviços e convenções de identidade, proveniência, vigência, correção e compartilhamento poderiam futuramente servir a diferentes aplicações. Isso **não** estabelece dependência, interoperabilidade atual ou decisão de arquitetura.

## 4. Duas memórias diferentes, mesmo nome parecido

A pasta `_wiki/` e o método Project Memory no repositório ASPONE registram o **desenvolvimento do software e de seus conceitos**. A futura Camada de Conhecimento e Verdade manteria o **conhecimento dos projetos que utilizarem o ASPONE**. A wiki de desenvolvimento não é, por si, esse produto.

Ver [Project Memory aplicada ao ASPONE](../solucoes/project-memory.md) e [definição da camada](../../docs/conhecimento/camada-conhecimento-verdade.md).

## 5. Questões abertas

- Que conhecimento é útil em tempo real e qual só deve ser consolidado no encerramento?
- Quando uma entrega passa de enviada a aceita?
- Como preservar contexto entre fases e equipes, sem transformar o sistema num controle indiscriminado de pessoas?
- Quais conceitos transversais poderão ser compartilhados com Knowledge Advisor, sem criar uma plataforma única antes de compreender as necessidades?

## Referências

- ASPONE: [definição da camada](../../docs/conhecimento/camada-conhecimento-verdade.md), [princípios](../../PROJECT.md).
- Knowledge Advisor: [README](https://github.com/FGV-Projetos-IA/knowledge-advisor) e [arquitetura de referência](https://github.com/FGV-Projetos-IA/knowledge-advisor/blob/main/docs/arquitetura-roadmap-knowledge-worker.md).
