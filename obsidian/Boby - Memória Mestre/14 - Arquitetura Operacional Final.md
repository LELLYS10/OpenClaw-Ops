# Arquitetura Operacional Final

## Objetivo
Fechar a base do BOBY/OpenClaw para operar com consistência, memória e integrações reais sem improviso.

## Camadas
1. Interface
- Telegram como canal principal.

2. Orquestração
- `BOOT.md` define regras absolutas.
- `AGENTS.md` define comportamento operacional e uso obrigatório de comandos locais.

3. Execução
- `google_bridge.py` concentra Gmail, Drive, Sheets, Agenda e vencidos.
- `time_now.py` é a fonte oficial de horário de Brasília.

4. Memória
- `MEMORY.md` para fatos duráveis.
- `memory/YYYY-MM-DD.md` para memória diária.
- Knowledge hub para contexto estrutural.

5. Governança
- Obsidian como mapa operacional.
- GitHub como trilha versionada.
- Auditoria e playbooks para reduzir esquecimento.

## Fontes de verdade
- Runtime ativo na VPS
- Hub operacional do BOBY
- Pasta `Boby - Memória Mestre`
- Repositório `OpenClaw-Ops`

## Regras
- Pergunta mutável exige verificação real.
- Pedido com formato explícito exige respeitar os campos pedidos.
- Falha real deve vir com causa e próximo passo.
- Mudança na VPS deve ser refletida no GitHub e no Obsidian.
