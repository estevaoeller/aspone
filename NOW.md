# Situação atual

Atualizado em **25/11/2026**. Este registro descreve o repositório consultado nesta data; não substitui verificação de ambiente operacional.

## 20/11/2026 — Project Memory inicializada

- **Realizado:** criada a camada de continuidade do desenvolvimento do ASPONE com `PROJECT.md`, `NOW.md`, `TASKS.md`, `AGENTS.md`, `CLAUDE.md`, `_wiki/` e `history/`.
- **Documentação preservada:** `README.md`, `docs/` e `modules/whatsapp/` não foram substituídos.
- **Estado do produto segundo a documentação:** primeira integração WhatsApp validada em laboratório; ingestão de outras fontes e consolidação de conhecimento permanecem em investigação/proposta. Consultar [evolução](docs/evolucao.md).
- **Referências em avaliação:** Project Memory, AI Memory e Ariso/TRAM, sem adoção arquitetural automática.
- **Aberto:** aprofundar a distinção entre fonte, acontecimento e conhecimento consolidado e avaliar um experimento pequeno de correção rastreável.
- **Próximo passo sugerido:** selecionar uma das questões documentadas em `TASKS.md` para discussão incremental; não iniciar implementação sem solicitação.
- **Pendente de validação:** páginas analíticas da wiki com marca `REQUIRES_REVIEW`.

## 20/11/2026 — Referências conceituais na wiki pública

- **Registrado:** os estudos sobre OKF e sobre proveniência, verificação, validade temporal, histórico, versionamento, rastreabilidade e auditabilidade foram publicados em `_wiki/referencias/`, relacionados entre si, à pesquisa AI Memory e ao índice da wiki.
- **Escopo documental esclarecido:** a wiki pública do ASPONE é a referência de trabalho para esses estudos. A wiki privada do Homelab pode manter cópias e evidências operacionais, sem sincronização automática.
- **Validação:** o direcionamento para a wiki de trabalho foi indicado pela pessoa responsável; as interpretações e definições técnicas seguem `REQUIRES_REVIEW`.
- **Aberto:** harmonizar os termos de verificação ampla, validade temporal e histórico com o glossário e a ontologia, sem presumir identidade entre vocabulários.

## 20/11/2026 — Camada de Conhecimento e Verdade documentada

- **Realizado na wiki pública e docs:** publicada a definição inicial da camada, as três responsabilidades do ASPONE, o papel do MD como representação de fontes, a relação com Knowledge Advisor e quatro artigos interligados de aprofundamento (fonte/afirmação, ciclo de vida, W3C PROV, histórico bitemporal).
- **Destino canônico:** [camada conceitual](docs/conhecimento/camada-conhecimento-verdade.md), com estudos em [_wiki/INDEX.md](_wiki/INDEX.md) e [registro histórico](history/2026-11-20-camada-conhecimento-verdade.md).
- **Validação:** publicação solicitada pelo responsável; interpretações, exemplos e proposta conceitual mantidos como `REQUIRES_REVIEW`.
- **Não implementado/decidido:** tecnologias, modelo físico, critérios finais de autoridade e validação; nenhuma integração com Knowledge Advisor foi estabelecida.
- **Próxima questão para discussão:** afirmação contextualizada e passagem de evidência para conhecimento confirmado, em exemplo pequeno. Ver itens MEM-01 a MEM-06 do backlog.

## Blocos encerrados

- Nenhum bloco movido para o histórico ainda.

## 25/11/2026: identidade e dados anotados

- Consolidação documental da proposta de camada estruturada: [identidade](docs/contexto/identidade-e-cadastro.md), [anotações](docs/conhecimento/anotacoes-e-proveniencia.md) e [implementação incremental](docs/conhecimento/implementacao-camada-estruturada.md).
- Requisito: identificadores escaláveis, estáveis e reutilizáveis. ULID e UUIDv7 ainda em avaliação; nenhuma implementação ou cadastro real publicado.
- Próximo passo: revisar contratos lógicos e definir piloto sintético, vinculado ao backlog existente. [Histórico](history/2026-11-25-identidade-e-dados-anotados.md).
