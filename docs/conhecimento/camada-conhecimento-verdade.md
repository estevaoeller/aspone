# ASPONE — Camada de Conhecimento e Verdade dos Projetos

**Estado:** definição conceitual inicial, em discussão (`REQUIRES_REVIEW`). **Data:** 20/11/2026. **Escopo:** conhecimento de projetos durante todo o ciclo de vida, não implementação já concluída.

## 1. A distinção que fundamenta o ASPONE

**Armazenar informações, recuperar informações e manter conhecimento sobre um projeto são três problemas diferentes.**

Guardar milhares de mensagens de WhatsApp, documentos, atas, e-mails e transcrições é necessário para preservar o histórico, mas não basta para responder com segurança: *o que está decidido, o que mudou, quais premissas estão vigentes e onde está a evidência?*

O ASPONE busca uma infraestrutura independente de aplicações específicas. O núcleo experimental de WhatsApp, com WAHA, PostgreSQL, projeções Markdown, recuperação de históricos ZIP e distribuição seletiva no SharePoint, ajuda a resolver **ingestão e preservação**. Não constitui, por si, uma memória consolidada dos projetos. Consultar [arquitetura](../arquitetura.md), [alimentação multifuente](../alimentacao/README.md) e [consolidação e correções](README.md).

## 2. Definição inicial

> **A Camada de Conhecimento e Verdade do ASPONE é o conjunto de mecanismos responsáveis por transformar informações provenientes de diferentes fontes em uma representação organizada, contextualizada, temporal, rastreável e continuamente atualizável do conhecimento sobre projetos.**
>
> Essa representação deve distinguir evidências, afirmações, interpretações, inferências e decisões validadas, preservando o histórico de sua evolução e permitindo identificar o fundamento e o grau de confirmação de cada informação.

A expressão **verdade** designa uma responsabilidade epistemológica e de governança: explicitar o fundamento e a condição das afirmações, não atribuir infalibilidade à IA ou garantir que tudo o que uma fonte registra aconteceu. Uma fonte pode ser autêntica e conter uma previsão, um equívoco ou um entendimento posteriormente substituído. A camada deve poder dizer *o que se sabe, como se sabe, desde quando, em qual escopo e o que ainda não se sabe*.

**Status da definição:** proposta de trabalho para discussão; a redação não equivale a decisão arquitetural ou regra de homologação.

## 3. Três responsabilidades conceitualmente diferentes

~~~mermaid
flowchart TB
    F["Fontes: mensagens, documentos, atas, e-mails, transcrições"]
    I["1. Ingestão e preservação<br/>O que recebemos? De onde veio?"]
    K["2. Conhecimento e verdade<br/>O que podemos afirmar? O que mudou? Por quê?"]
    C["3. Consumo do conhecimento<br/>Como utilizar de forma autorizada?"]
    U["RAG, agentes, Watchtower, Knowledge Advisor e outras aplicações"]
    F --> I
    I --> K
    I -. "acervo consultável" .-> C
    K --> C
    C --> U
~~~

O desenho é **conceitual**, não uma arquitetura física ou fluxo já implantado. O acervo pode também ser consultado diretamente por consumidores autorizados. As camadas podem compartilhar componentes, sem confundir suas responsabilidades.

| Dimensão | 1. Ingestão e preservação | 2. Conhecimento e verdade | 3. Consumo |
| --- | --- | --- | --- |
| Pergunta | O que chegou, quando e de onde? | O que significa, qual seu estado e fundamento? | Como responder ou agir com isso? |
| Unidade de trabalho | Mensagem, arquivo, versão, evento de coleta | Projeto, entidade, afirmação, acontecimento, decisão, premissa, vínculo | Resposta, alerta, relatório, ação, consulta |
| Responsabilidade | Preservar originais, metadados e rastreabilidade | Relacionar, consolidar, revisar, contextualizar e historizar | Aplicar permissões, recuperar e apresentar conhecimento para um uso |
| Risco de confusão | Considerar MD como conhecimento pronto | Tratar extração de IA como decisão efetiva | Deixar cada aplicativo redefinir a verdade do projeto |
| Produto esperado | Acervo verificável | Conhecimento sustentado e evolutivo | Serviços e funcionalidades úteis |

**Não confundir essas três responsabilidades com as duas capacidades de produto do README:** *acervo documental* e *memória de conhecimento*. As duas capacidades descrevem o que o ASPONE oferece; as três responsabilidades descrevem partes do ciclo de informação e conhecimento.

## 4. Responsabilidades da camada de conhecimento

1. **Identificar e contextualizar:** reconhecer projetos, pessoas, equipes, organizações, documentos, reuniões, eventos e vínculos, inclusive muitos-para-muitos. Um grupo de WhatsApp não equivale a um projeto.
2. **Interpretar sem promover automaticamente:** localizar afirmações, propostas, dúvidas, acontecimentos, responsabilidades, compromissos e decisões alegadas. Preservar a diferença entre trecho literal e interpretação.
3. **Relacionar e consolidar:** reunir evidências distribuídas, distinguir repetições de corroborações independentes e organizar o conhecimento por projeto, assunto e período.
4. **Manter o tempo explícito:** diferenciar data do acontecimento, vigência da informação, data em que foi registrada e momento da revisão. Não presumir que “mais recente” significa “vigente”.
5. **Evidenciar conflito e incerteza:** registrar versões divergentes, lacunas, hipótese não validada, autoridade ainda desconhecida e fontes contraditórias.
6. **Permitir validação e correção auditáveis:** registrar autor da proposta, revisor, motivo, evidências, alteração, vigência e relação com versões anteriores; não apagar o passado.
7. **Servir a consumidores com governança:** permitir usos diferentes e compartilhamento conforme permissões, sem se tornar propriedade de um único RAG, agente ou Watchtower.

**Limite:** classificação, extração e consolidação sugeridas por IA não conferem, por si, aprovação humana, autoridade decisória ou permissões de acesso.

## 5. Exemplo: um modelo econômico-financeiro

*Exemplo inteiramente fictício, sem dados reais de projeto.*

- **10/11:** João escreve “A previsão é entregar o modelo na sexta-feira”.
- **12/11:** Maria escreve “Precisaremos adiar para segunda por causa da revisão dos investimentos”.
- **16/11:** um e-mail informa “Segue o modelo atualizado, versão 3”.

O acervo guarda os registros. A camada de conhecimento pode **propor** que existe uma entrega, com previsão inicial, possível alteração de prazo, justificativa e evidência de encaminhamento de uma versão. Mas há verificações distintas:

| Afirmação ou questão | Tratamento prudente |
| --- | --- |
| Havia previsão de entrega na sexta | Atribuir à mensagem de João; previsão, não compromisso necessariamente aprovado |
| A entrega passou para segunda | Mensagem é evidência de anúncio; confirmar autoridade e concordância |
| Houve encaminhamento de versão 3 | Evidência de e-mail; conferir destinatários e anexo |
| O modelo foi aceito pelo cliente | **Não demonstrado** pelas três fontes |
| O projeto não tem mais pendências | **Não demonstrado** pelas três fontes |

O sistema não deve converter “enviado” em “aprovado”, nem transformar a interpretação de um agente em validação humana. Ver [fonte, afirmação e conhecimento](../../_wiki/conceitos/fonte-afirmacao-conhecimento.md).

## 6. Fonte de verdade: uma propriedade contextual

Não pressupor um único documento “verdadeiro” para todas as perguntas. Uma ata aprovada pode ter autoridade para determinada decisão; uma planilha revisada pode conter o cálculo utilizado; um e-mail pode comprovar o envio. Essas fontes respondem **perguntas diferentes**. A autoridade pode depender do tipo de informação, processo, competência decisória, versão, período e evidência disponível.

A camada precisa distinguir:
- **integridade/autenticidade da fonte:** é o registro que afirmamos ter recebido?
- **conteúdo declarado:** o que a fonte efetivamente diz?
- **validade e confirmação:** a afirmação é aplicável ao projeto e foi confirmada por quem tem competência?
- **estado atual do conhecimento:** o que sabemos hoje e como isso difere do que sabíamos antes?

Uma correção não reescreve mensagens e documentos originais; cria ou modifica o **estado do conhecimento**, preservando o encadeamento justificativo. Ver [proveniência W3C PROV](../../_wiki/referencias/w3c-prov.md) e [histórico bitemporal](../../_wiki/referencias/historico-bitemporal.md).

## 7. Papel dos arquivos Markdown

Os arquivos MD atualmente produzidos são **representações das fontes para leitura, intercâmbio e distribuição**, não necessariamente as unidades canônicas de conhecimento. Podem servir como entrada para interpretação, busca e consulta. O conhecimento de uma decisão, entretanto, pode depender de passagens em diversas fontes e versões.

Consequências conceituais:
- apontar, quando possível, para a **mensagem, trecho, registro e versão** de origem, e não só para um arquivo diário;
- evitar que “mais arquivos de resumo” sejam confundidos com organização do conhecimento;
- preservar a possibilidade de reconstruir projeções Markdown a partir das fontes e do conhecimento mantido;
- não exigir edição manual de MD como fluxo final de validação humana.

O modo de representação e armazenamento do conhecimento **permanece em aberto**.

## 8. Conhecimento enquanto o projeto está acontecendo

O ASPONE deve acompanhar o **dia a dia do projeto**: mudanças, decisões, premissas, entregas, dúvidas e responsáveis. O encerramento não inaugura a gestão do conhecimento; permite também o reaproveitamento de aprendizados e produtos históricos. Ver [gestão do conhecimento ao longo do ciclo de vida](../../_wiki/conceitos/gestao-conhecimento-ciclo-vida.md).

O [Knowledge Advisor](https://github.com/FGV-Projetos-IA/knowledge-advisor) explora fluxos de documentos, evidências, RAG, agentes e reutilização institucional. Há afinidade conceitual, mas **não há integração técnica aprovada**. Não reduzir o Knowledge Advisor a “RAG de relatórios” nem restringir a gestão do conhecimento ao pós-projeto.

## 9. O que está decidido e o que está em estudo

**Princípios já estabelecidos no ASPONE:** independência das aplicações; preservação dos originais; proveniência; correções auditáveis; distinção entre extração, inferência e validação humana; evolução incremental.

**Propostas ainda em discussão:** esta definição da camada; unidades de conhecimento; critérios de autoridade e confirmação; modelo de temporalidade; instrumentos para conflitos; formato de armazenamento e interoperação.

**Não decidido:** adoção de W3C PROV-O, banco temporal, grafo, ontologia, framework, sistema de agentes ou padrão de arquivos.

## 10. Leituras vinculadas

- [Consolidação, correções e conhecimento vigente](README.md) — proposta já existente de fluxo e estados.
- [Fonte, afirmação, evidência e validação](../../_wiki/conceitos/fonte-afirmacao-conhecimento.md) — distinções epistemológicas.
- [Gestão do conhecimento durante o ciclo do projeto](../../_wiki/conceitos/gestao-conhecimento-ciclo-vida.md) — ASPONE e Knowledge Advisor.
- [W3C PROV](../../_wiki/referencias/w3c-prov.md) — proveniência das transformações.
- [Histórico bitemporal](../../_wiki/referencias/historico-bitemporal.md) — vigência e evolução do que sabíamos.
- [Conceitos fundamentais](../../_wiki/referencias/conceitos-fundamentais-confianca-conhecimento.md) — glossário de conceitos correlatos.
- [Contexto compartilhado](../contexto/README.md) — projetos, pessoas, reuniões e vínculos.
