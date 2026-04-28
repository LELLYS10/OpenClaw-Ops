# Deploy e Rollback do BOBY

## Quando usar
- Alteração em `BOOT.md`
- Alteração em `AGENTS.md`
- Alteração em `google_bridge.py`
- Ajuste de plugin, Telegram ou memória operacional

## Deploy
1. Confirmar diff local no `OpenClaw-Ops`
2. Subir arquivo alterado para a VPS
3. Reiniciar `openclaw-189p-openclaw-1`
4. Validar comandos locais críticos
5. Validar pelo menos um caso real no Telegram
6. Registrar em auditoria e commitar no GitHub

## Rollback
1. Identificar o arquivo que quebrou
2. Restaurar backup local ou versão anterior do GitHub
3. Reenviar para a VPS
4. Reiniciar o container
5. Revalidar a matriz mínima

## Matriz mínima
- identidade
- hora de Brasília
- Gmail
- Drive
- Sheets
- Agenda
