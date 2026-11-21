---
type: Project Wiki
date_created: 20/11/2026
date_modified: 20/11/2026
related:
  - "[[conceitos-fundamentais-confianca-conhecimento]]"
  - "[[ai-memory]]"
domain: ASPONE
client: A definir
engagement: A definir
organization: A definir
status: REQUIRES_REVIEW
---

# Open Knowledge Format (OKF): fundamentos, estrutura e semântica

> **Publicação no ASPONE:** referência conceitual em elaboração (`REQUIRES_REVIEW`), mantida na wiki pública de trabalho do projeto. Uma cópia para consulta existe na wiki privada do Homelab; as duas wikis não são sincronizadas automaticamente. A adoção de qualquer tecnologia ou padrão ainda depende de decisão específica.

> **Natureza do documento:** artigo de referência conceitual. Descreve o Open Knowledge Format a partir de sua especificação pública v0.2 e distingue essa especificação da implementação oferecida pelo projeto AI Memory. **Não constitui decisão de adotar OKF em qualquer sistema.**
>
> **Base consultada:** especificação OKF v0.2 no repositório GoogleCloudPlatform/knowledge-catalog e documentação de conformidade do ai-memory 2.0, consultadas em 20/11/2026.

## 1. Introdução: o problema que o formato procura resolver

Sistemas informatizados armazenam documentos e dados em grande escala, mas ter acesso a arquivos não equivale a dispor de conhecimento organizado. Um documento pode registrar uma definição, uma decisão ou uma instrução; para utilizá-lo de modo confiável, é necessário também saber o que ele representa, de onde veio, quem o produziu, quais outras informações lhe dão suporte e se ainda está vigente.

O problema torna-se mais relevante quando agentes de inteligência artificial produzem, consultam e atualizam conhecimento. Sem convenções compartilhadas, cada sistema tende a adotar estruturas próprias, dificultando a leitura humana, a transferência entre ferramentas e a interpretação da origem e da validade das afirmações.

O **Open Knowledge Format (OKF)** é uma especificação aberta destinada a representar unidades de conhecimento em arquivos legíveis por pessoas e processáveis por software. Sua proposta é padronizar um conjunto mínimo de convenções estruturais e semânticas, mantendo liberdade para organizar os conteúdos e escolher as ferramentas que os utilizarão.

A especificação aqui estudada é a **versão 0.2**, publicada no projeto [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md). A existência de uma especificação pública não deve ser confundida com homologação por organismo formal de normalização nem com adoção universal pelo mercado.

## 2. A ideia fundamental: conhecimento como documento autocontido

O OKF parte de uma representação simples: **um conceito é um arquivo Markdown com metadados YAML no início**. Um conjunto organizado de conceitos forma um *knowledge bundle* (pacote de conhecimento).

Essa escolha combina quatro propriedades:

1. **Legibilidade:** o conteúdo permanece inteligível sem um aplicativo especializado.
2. **Estruturação:** metadados podem ser lidos por programas e agentes.
3. **Portabilidade:** os arquivos podem ser copiados, distribuídos e interpretados por diferentes ferramentas.
4. **Comparabilidade histórica:** alterações em arquivos de texto podem ser comparadas por ferramentas de versionamento.

O formato não pretende substituir bancos de dados, mecanismos de busca, sistemas de RAG ou ontologias formais. Ele define uma **forma intercambiável de representar conhecimento**, sem impor arquitetura de armazenamento, mecanismo de execução ou infraestrutura de consulta.

### 2.1. Dados, documentos e conhecimento

Para compreender o propósito do OKF, convém distinguir:

- **Dado:** registro de um valor, evento ou atributo.
- **Documento:** suporte que reúne e apresenta informações, possivelmente acompanhado de contexto.
- **Conhecimento representado:** uma unidade de informação interpretável, acompanhada de definição, relações, proveniência e, quando disponíveis, sinais de verificação e atualidade.

Essa distinção é analítica; não significa que o OKF transforme automaticamente dados em conhecimento validado. A qualidade da interpretação e a evidência continuam dependendo dos processos que produziram o conteúdo.

## 3. Conceitos e terminologia

| Termo | Significado na especificação |
| --- | --- |
| **Bundle** | Diretório hierárquico de documentos de conhecimento; unidade de distribuição. |
| **Concept** | Unidade de conhecimento representada em um arquivo Markdown. |
| **Concept ID** | Caminho do arquivo dentro do bundle, sem a extensão `.md`. |
| **Frontmatter** | Bloco YAML delimitado por `---` no início do arquivo. |
| **Body** | Conteúdo Markdown localizado depois do frontmatter. |
| **Source** | Material do qual um conceito deriva, identificado em `sources`. |
| **Provenance** | Conjunto de fontes que sustentam a formação do conceito. |
| **Actor** | Identificador de pessoa, agente ou processo que produziu/verificou algo. |
| **Trust tier** | Nível indicativo de verificação derivado do campo `verified`. |
| **Attested Computation** | Conceito que descreve uma computação autorizada e os meios de atestar sua execução. |

A unidade primária é o **conceito documentado**, e não uma linha de banco de dados, um vetor de embedding ou uma mensagem de chat.

## 4. Estrutura de um pacote de conhecimento

Um bundle é uma árvore de diretórios contendo arquivos `.md`. Pode ser distribuído como repositório Git, arquivo compactado ou subdiretório de outro repositório.

```text
pacote/
├── index.md
├── log.md
├── conceitos/
│   ├── index.md
│   ├── indicador.md
│   └── processo.md
└── procedimentos/
    └── procedimento-a.md
```

Os nomes `index.md` e `log.md` são reservados para funções próprias:

- **`index.md`:** apresenta o conteúdo do diretório e favorece descoberta progressiva, isto é, consultar primeiro o índice e depois os documentos pertinentes.
- **`log.md`:** registra alterações em ordem cronológica, quando utilizado.

Na especificação OKF v0.2, esses arquivos são **opcionais**. O índice raiz pode declarar `okf_version: "0.2"` em seu frontmatter. Não se deve confundir essa possibilidade com exigências adicionais de uma implementação específica.

A hierarquia oferece organização, enquanto os links entre documentos permitem relações transversais que não dependem apenas da posição nas pastas.

## 5. Composição de um documento OKF

Um conceito contém duas partes: metadados estruturados e corpo em Markdown.

### 5.1. Campos gerais

| Campo | Função | Obrigatoriedade |
| --- | --- | --- |
| `type` | Identifica o tipo de conceito. | **Obrigatório** |
| `title` | Nome de apresentação. | Opcional, recomendado |
| `description` | Resumo em uma frase. | Opcional, recomendado |
| `resource` | URI do objeto ou recurso descrito, quando existir. | Opcional |
| `tags` | Termos de classificação transversal. | Opcional |

O campo `type` é o **único campo universalmente obrigatório** para um documento de conceito conformante. Seu vocabulário não é fechado: produtores podem criar tipos explicativos, e leitores devem tolerar tipos desconhecidos.

As seções do corpo são livres. Títulos, listas, tabelas, exemplos e blocos de código são recomendáveis quando melhoram a interpretação. Cabe ao produtor decidir a granularidade do conceito: o formato não fornece, por si só, uma regra de decomposição do conhecimento.

### 5.2. Exemplo didático fictício

O trecho seguinte ilustra a estrutura e não registra um acontecimento real:

```markdown
---
type: Decision
title: Prazo de entrega de um relatório
description: Registro de uma decisão de cronograma em um projeto fictício.
tags: [cronograma, entrega]
status: draft
generated:
  by: process:exemplo-didatico
  at: 2026-01-15T12:00:00Z
sources:
  - id: ata-reuniao-01
    resource: https://example.org/documentos/ata-01
    title: Ata de reunião fictícia
---

# Decisão

O prazo do relatório foi alterado para 15 de dezembro,
conforme a ata da reunião.[^ata-reuniao-01]

[^ata-reuniao-01]: Ata de reunião fictícia
```

Nesse exemplo, o conteúdo de interesse está no corpo. Já os metadados informam natureza, classificação, responsável pela geração e fonte declarada. **A presença de uma fonte não demonstra, sozinha, que a afirmação foi conferida.**

## 6. Proveniência: de onde veio o conhecimento?

A proveniência responde à pergunta: **quais materiais deram origem a este conceito?** O campo `sources` contém uma lista de referências, internas ou externas ao bundle.

Cada fonte declara obrigatoriamente `resource` dentro da sua entrada. Pode apresentar adicionalmente:

- `id`: chave estável para vincular afirmações à fonte;
- `title`: identificação legível;
- `author`: quem produziu o material;
- `last_modified`: data de alteração da fonte;
- `usage_count` e `usage_window`: sinais de utilização em determinado intervalo.

A especificação distingue **fontes e sinais de credibilidade** de um julgamento conclusivo de confiabilidade. Contagem de acessos, autoria e data de atualização não substituem análise crítica.

### 6.1. Atribuição de afirmações específicas

O OKF v0.2 propõe associar notas de rodapé Markdown aos identificadores `sources[].id`. Uma afirmação pode citar `[^fonte-1]`, que remete à fonte `id: fonte-1` no frontmatter.

A escolha de identificadores estáveis evita que a reorganização da lista de fontes mude silenciosamente o significado de uma citação.

Essa convenção permite **atribuição por afirmação**, mas não exige que toda frase esteja citada. Também não impõe hashes, cópias imutáveis, coordenadas de página, trechos preservados ou validação automática do conteúdo. Essas são preocupações adicionais de sistemas de rastreabilidade documental.

## 7. Autoria, verificação e confiança

O OKF separa a **produção do conhecimento** da **verificação do conteúdo**:

- `generated.by` identifica quem ou o que produziu a versão atual;
- `generated.at` informa quando ocorreu a última alteração significativa;
- `verified` registra uma ou várias verificações, cada uma com `by` e `at`.

A convenção de atores utiliza identificadores como `human:identificador`, `process:identificador` ou `agente/versao`.

Da existência e do tipo de `verified`, um consumidor pode derivar três categorias:

| Categoria | Interpretação |
| --- | --- |
| **Unverified** | Não há verificação registrada. |
| **Machine-confirmed** | Há verificação por processo ou agente, sem verificação humana. |
| **Human-reviewed** | Há ao menos uma verificação identificada como humana. |

Esses níveis são **sinais declarativos**, não garantias automáticas de verdade. O formato não verifica identidade, competência do revisor, independência dos verificadores ou qualidade da evidência. Uma verificação registrada tampouco equivale, necessariamente, à aprovação institucional.

Os níveis de confiança também **não são regras de autorização de acesso**. Permissões devem ser implementadas fora da especificação.

## 8. Atualidade e ciclo de vida

Conhecimento pode permanecer bem documentado e, mesmo assim, tornar-se obsoleto.

O campo `status` expressa o ciclo de vida do conceito:

- `draft`: conteúdo preliminar;
- `stable`: conteúdo disponibilizado para consumo;
- `deprecated`: conteúdo preservado, mas não mais corrente.

Quando `status` está ausente, a especificação adota `stable` como padrão. Isso **não deve ser interpretado como comprovação de revisão humana**; a verificação continua sendo representada separadamente por `verified`.

O campo `stale_after` indica um instante absoluto a partir do qual o conceito passa a ser considerado desatualizado. Sua presença não determina eliminação: sinaliza a necessidade de cautela ou reavaliação.

Três perguntas diferentes, portanto, convivem no formato:

1. **Quem produziu?** — `generated`.
2. **Quem conferiu?** — `verified`.
3. **Ainda está atual?** — `status` e `stale_after`.

## 9. Relações entre conceitos

Os documentos OKF podem apontar para outros conceitos por links Markdown comuns. Isso permite construir uma rede de relações navegáveis entre definições, procedimentos, indicadores e recursos.

Contudo, um link não identifica formalmente sua semântica. A relação — por exemplo, “depende de”, “refere-se a” ou “é derivado de” — é expressa normalmente pelo texto que acompanha o link.

Consequentemente, o OKF pode dar origem a um **grafo simples de documentos interligados**, mas **não é, por si só, uma ontologia formal nem um grafo de conhecimento com relações tipadas e restrições semânticas**.

A especificação permite inclusive links cujo destino ainda não existe; essa tolerância facilita evolução progressiva, mas requer atenção se o consumidor depender de integridade referencial rigorosa.

## 10. Computações atestadas

Uma extensão importante da versão 0.2 é o tipo `Attested Computation`. Ele documenta **uma maneira autorizada de calcular um resultado e um mecanismo para comprovar que essa maneira foi efetivamente utilizada**.

Seu contrato pode incluir:

- `runtime`: ambiente de execução, como SQL, Python ou dbt;
- `parameters`: parâmetros declarados e seus tipos;
- `computation`: referência ao cálculo, quando não estiver no corpo do documento;
- `executor`: instruções de execução e dados esperados de evidência (*receipt*);
- `attester`: verificação determinística dos resultados e do procedimento executado.

A ideia é distinguir duas operações que frequentemente são confundidas:

**Verificação do conceito:** confirma que a definição documentada está adequada às fontes ou políticas (`verified`).

**Atestação de uma execução:** confirma, para determinada execução, que um cálculo foi realizado conforme o procedimento autorizado e que o resultado corresponde à evidência retornada.

O OKF descreve esse contrato, mas **não executa cálculos, não fornece automaticamente um ambiente seguro de execução e não implementa um protocolo universal completo para os atestadores**. Parte desses detalhes permanece fora do escopo da versão 0.2.

## 11. Conformidade, interoperabilidade e extensibilidade

O OKF adota uma conformidade deliberadamente permissiva. Para um bundle ser conformante na versão 0.2, cada arquivo de conceito precisa ter frontmatter YAML válido e um `type` não vazio; arquivos reservados devem seguir suas estruturas, se existirem.

O consumidor não deve rejeitar um pacote apenas porque lhe faltam campos opcionais, porque contém tipos ou chaves desconhecidos, porque há links quebrados ou porque faltam índices.

Essa política facilita a interoperabilidade e a evolução incremental. Em contrapartida, **conformidade sintática mínima não significa completude informacional, confiabilidade ou governança suficiente**.

Extensões podem acrescentar campos de domínio específico. A compatibilidade depende, entretanto, de como diferentes produtores interpretam essas extensões: admitir chaves desconhecidas não significa atribuir-lhes uma semântica universal.

### 11.1. O papel do Git

O uso de Git é recomendado como opção de distribuição e versionamento, mas **não integra uma exigência de conformidade do OKF**.

Git registra alterações em arquivos e pode oferecer histórico e autoria de commits. Já o OKF descreve conceitos e metadados. Nenhum dos dois, isoladamente, garante que uma correção inclua sua motivação, a evidência que a sustenta, a identidade verificada do responsável e o efeito sobre todas as afirmações relacionadas.

## 12. Diferença entre a especificação OKF e o projeto AI Memory

É importante distinguir **formato** de **software que implementa o formato**.

A especificação OKF v0.2 está publicada no repositório `GoogleCloudPlatform/knowledge-catalog`. O projeto open source [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) é uma implementação de memória para agentes que passou a utilizar OKF de forma nativa em sua versão 2.0.

Segundo a documentação do AI Memory:

- as páginas da wiki são armazenadas como arquivos de conceitos OKF;
- o escopo de cada projeto corresponde a um bundle;
- o índice raiz do projeto é gerado com a declaração de versão;
- a implementação mapeia seus tipos internos, autoria, fontes e validade para campos OKF;
- uma exportação OKF pode transportar a memória para outras ferramentas compatíveis.

Esses são **comportamentos específicos da implementação**, não requisitos universais do formato. Busca, indexação, consolidação, histórico de páginas e integração de agentes pertencem à arquitetura do software, e não decorrem automaticamente de arquivos OKF.

Em particular, a regra do AI Memory de gerar um `index.md` raiz com `okf_version` não altera o caráter opcional desse arquivo na especificação geral.

## 13. Limites conceituais do OKF

A proposta do formato é útil justamente por delimitar aquilo que pretende padronizar. Entre os pontos que ele não resolve sozinho:

1. **Ingestão:** não define conectores para e-mail, mensagens, PDFs, áudio ou sistemas externos.
2. **Extração e interpretação:** não especifica como um agente identifica conceitos e os transforma em conhecimento consistente.
3. **Verificação factual:** metadados podem registrar verificações, mas não garantem a validade material das afirmações.
4. **Preservação de evidências:** uma referência externa pode mudar ou desaparecer; o formato não a torna imutável.
5. **Governança:** controle de acesso, confidencialidade, consentimento e segregação de usuários dependem de mecanismos externos.
6. **Resolução de conflitos:** a existência de fontes contraditórias não determina qual prevalece.
7. **Auditoria de correções:** metadados e Git ajudam na rastreabilidade, mas não estabelecem um fluxo obrigatório de justificativa, aprovação e reconciliação.
8. **Recuperação:** não inclui, como requisito, busca lexical, embeddings, reranking ou respostas de RAG.
9. **Semântica formal:** links textuais não substituem ontologias, tipagem de relações ou regras de inferência.

Essas limitações não caracterizam falhas de implementação. São consequência da intenção de manter um **formato mínimo e desacoplado de uma infraestrutura específica**.

## 14. Síntese

O Open Knowledge Format propõe representar conhecimento como **documentos Markdown portáveis com metadados padronizados**, organizados em bundles e interligados por referências.

Sua contribuição principal é criar um vocabulário comum para descrever **o que é um conceito, de onde ele veio, quem o produziu, quem o verificou e quando pode deixar de ser atual**. A versão 0.2 também introduz contratos para computações atestáveis.

A compreensão mais rigorosa é esta: **OKF é uma camada de representação e intercâmbio de conhecimento, não uma solução completa de memória, ingestão, busca ou governança**.

A avaliação de sua adequação a uma infraestrutura concreta e a definição de extensões ou componentes complementares pertencem a um estudo de aplicação separado deste artigo teórico.

## Conceitos transversais relacionados

Para interpretação consistente de `sources`, `generated`, `verified`, `status` e `stale_after`, consultar [Conceitos fundamentais para a confiança e evolução do conhecimento](conceitos-fundamentais-confianca-conhecimento.md). Essa referência distingue proveniência, verificação, validade temporal, histórico, versionamento, rastreabilidade e auditabilidade e identifica a relação com o glossário e a ontologia.

## Referências e leitura complementar

1. **GoogleCloudPlatform.** [Open Knowledge Format — SPEC.md, versão 0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md). Especificação primária: objetivos, campos, conformidade, proveniência, confiança, ciclo de vida e computações atestadas.
2. **akitaonrails.** [AI Memory — documentação de conformidade OKF 2.0](https://github.com/akitaonrails/ai-memory/blob/main/docs/okf.md). Descreve o mapeamento do formato para uma implementação de memória de agentes.
3. **akitaonrails.** [AI Memory — repositório do projeto](https://github.com/akitaonrails/ai-memory). Código e documentação geral.

**Data da consulta:** 20/11/2026. **Nota metodológica:** as explicações sobre limites e implicações práticas são análise conceitual a partir do escopo explicitamente declarado na especificação; não equivalem a testes de implementação.