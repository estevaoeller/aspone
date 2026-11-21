---
type: Project Wiki
date_created: 20/11/2026
date_modified: 20/11/2026
related:
  - "[[conceitos-fundamentais-confianca-conhecimento]]"
  - "[[w3c-prov]]"
  - "[[fonte-afirmacao-conhecimento]]"
domain: ASPONE
client: A definir
engagement: A definir
organization: A definir
status: REQUIRES_REVIEW
---

# Histórico bitemporal — quando algo valia e quando passamos a saber

**Natureza:** estudo de padrão de modelagem temporal existente; **não** decisão de banco, estrutura física ou mecanismo de versionamento. **Estado do artigo:** `REQUIRES_REVIEW`.

## 1. O problema do “que sabíamos na época?”

Informações sobre projetos não mudam apenas porque o projeto mudou. Às vezes **descobrimos hoje que uma condição já tinha mudado dias atrás**. Uma história linear de arquivos substituídos perde essa diferença.

O **histórico bitemporal** (*bitemporal history*) trabalha com duas dimensões temporais principais:

| Dimensão | Pergunta | Termos usados na literatura |
| --- | --- | --- |
| **Tempo de validade** | Quando a condição representada era aplicável ao projeto ou ao mundo descrito? | *valid time*, *actual time*, *application/business time* |
| **Tempo de registro/conhecimento no sistema** | Quando determinada versão da informação constava no sistema? | *transaction time*, *record time*, *system time* |

Essas expressões têm diferenças de implementação e uso entre autores e SGBDs. Em particular, **tempo de registro em banco** não equivale sempre ao instante em que uma pessoa tomou conhecimento de algo; este pode precisar de registro próprio.

A bitemporalidade permite perguntas como: “Qual prazo hoje entendemos que valia em 15/11?” e “Em 15/11, qual prazo o sistema registrava como vigente para aquela data?”.

## 2. Exemplo de projeto — fictício

Suponha o seguinte histórico:

- **10/11:** o sistema registra prazo de entrega **20/11**.
- **12/11:** uma decisão efetiva altera o prazo para **25/11**, valendo desde 12/11; o sistema ainda não tem esse registro.
- **18/11:** chega uma ata que informa a decisão do dia 12; a informação é incorporada após conferência adequada.

| Consulta | Resposta contextualizada |
| --- | --- |
| O que o sistema sabia em **15/11** sobre o prazo? | Registrava **20/11** |
| O que hoje sabemos sobre o prazo aplicável em **15/11**? | Que havia sido alterado para **25/11**, **se** a decisão tiver autoridade e efeito desde 12/11 |
| Quando o sistema recebeu essa correção de entendimento? | **18/11** |
| O que ocorreu com o registro antigo? | Mantém-se na história do conhecimento, não é apagado silenciosamente |

A bitemporalidade pode representar a coexistência entre **história de validade** e **história do que estava registrado**. O exemplo também exige proveniência da ata e confirmação da autoridade decisória: bitemporalidade sozinha não resolve isso.

## 3. Datas que ainda precisam ser distinguidas

Duas dimensões temporais resolvem um problema específico, mas podem existir outros marcos relevantes:

- **data do evento:** quando a reunião ocorreu ou a pessoa enviou a mensagem;
- **data do documento:** quando o arquivo foi elaborado ou emitido;
- **data da ingestão:** quando a fonte entrou no acervo ASPONE;
- **vigência:** quando a regra, responsabilidade ou premissa é aplicável;
- **registro do conhecimento:** quando uma afirmação passou a constar numa versão do sistema;
- **verificação e aprovação:** quando e por quem determinada revisão foi feita;
- **prazo/expiração/revisão:** quando algo deve ser reexaminado.

**Não reduzir todos esses marcos a `created_at` e `updated_at`.** Tampouco presumir que uma decisão registrada posteriormente era de conhecimento das equipes na data de validade retroativa.

## 4. O que existe na literatura e nos padrões

**Martin Fowler**, no padrão *Bitemporal History*, descreve uma história em duas dimensões: *actual history* (o que consideramos ter acontecido no período) e *record history* (como a representação registrada dessa história mudou). É uma explicação especialmente útil para pensar no conhecimento revisável dos projetos.

O **SQL:2011** incluiu recursos temporais, como períodos de tempo de aplicação e de sistema. A combinação dessas perspectivas é conhecida na literatura e em produtos como tabelas bitemporais. O padrão SQL não determina, por si, um sistema de proveniência ou curadoria de afirmações. O suporte concreto varia conforme SGBD e implementação.

**Richard T. Snodgrass** é uma referência histórica importante na área de bancos de dados temporais; a terminologia *valid time* e *transaction time* está associada a essa tradição.

Esses referenciais ajudam a **não inventar novamente** um problema de modelagem conhecido, sem exigir que o ASPONE adote desde já tabelas temporais.

## 5. O que seria útil no ASPONE

1. **Reconstruir um estado passado:** o que o projeto considerava vigente em uma data de referência.
2. **Reconstituir a informação disponível naquele momento:** o que o sistema tinha registrado em outra data.
3. **Distinguir correção retroativa de mudança atual:** descobrimos um equívoco anterior ou aconteceu uma nova decisão?
4. **Tratar substituições parciais:** uma premissa pode mudar apenas para um cenário, lote, entrega ou período.
5. **Evitar falsas conclusões de atualidade:** a mensagem mais nova não substitui automaticamente uma decisão vigente.

**Limites:** modelos temporais não verificam a veracidade das afirmações, não definem a autoridade de quem decide e não substituem proveniência, controle de acesso ou auditoria. É necessário pensar também em conflitos e múltiplas versões que ainda estejam em disputa.

## 6. Relação com W3C PROV e versionamento

- **Bitemporalidade:** quando a informação se aplicava e quando constava no sistema.
- **W3C PROV:** de que fontes, processos e agentes a informação deriva.
- **Versionamento:** quais representações ou estados foram preservados em cada revisão.
- **Validação humana:** que decisão autorizada aceitou, rejeitou ou contestou uma proposta de atualização.

Essas responsabilidades são **complementares**, não substitutas. Uma ferramenta de Git, por exemplo, não representa automaticamente tempo de validade no mundo. Ver [W3C PROV](w3c-prov.md), [conceitos fundamentais](conceitos-fundamentais-confianca-conhecimento.md) e [definição da camada](../../docs/conhecimento/camada-conhecimento-verdade.md).

## 7. Questões em aberto para o ASPONE

- Quais informações exigem vigência com intervalo explícito e quais demandam apenas data do evento?
- Como representar períodos desconhecidos, disputados ou condicionais?
- Como relacionar decisões com efeito retroativo, atrasos na ingestão e revisão de afirmações?
- Precisamos preservar o instante em que *o sistema registrou* e o instante em que *uma pessoa soube*?
- Quais padrões serão suficientes antes de escolher qualquer tecnologia?

## 8. Referências verificáveis

1. **[Martin Fowler — Bitemporal History](https://martinfowler.com/articles/bitemporal-history.html)** — explicação do padrão e da reconstrução da história em duas dimensões.
2. **[Martin Fowler — Temporal Patterns](https://martinfowler.com/eaaDev/timeNarrative.html)** — discussão mais ampla sobre *record time* e *actual time*.
3. **[PostgreSQL Wiki — SQL2011Temporal](https://wiki.postgresql.org/wiki/SQL2011Temporal)** — visão técnica das noções do SQL:2011; **é uma página de wiki, não comprovação de suporte integral pelo PostgreSQL**.
4. **[IBM Db2 — Temporal tables and data versioning](https://www.ibm.com/docs/en/db2-for-zos/13.0.0?topic=tables-temporal-data-versioning)** — documentação de implementação que distingue temporalidade de sistema, aplicação e bitemporalidade.
5. **[Richard T. Snodgrass — SQL3 Support for Time](https://www2.cs.arizona.edu/~rts/sql3.html)** — histórico dos conceitos temporais e sua relação com SQL:2011.

**Ordem sugerida de leitura:** Fowler para entender o problema; SQL2011Temporal e Snodgrass para terminologia; Db2 para ver um exemplo de suporte em produto existente — sem implicação de escolha do fornecedor.
