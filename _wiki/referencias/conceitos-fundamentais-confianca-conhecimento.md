---
type: Project Wiki
date_created: 20/11/2026
date_modified: 20/11/2026
related:
  - "[[okf-open-knowledge-format]]"
  - "[[ai-memory]]"
domain: ASPONE
client: A definir
engagement: A definir
organization: A definir
status: REQUIRES_REVIEW
---

# Conceitos fundamentais para a confiança e evolução do conhecimento

> **Publicação no ASPONE:** referência conceitual em elaboração (`REQUIRES_REVIEW`), mantida na wiki pública de trabalho do projeto. Uma cópia para consulta existe na wiki privada do Homelab; as duas wikis não são sincronizadas automaticamente. A adoção de qualquer tecnologia ou padrão ainda depende de decisão específica.

> **Natureza:** referência conceitual transversal, em discussão. Destina-se a leitores, autores, agentes e projetos que precisem empregar os termos de forma consistente. Não representa adoção de tecnologia nem altera as definições do repositório institucional de glossário e ontologia.
>
> **Critério de redação:** adotar, quando já existem, os termos e distinções do [Glossário e Ontologia de IA da FGV Projetos](https://github.com/FGV-Projetos-IA/glossario-ontologia) e distinguir definições preexistentes de complementos analíticos propostos aqui.

## 1. Por que separar os conceitos?

Registrar o conhecimento de forma confiável exige responder a perguntas diferentes, que não devem ser comprimidas em um único atributo como "validado", "confiável" ou "atualizado":

1. **Origem:** de onde veio e como se formou? — [Proveniência](#2-proveniência).
2. **Exame:** o que foi efetivamente conferido, por quem e com qual conclusão? — [Verificação](#3-verificação).
3. **Tempo:** quando era verdade, quando foi conhecido e quando passou a ser considerado desatualizado? — [Validade temporal](#4-validade-temporal).
4. **Mudança:** o que aconteceu e como o entendimento evoluiu? — [Histórico](#5-histórico).
5. **Estado:** qual redação ou representação era utilizada em cada momento? — [Versionamento](#6-versionamento).
6. **Encadeamento:** como seguir relações entre origem, transformações, saídas e responsabilidades? — [Rastreabilidade](#7-rastreabilidade).
7. **Exame posterior:** existem critérios e registros suficientes para reconstituir e analisar o que ocorreu? — [Auditabilidade](#8-auditabilidade).

**Regra de interpretação:** nenhuma dessas propriedades, isoladamente, garante que o conteúdo seja verdadeiro, completo, autorizado, vigente ou adequado para determinado uso.

## 2. Proveniência

**Definição de referência:** informação sobre origem, derivação, uso, geração, responsáveis e contexto de um recurso ou resultado, que permite explicar sua formação. Corresponde ao conceito **K-37 (proveniência)** do glossário institucional.

**Pergunta:** *De onde veio esta informação e por quais etapas ela passou?*

- Inclui a identificação de fontes, versões, atividades de transformação, responsáveis, datas e contexto.
- Pode indicar que um trecho foi transcrito de reunião, extraído de documento ou calculado a partir de dados.
- Não demonstra, por si só, que a informação está correta.
- Não se confunde com **citação**, que aponta para uma fonte, nem com **linhagem** (K-38), que enfatiza a cadeia específica das transformações.

**Exemplo fictício:** a informação "o prazo é 15/12" foi registrada a partir da ata A, versão 2, aprovada após a reunião R, utilizando o trecho localizado na seção 3.

**Relações:** [Verificação](#3-verificação), [Rastreabilidade](#7-rastreabilidade), [Histórico](#5-histórico).

**Correspondência ontológica existente:** K-37 (proveniência), K-38 (linhagem), K-03 (fonte), R-03 (evidência). Consultar as [fichas C4.6](https://github.com/FGV-Projetos-IA/glossario-ontologia/blob/main/c4-completude/fichas_c4_6_rag_grounding_rastreabilidade_v0.1.md) e [fichas C4.1](https://github.com/FGV-Projetos-IA/glossario-ontologia/blob/main/c4-completude/fichas_c4_1_entidades_informacionais_autoridade_v0.1.md).

## 3. Verificação

**Definição de trabalho:** processo pelo qual uma pessoa ou mecanismo examina uma afirmação, registro ou resultado segundo critérios declarados e registra o escopo, a evidência examinada e a conclusão.

**Pergunta:** *O que foi examinado, como e por quem?*

- O resultado pode ser confirmação, ressalva, reprovação ou impossibilidade de concluir.
- A verificação precisa ter **objeto e escopo**: conferir uma data não valida automaticamente todos os fatos de um documento.
- **Verificação humana** é uma modalidade com conceito correspondente no glossário (**G-20 — validação humana**): pessoa competente examina e registra conclusão, ressalva ou rejeição com critérios definidos.
- A palavra *verificação* tem uso mais amplo que *validação humana*. Não tratar os dois termos como sinônimos perfeitos.
- Uma marca de verificação declarada não substitui evidências, identidade verificável, competência e critérios apropriados.
- Verificação factual também não equivale a autorização de acesso nem à homologação institucional.

**Exemplo fictício:** em 16/11, uma pessoa verifica apenas a data da entrega na ata aprovada e registra "confirmada com base na seção 3". Isso não confere automaticamente orçamento, escopo nem responsabilidades.

**Relações:** [Proveniência](#2-proveniência), [Validade temporal](#4-validade-temporal), [Auditabilidade](#8-auditabilidade).

**Correspondência ontológica:** G-20 (validação humana) e Q-01 (avaliação) são conceitos correlatos já definidos, **não equivalentes integrais** da noção ampla de verificação empregada neste artigo. Ver [fichas C6.4](https://github.com/FGV-Projetos-IA/glossario-ontologia/blob/main/c6-abertura/fichas_c6_4_supervisao_decisao_humana_v0.1.md).

## 4. Validade temporal

**Definição de trabalho:** qualificação do período ou instante no qual uma afirmação, situação, regra ou decisão é aplicável ao mundo descrito, distinguindo-o das datas em que a informação foi registrada, modificada, examinada ou sinalizada para revisão.

**Pergunta:** *A partir de quando, até quando e em qual contexto a informação é válida?*

É necessário distinguir, ao menos quando forem relevantes:

| Dimensão temporal | Pergunta |
| --- | --- |
| **Tempo do fato / evento** | Quando o acontecimento ocorreu? |
| **Tempo de vigência ou validade no mundo** (*valid time*) | Em qual intervalo a situação descrita é aplicável? |
| **Tempo de registro no sistema** (*transaction/system time*) | Quando o sistema passou a armazenar determinada afirmação? |
| **Tempo de verificação** | Quando e em que condições o conteúdo foi examinado? |
| **Prazo de revisão / sinal de desatualização** | Quando será necessário reavaliar o conteúdo? |

O tempo de validade e o tempo de registro podem ser diferentes: uma decisão com efeito retroativo pode ser registrada apenas depois. Em sistemas temporais, a coexistência das duas dimensões costuma ser chamada de **bitemporalidade**.

**Exemplo fictício:** em 18/11, o sistema registra que uma decisão tomada em 12/11 alterou o prazo com efeito desde 12/11. A data do registro (18/11) não altera a data de vigência (12/11).

**Não confundir:** uma informação **antiga** não é necessariamente **inválida**; uma informação **recente** não é necessariamente **vigente**. Da mesma forma, a ausência de data final não prova validade indefinida. O campo `stale_after` do OKF é um alerta de desatualização/revisão, **não uma representação completa do intervalo de validade da afirmação**.

**Correspondência ontológica:** não se identificou, nos índices e fichas consultados do repositório FGV, um conceito único que corresponda integralmente a "validade temporal" nessa acepção. **Mapeamento pendente de revisão**, sem criar um novo ID. Base técnica externa: [IBM — modelagem de dados temporais](https://www.ibm.com/docs/en/data-studio/4.1.1?topic=models-modeling-temporal-data) e [W3C — OWL-Time](https://www.w3.org/TR/owl-time/).

**Relações:** [Histórico](#5-histórico), [Versionamento](#6-versionamento), [Verificação](#3-verificação).

## 5. Histórico

**Definição de trabalho:** sequência preservada e contextualizada de eventos, estados, decisões e alterações relacionados a um objeto de conhecimento, que permite reconstruir sua evolução.

**Pergunta:** *O que aconteceu, em qual ordem e como isso afetou o conhecimento disponível?*

O histórico pode incluir eventos como recebimento de documento, registro de hipótese, mudança de entendimento, correção, verificação, aprovação e revogação.

Deve ser possível distinguir:

- **O acontecimento original** (uma reunião, por exemplo).
- **O registro do acontecimento** (uma ata, transcrição ou nota).
- **A interpretação sobre ele** (uma síntese ou uma decisão inferida).
- **A alteração no conhecimento mantido** (nova versão ou correção).

O histórico não é necessariamente uma sucessão de arquivos: existem acontecimentos relevantes que não mudam a redação de uma página. Por outro lado, uma alteração textual pode ocorrer sem que o fato descrito tenha mudado.

**Exemplo fictício:** reunião discute prazo; ata formaliza alteração; sistema incorpora nova informação; pessoa corrige a interpretação do escopo. Esses são eventos diferentes e não devem ser fundidos num único "documento atualizado".

**Não confundir:** histórico de acontecimentos, histórico de versões, registro de execução (*log*) e trilha de auditoria são objetos relacionados, mas diferentes. Nem todo histórico é íntegro, completo ou suficiente para auditoria.

**Correspondência ontológica:** conceitos relacionados incluem Q-30 (versionamento), Q-26 (registro de eventos), R-13 (trilha de auditoria) e R-06 (decisão), sem correspondência 1:1 automática ao termo genérico *histórico*. Mapeamento a revisar.

**Relações:** [Versionamento](#6-versionamento), [Validade temporal](#4-validade-temporal), [Auditabilidade](#8-auditabilidade).

## 6. Versionamento

**Definição de referência:** identificação e gestão de estados sucessivos de objetos, com registro de mudanças e dependências. Corresponde a **Q-30 (versionamento)** no glossário institucional.

**Pergunta:** *Qual estado ou versão do objeto estava sendo utilizado?*

- Uma versão identifica uma representação determinada, não apenas a hora em que o arquivo foi salvo.
- Versões permitem comparar o conteúdo anterior e posterior a uma alteração.
- Versionamento de conteúdo não preserva automaticamente todas as razões, responsáveis e evidências que motivaram a mudança.
- Um commit Git pode dar uma parte importante do histórico, mas não é, sozinho, comprovação de verificação humana ou vigência temporal.

**Exemplo fictício:** a versão 1 do registro informava "entrega do projeto", enquanto a versão 2 corrige para "entrega do relatório preliminar". O conteúdo anterior permanece identificável e ligado ao motivo da correção.

**Correspondência ontológica existente:** Q-30; consultar [fichas C6.10](https://github.com/FGV-Projetos-IA/glossario-ontologia/blob/main/c6-abertura/fichas_c6_10_operacao_observabilidade_melhoria_v0.1.md).

**Relações:** [Histórico](#5-histórico), [Rastreabilidade](#7-rastreabilidade).

## 7. Rastreabilidade

**Definição de referência:** capacidade de seguir e relacionar origem, versões, transformações, dependências, ações e responsáveis associados a dado, artefato, decisão ou execução. Corresponde a **G-30 (rastreabilidade)** no glossário institucional.

**Pergunta:** *Consigo seguir o percurso entre informação, fonte, processamento, versão e decisão?*

**Exemplo fictício:** recuperar a afirmação exibida em um painel e, a partir dela, localizar a versão do conhecimento, a extração, o trecho da ata e a revisão humana correspondente.

**Não confundir:** ter proveniência registrada não significa que todos os elos necessários estejam navegáveis ou íntegros. Rastreabilidade também não é sinônimo de auditoria concluída.

**Correspondência ontológica existente:** G-30; ver [fichas C6.6](https://github.com/FGV-Projetos-IA/glossario-ontologia/blob/main/c6-abertura/fichas_c6_6_transparencia_auditabilidade_risco_v0.1.md).

**Relações:** [Proveniência](#2-proveniência), [Versionamento](#6-versionamento), [Auditabilidade](#8-auditabilidade).

## 8. Auditabilidade

**Definição de referência:** capacidade de um sistema ou processo ser examinado posteriormente por parte autorizada com base em critérios, registros e evidências suficientes para reconstruir decisões relevantes e avaliar sua conformidade, desempenho e controles. Corresponde a **G-29 (auditabilidade)** no glossário institucional.

**Pergunta:** *Outra pessoa autorizada consegue compreender e examinar o ocorrido com evidências suficientes?*

A trilha de auditoria (**R-13**) é um conjunto correlacionado de registros, evidências, versões, proveniência e decisões. A trilha **apoia** a auditabilidade, mas não é a própria capacidade de auditoria e não se confunde com um log isolado.

**Exemplo fictício:** identificar a fonte que embasou uma alteração de prazo, quem sugeriu a correção, quem a validou, quando foi registrada e quais versões foram afetadas.

**Não confundir:** a existência de registros não comprova, por si, sua integridade, completude, legitimidade ou adequação às exigências de privacidade.

**Correspondência ontológica existente:** G-29 e R-13; consultar [fichas C6.6](https://github.com/FGV-Projetos-IA/glossario-ontologia/blob/main/c6-abertura/fichas_c6_6_transparencia_auditabilidade_risco_v0.1.md) e [fichas C7.1](https://github.com/FGV-Projetos-IA/glossario-ontologia/blob/main/c7-ontologia/fichas_c7_1_resultados_evidencias_artefatos_v0.1.md).

**Relações:** [Histórico](#5-histórico), [Verificação](#3-verificação), [Rastreabilidade](#7-rastreabilidade).

## 9. Exemplo integrado: uma alteração de prazo

**Cenário inteiramente fictício.**

| Data | Acontecimento e registro | Conceito principal |
| --- | --- | --- |
| 10/11 | E-mail estabelece entrega em 30/11. | Fonte, proveniência, histórico |
| 12/11 | Reunião decide alterar o prazo para 15/12, com efeito desde esse dia. | Evento, validade temporal |
| 14/11 | Ata aprovada formaliza a mudança. | Evidência, verificação do registro |
| 18/11 | Sistema incorpora a informação e gera nova versão de síntese. | Tempo de registro, versionamento |
| 19/11 | Especialista esclarece que a alteração se refere apenas ao relatório preliminar. | Correção, verificação, histórico |
| 19/11 | Registro mantém a versão anterior, motivo e referência à correção. | Rastreabilidade, auditabilidade |

Esse exemplo evidencia por que é insuficiente guardar apenas a frase "prazo: 15/12" ou marcar uma página como "atualizada". A frase precisa permanecer relacionada ao seu escopo, às fontes e à sequência dos acontecimentos.

## 10. Mapa para o glossário e a ontologia

**Consulta realizada em 20/11/2026** ao repositório [FGV-Projetos-IA/glossario-ontologia](https://github.com/FGV-Projetos-IA/glossario-ontologia), principalmente à Lista Mestra, às fichas dos ciclos C4, C6 e C7 e aos respectivos índices. O repositório identifica-se como fonte canônica **para o trabalho institucional da FGV Projetos**, não automaticamente para os demais projetos. As fichas institucionais são externas ao ASPONE e seu acesso pode depender das permissões de quem as consulta; as definições fundamentais deste artigo permanecem legíveis independentemente desses links.

| Termo neste artigo | ID relacionado | Natureza da correspondência |
| --- | --- | --- |
| Proveniência | **K-37** | Correspondência direta |
| Fonte | **K-03** | Conceito relacionado |
| Evidência | **R-03** | Conceito distinto e relacionado |
| Linhagem | **K-38** | Especialização de proveniência |
| Verificação (sentido amplo) | **G-20**, Q-01 | Aproximações parciais; **não** equiparar à validação humana |
| Validade temporal | — | Correspondência específica **pendente** |
| Histórico | Q-26, **Q-30**, R-13 | Conceitos relacionados; **não** equivalentes |
| Versionamento | **Q-30** | Correspondência direta |
| Rastreabilidade | **G-30** | Correspondência direta |
| Auditabilidade | **G-29** | Correspondência direta |
| Trilha de auditoria | **R-13** | Conceito distinto e relacionado |
| Feedback humano | Q-33 | Possível origem de correção, não correção já validada |

As **fichas e IDs do repositório prevalecem para definições institucionais ali já estabelecidas**. Este artigo explicita suas relações e acrescenta distinções analíticas onde ainda não se localizou equivalência direta. Nenhum ID foi criado ou alterado no repositório.

### Regras de uso terminológico propostas

1. Preferir o **termo em português** e o **ID estável** quando houver correspondência estabelecida.
2. Registrar separadamente **fonte**, **evidência**, **afirmação**, **verificação** e **decisão**.
3. Não tratar **verificado**, **vigente**, **autorizado** e **homologado** como sinônimos.
4. Diferenciar o **tempo do fato**, a **vigência** e o **tempo de registro** sempre que essa diferença puder alterar a interpretação.
5. Não substituir **histórico de acontecimentos** por **histórico de arquivos** sem justificativa.
6. Registrar quando uma relação é **confirmada no glossário**, **analogia** ou **conceito pendente de harmonização**.
7. Se uma definição for revista, atualizar esta referência e os links dependentes, registrando a razão, a data e as fontes; não reescrever silenciosamente o significado anterior.

## 11. Relação com OKF e outros padrões

O [artigo teórico sobre Open Knowledge Format (OKF)](okf-open-knowledge-format.md) explica o formato; este artigo explica as **distinções conceituais** usadas para interpretá-lo:

| Aspecto | OKF v0.2 | Limite interpretativo |
| --- | --- | --- |
| Proveniência | `sources` | Fontes declaradas não garantem veracidade |
| Autoria/geração | `generated` | Gerar não é verificar |
| Verificação | `verified` | Registro declarativo, não prova completa de conformidade |
| Ciclo de vida | `status`, `stale_after` | Desatualização não equivale a intervalo de validade no mundo |
| Histórico | `log.md` opcional, arquivos versionáveis | Não exige registro completo de todos os acontecimentos nem trilha de auditoria |
| Versões | Arquivos podem ser versionados externamente | Git é opcional; não resolve sozinho auditoria factual |

O **W3C PROV-O** permite representar relações explícitas entre **entidades**, **atividades** e **agentes** na proveniência. O **W3C OWL-Time** dispõe de uma ontologia para instantes, intervalos e relações temporais. Os padrões auxiliam a modelagem, mas sua utilização concreta não está sendo decidida neste artigo.

### Estudos específicos vinculados

- [W3C PROV — modelo padronizado de proveniência](w3c-prov.md): entidades, atividades, agentes, relações de derivação e limites da consistência PROV.
- [Histórico bitemporal](historico-bitemporal.md): tempo de validade e tempo de registro; diferenças entre o que se sabia e o que passou a ser conhecido.
- [Fonte, afirmação, evidência e validação](../conceitos/fonte-afirmacao-conhecimento.md): como os conceitos podem ser aplicados ao conhecimento dos projetos.
- [Camada de Conhecimento e Verdade](../../docs/conhecimento/camada-conhecimento-verdade.md): aplicação integrada ao ASPONE.

## 12. Situação e questões em aberto

**Situação deste texto:** referência proposta, consistente com as definições consultadas, aguardando eventual revisão conceitual conjunta. **Não houve alteração no repositório de glossário e ontologia.**

Questões para harmonização futura:

- Se "verificação" no sentido geral merece uma ficha própria, sem conflitar com G-20 (validação humana) e Q-01 (avaliação).
- Se "validade temporal" deve ser conceituada como termo transversal (e como distinguir validade de atualidade e expiração).
- Como nomear, separadamente, histórico de eventos, histórico de conhecimento, histórico de versões e trilha de auditoria.
- Se convém uma representação explícita de correção, supersessão, revogação e contradição entre afirmações, sem perder referências às fontes originais.

Essas são **pendências de modelagem conceitual**, não tarefas de implantação já aprovadas.

## Referências

1. [Glossário e Ontologia de IA da FGV Projetos — README](https://github.com/FGV-Projetos-IA/glossario-ontologia/blob/main/README.md), [Lista Mestra](https://github.com/FGV-Projetos-IA/glossario-ontologia/blob/main/c5-abertura/lista_mestra_termos_ia_fgv_projetos_v0.1.md) e [Padrão da Ficha Conceitual](https://github.com/FGV-Projetos-IA/glossario-ontologia/blob/main/padrao_ficha_conceitual_ia_fgv_projetos_v0.1.md).
2. [Fichas C4.6 — proveniência e linhagem](https://github.com/FGV-Projetos-IA/glossario-ontologia/blob/main/c4-completude/fichas_c4_6_rag_grounding_rastreabilidade_v0.1.md).
3. [Fichas C6.4 — validação humana](https://github.com/FGV-Projetos-IA/glossario-ontologia/blob/main/c6-abertura/fichas_c6_4_supervisao_decisao_humana_v0.1.md).
4. [Fichas C6.6 — auditabilidade e rastreabilidade](https://github.com/FGV-Projetos-IA/glossario-ontologia/blob/main/c6-abertura/fichas_c6_6_transparencia_auditabilidade_risco_v0.1.md).
5. [Fichas C6.10 — versionamento](https://github.com/FGV-Projetos-IA/glossario-ontologia/blob/main/c6-abertura/fichas_c6_10_operacao_observabilidade_melhoria_v0.1.md).
6. [Fichas C7.1 — evidência e trilha de auditoria](https://github.com/FGV-Projetos-IA/glossario-ontologia/blob/main/c7-ontologia/fichas_c7_1_resultados_evidencias_artefatos_v0.1.md).
7. [W3C — PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/).
8. [W3C — Time Ontology in OWL](https://www.w3.org/TR/owl-time/).
9. [IBM — Modeling temporal data](https://www.ibm.com/docs/en/data-studio/4.1.1?topic=models-modeling-temporal-data).
10. [GoogleCloudPlatform — Open Knowledge Format v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md).

**Última revisão documental:** 20/11/2026.