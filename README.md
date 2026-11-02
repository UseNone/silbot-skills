# SilBot Skills

Catálogo oficial distribuído pelo SilBot: skills próprias da equipe UseNone e uma seleção portátil do projeto [anthropics/skills](https://github.com/anthropics/skills).

## Catálogo para aplicativos

`https://raw.githubusercontent.com/UseNone/silbot-skills/main/catalog.json`

Acesso público, sem token. Cada registro inclui origem, descrição, revisão SHA-256 e arquivos com seus hashes. O SilBot busca novamente o catálogo periodicamente e permite atualizar skills oficiais instaladas. As skills do usuário são preservadas.

## Curadoria

Foram retiradas `claude-api`, `academy-guide`, `brand-guidelines`, `web-artifacts-builder` e `discernment-nudge`, por serem específicas de produtos, marca ou comportamento da Claude. `docx`, `pdf`, `pptx` e `xlsx` também foram removidas: o upstream as identifica como proprietárias/source-available.

As skills herdadas mantêm os arquivos de licença e a autoria Anthropic. Não são apresentadas como criações originais do SilBot. As skills `learn-from-conversation` e `learn-from-demonstration` são instruções próprias para o runtime do SilBot.

## Atualização

`python scripts/sync_upstream.py` atualiza apenas a lista portátil revisada e reconstrói o manifesto. Um workflow diário executa esse processo; novas pastas do upstream não entram automaticamente na distribuição. O manifesto também pode ser reconstruído com `python scripts/build_catalog.py`.

Instruções não concedem permissões de execução. A instalação não executa scripts nem instala dependências.
