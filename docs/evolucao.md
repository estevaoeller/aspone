# Evolução e critérios de conclusão

O ASPONE ainda está em desenvolvimento. Cada incremento deve ser documentado com objetivo, evidência e limites, sem antecipar a arquitetura inteira.

| Frente | Estado | Critério de conclusão |
| --- | --- | --- |
| WhatsApp live | Validado no LAB | Saúde e correspondência contínuas, testes de mutação reais |
| Publicação seletiva | Manual validada | Timer, logs, verificações e falhas tratadas |
| Recuperação histórica | Piloto | Lotes progressivos, checkpoints, deduplicação e tratamento de mutações |
| Continuidade | Backup pontual | Política autorizada, execução periódica, proteção externa e restauração testada |
| Engenharia | Núcleo do coletor versionado | Publicador e backfill parametrizados, testes e pacote de implantação reproduzível |
| Contrato de consumo | Em definição | Identidade de fonte, atualizações, proveniência, permissões e versionamento |
| Outras fontes | Conceitual | Experimentos e contratos próprios |
| Memória de conhecimento | Conceitual | Relação entre fontes, afirmações, correções e revisão humana |

## Backlog vivo

A lista detalhada de entregas, descobertas e dependências está no [To-do list](backlog.md). Este documento permanece como visão resumida de maturidade, não como lista concorrente de tarefas.

## Relações

- [Wiki](README.md)
- [Backlog](backlog.md)
- [Arquitetura](arquitetura.md)
