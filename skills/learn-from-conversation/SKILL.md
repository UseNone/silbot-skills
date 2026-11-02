---
name: Transformar aprendizados em skills
description: Identificar procedimentos reutilizáveis nas conversas, correções e preferências explícitas do usuário e propor uma skill quando houver evidência suficiente.
---

# Transformar aprendizados em skills

Use quando o usuário ensinar uma sequência de trabalho, corrigir repetidamente um procedimento, ou validar um resultado que poderá repetir. Considere o contexto da conversa proativamente; não transforme toda conversa em proposta.

1. Identifique o procedimento aprendido, seu gatilho e o resultado esperado. Diferencie instruções explícitas do usuário, resultados verificados e hipóteses. Uma tarefa isolada ou um fato pessoal deve permanecer na conversa ou na memória, sem virar uma skill genérica.
2. Consulte `UpdateSkill(action="list")` e, se houver uma skill relacionada, leia-a com `ReadSkill`. Prefira propor uma melhoria à duplicação. Não altere skills oficiais do SilBot.
3. Quando o aprendizado for claro e útil, proponha em uma frase: "Posso transformar esse procedimento em uma skill para repetir [resultado] quando [gatilho]?" Mostre o nome e um resumo do que será salvo. Se o usuário já pediu para criar/salvar a skill, a autorização existe: prepare e salve diretamente, respeitando o escopo pedido.
4. Redija instruções em português ou no idioma do usuário, contendo: quando usar; entradas necessárias; passos essenciais; critério de conclusão; limitações observadas. Parametrize nomes, datas, caminhos e exemplos incidentais. Não salve senhas, tokens, códigos de login, dados pessoais desnecessários, suposições não confirmadas ou o histórico integral da conversa.
5. Após a aceitação, use `UpdateSkill(action="write", name=..., description=..., body=...)`; informe `id` apenas para uma atualização autorizada. Novas skills ficam no escopo do bot atual. Não prometa disponibilização a outros bots sem configurar esse escopo explicitamente.
6. Só declare que a skill foi criada após a ferramenta retornar sucesso. Apresente o link `[Nome](silbot-skill:<id retornado>)`, o gatilho e o que foi aprendido. Em caso de falha, preserve o rascunho e explique sem afirmar que salvou.

Propor uma skill não concede autorização para executar suas ações futuras. Uma skill é um procedimento reutilizável, sujeito ao pedido e às permissões atuais. Caso o usuário recuse a proposta, continue a tarefa sem insistir.
