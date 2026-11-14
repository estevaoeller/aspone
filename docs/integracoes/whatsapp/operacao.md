# Operação, backup e recuperação

## Rotina operacional

| Rotina | Estado observado no piloto em 14/11/2026 |
| --- | --- |
| Recepção de eventos | Contínua |
| Atualização de nomes | Processo a cada 15 minutos |
| Publicação | Manual, validada |
| Recuperação histórica | Piloto de um lote validado |
| Backup PostgreSQL | Dumps pontuais antes de intervenções |
| Backup periódico e externo | Não comprovado |
| Publicação horária | Não instalada |

A verificação considerou os timers do sistema e usuário acessíveis, o crontab do operador e locais comuns de cron. Isso não exclui uma rotina externa não observada. Não afirmar periodicidade sem logs e restauração comprovada.

## Proteção necessária

| Ativo | Método a avaliar | Frequência proposta, não implementada |
| --- | --- | --- |
| PostgreSQL | pg_dump consistente, cópia protegida fora do LAB | Diária e antes de mudanças |
| Sessão/cache GOWS | Backup SQLite consistente, incluindo tratamento de WAL; proteger credenciais da sessão | Conforme criticidade e antes de reconfiguração |
| Compose e scripts | Git e snapshot privado da configuração | A cada alteração |
| Markdown interno | Reconstruir do banco; preservar quando necessário | Conforme custo de recuperação |
| SharePoint | Governança, retenção e versionamento próprios | Conforme política institucional |

A política de retenção e destino externo ainda deve ser definida com autorização institucional. Não copiar conversas profissionais automaticamente para um repositório de backup pessoal. SharePoint contém apenas a projeção selecionada, portanto não substitui backup do banco, eventos ou sessão. Dump local não substitui proteção externa.

## Verificações e recuperação

Conferir saúde dos serviços, validação de correspondência entre mensagens e arquivos, mutações não resolvidas, log e integridade da publicação. Executar restauração em ambiente isolado, conferir contagens, eventos, reconstrução do Markdown e proteção contra exposição. Não restaurar o dump indiscriminadamente sobre a base ativa: preservar eventos posteriores. Em caso de falha de publicação, bloquear novas execuções, avaliar arquivos parciais e não usar sync destrutivo.

A validação de IDs do coletor não demonstra completude do WhatsApp, exatidão de toda interpretação ou autorização de compartilhamento. Os logs detalhados devem ficar em ambiente restrito.

## Relações

- [Implantação](implantacao.md)
- [Evolução](../../evolucao.md)
