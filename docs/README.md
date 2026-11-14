# Wiki do ASPONE

Esta árvore é a fonte versionada de documentação de produto, arquitetura e engenharia. A documentação de um ambiente específico permanece no registro operacional privado. Não confundir projeto de arquitetura com estado observado.

| Documento | Pergunta que responde |
| --- | --- |
| [Negócio](negocio.md) | Por que existe e quem se beneficia? |
| [Arquitetura](arquitetura.md) | Como as capacidades se relacionam? |
| [Integração WhatsApp](integracoes/watchtower-whatsapp.md) | O que a primeira fonte implementa? |
| [Implantação técnica](integracoes/whatsapp/implantacao.md) | Como os componentes são configurados e operados? |
| [Dados e proveniência](integracoes/whatsapp/dados.md) | O que é preservado e como se trata alterações? |
| [Distribuição SharePoint](integracoes/whatsapp/sharepoint.md) | Como outras pessoas e sistemas consomem o acervo? |
| [Continuidade e backup](integracoes/whatsapp/operacao.md) | Como verificar, recuperar e manter o fluxo? |
| [Código](../modules/whatsapp/README.md) | Quais scripts existem, quais estão versionados? |
| [Evolução](evolucao.md) | O que falta e como saber se está pronto? |

## Regras de manutenção

1. Distinguir observado, proposto e pendente; datar evidências de implantação.
2. Preservar fonte original, projeção documental, inferências e validação humana como coisas distintas.
3. Registrar mudanças na documentação canônica e usar links relativos; não repetir toda a Wiki no README.
4. Versionar código e exemplos sem segredos; não incluir conversas, identificadores reais, configurações privadas, dumps, sessões ou tokens.
5. Detalhes operacionais específicos ficam em documentação privada; SharePoint recebe o guia de consumo e o acervo autorizado, não o banco ou as credenciais.

## Relações

- [README](../README.md)
- [Arquitetura](arquitetura.md)
