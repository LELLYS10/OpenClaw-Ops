# Deploy e Rollback

## Quando usar
- Alteracao em `BOOT.md`
- Alteracao em `AGENTS.md`
- Alteracao em `google_bridge.py`
- Ajuste de plugin, Telegram ou memoria operacional

## Deploy
1. Confirmar diff local no `OpenClaw-Ops`
2. Subir arquivo alterado para a VPS
3. Reiniciar `openclaw-189p-openclaw-1`
4. Validar comandos locais criticos:
- `gmail-unread`
- `drive-recent`
- `sheets-list`
- `calendar-today`
- `sheet-overdue MARCOS`
5. Validar pelo menos um caso real no Telegram
6. Registrar em auditoria e commitar no GitHub

## Rollback
1. Identificar qual arquivo quebrou
2. Restaurar backup local ou versao anterior do GitHub
3. Reenviar para a VPS
4. Reiniciar container
5. Revalidar a matriz minima

## Matriz minima de rollback
- identidade
- hora de Brasilia
- uma consulta Gmail
- uma consulta Drive
- uma consulta Sheets
- uma consulta Agenda

## Regra
- Nenhuma mudanca estrutural termina sem validacao real.
