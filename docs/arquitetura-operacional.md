# Arquitetura Operacional

## Objetivo
Fechar a base do BOBY/OpenClaw para operar com consistência, memória e integrações reais sem depender de improviso.

## Camadas
1. Interface
- Telegram como canal principal com validação ponta a ponta.

2. Orquestração
- `BOOT.md` define regras absolutas.
- `AGENTS.md` define comportamento operacional e uso obrigatório de comandos locais.

3. Execução local
- `google_bridge.py` concentra Gmail, Drive, Sheets, Agenda e consultas de vencidos.
- `time_now.py` é a fonte de hora oficial de Brasília.

4. Memória
- `MEMORY.md` para fatos duráveis.
- `memory/YYYY-MM-DD.md` para memória diária e trilha de tarefa.
- Knowledge hub em `/data/.openclaw/knowledge-hub/boby-openclaw/` para contexto estrutural.

5. Governança
- Obsidian como memória humana e mapa operacional.
- GitHub como trilha versionada do que é publicável e reprodutível.
- Auditoria e playbooks para reduzir esquecimento e respostas genéricas.

## Fontes de verdade
- Runtime ativo na VPS: `/docker/openclaw-189p/data/.openclaw/workspace`
- Hub operacional: `/docker/openclaw-189p/data/.openclaw/knowledge-hub/boby-openclaw`
- Vault operacional: `Boby - Memória Mestre`
- Repositório versionado: `OpenClaw-Ops`

## Regras de operação
- Pergunta mutável exige verificação real antes de responder.
- Pedido com formato explícito exige respeitar exatamente os campos pedidos.
- Falha real deve ser explicada com causa e próximo passo, não com texto genérico.
- Mudança estrutural na VPS deve ser refletida no GitHub e no Obsidian.

## Próximo nível
- Bateria fixa de validação Telegram.
- Memória diária obrigatória ao fim de tarefas relevantes.
- Base pronta para futura camada de swarm sem misturar isso com CredPlus neste momento.
