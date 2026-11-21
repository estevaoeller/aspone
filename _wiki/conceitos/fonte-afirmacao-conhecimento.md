---
type: Project Wiki
date_created: 20/11/2026
date_modified: 20/11/2026
related:
  - "[[camada-conhecimento-verdade]]"
  - "[[w3c-prov]]"
  - "[[historico-bitemporal]]"
domain: ASPONE
client: A definir
engagement: A definir
organization: A definir
status: REQUIRES_REVIEW
---

# Fonte, afirmação, evidência, interpretação e conhecimento

**Estado:** conceitos candidatos para estudo (`REQUIRES_REVIEW`), não um esquema de dados aprovado.

## 1. Por que estas palavras não são sinônimas?

Uma mensagem preservada não é um fato automaticamente estabelecido. Um resumo pode ser fiel ao texto e ainda omitir condições importantes. Uma interpretação da IA pode ser plausível sem estar confirmada. E uma decisão requer contexto e autoridade, não apenas uma frase com o verbo “decidir”.

Para o ASPONE, interessa registrar as passagens entre essas categorias **sem apagar as diferenças**.

| Termo | Papel | O que não garante |
| --- | --- | --- |
| **Fonte** | Registro recebido, com origem, versão e contexto | Que seu conteúdo é correto |
| **Trecho / declaração** | Conteúdo efetivamente expresso em uma fonte | Que a declaração corresponde a fato validado |
| **Afirmação** | Proposição sobre algo do projeto, explicitada ou extraída com escopo | Que a proposição está confirmada |
| **Evidência** | Fonte ou elemento que sustenta ou contesta uma afirmação específica | Que o conjunto de evidências é suficiente |
| **Interpretação / inferência** | Leitura ou conclusão produzida por humano ou IA | Que foi autorizada por alguém competente |
| **Conhecimento consolidado** | Estado organizado de afirmações, relações, contexto e fundamentos | Que seja infalível ou permanente |
| **Decisão validada** | Decisão com autoridade, escopo e confirmação estabelecidos | Que permaneça vigente indefinidamente |

**Uma mesma fonte pode dar origem a várias afirmações.** Uma afirmação pode ter várias evidências favoráveis e contrárias. Várias citações repetidas de uma única mensagem **não** equivalem a várias confirmações independentes.

## 2. Exemplo fictício de mudança de prazo

Mensagem: “Podemos mudar a entrega para segunda-feira?”

- **Fonte:** mensagem original, remetente, conversa, horário, identificador e versão.
- **Declaração:** pergunta/proposta de mudança de prazo.
- **Afirmação candidata:** há proposta de alterar a data de entrega.
- **Inferência indevida:** “a entrega foi oficialmente reagendada”.
- **Evidência adicional possível:** resposta de aceite, ata formal, atualização de cronograma.
- **Conhecimento prudente:** alteração *em discussão*, até existir evidência suficiente de aceitação e autoridade.

Se depois uma pessoa autorizada confirmar a mudança, a nova condição do conhecimento deve ser registrada com autoria, fundamento e data; o registro anterior continua recuperável.

## 3. Perguntas que uma afirmação contextualizada precisa permitir responder

Não são campos obrigatórios de um banco definido, mas **dimensões de informação a investigar**:

1. **Sobre o quê:** projeto, assunto, entidade ou acontecimento?
2. **O que é declarado:** qual conteúdo, de modo suficientemente específico?
3. **Origem:** quais mensagens, trechos, documentos e versões sustentam?
4. **Produção:** extração textual, interpretação humana, inferência da IA ou cálculo?
5. **Tempo:** quando ocorreu, quando valeu e quando passamos a saber?
6. **Escopo:** qual cenário, artefato, parte do projeto ou condição?
7. **Confirmação:** quem confirmou, em que capacidade e por qual procedimento?
8. **Relações:** complementa, contradiz, substitui ou restringe outra afirmação?
9. **Revisões:** o que foi corrigido, por quem, quando, por quê e com que evidência?
10. **Acesso:** quem pode consultar a fonte e os derivados?

É possível que uma informação contenha campos desconhecidos. **“Não identificado” deve ser preservado como ausência de conhecimento, não preenchido por suposição.**

## 4. O que a camada deve evitar

- Promover texto extraído a decisão validada apenas porque a IA assim classificou.
- Presumir que a fonte mais recente tem maior autoridade em qualquer assunto.
- Substituir a origem pelo arquivo Markdown de resumo.
- Perder a relação com a afirmação anterior quando uma correção é aceita.
- Confundir concordância entre fontes com confirmação independente.
- Dizer “não há pendências” quando apenas não foram encontradas no corpus acessível.

## 5. Conexões com padrões existentes

O [W3C PROV](../referencias/w3c-prov.md) oferece vocabulário para **origem e transformações** de entidades, atividades e agentes. A [modelagem bitemporal](../referencias/historico-bitemporal.md) ajuda a distinguir a **vigência de uma condição** do **momento em que ela foi registrada/conhecida**. Nenhum dos dois determina automaticamente se uma afirmação é correta ou formalmente aprovada.

Ver também [conceitos fundamentais](../referencias/conceitos-fundamentais-confianca-conhecimento.md) e [processo de consolidação e correções](../../docs/conhecimento/README.md).

## Próximo aprofundamento proposto

Definir, com exemplos reais autorizados ou fictícios, a unidade **afirmação contextualizada** e o ciclo de sua promoção, contestação, revisão e substituição. **Ainda não escolher esquema, formato de armazenamento ou framework.**
