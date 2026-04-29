# Estado Atual do OpenClaw

## Situação geral
- BOBY em operação na VPS
- Google OAuth validado para Gmail, Drive, Agenda e Sheets
- timezone de Brasília aplicado
- gabarito comportamental condensado e aplicado ao runtime

## Runtime crítico já alterado
- `AGENTS.md`
- `BOOT.md`
- `google_bridge.py`

## Melhorias já implantadas
- remoção de respostas genéricas quando houver integração válida
- consulta real de vencidos da planilha `JEAN`
- redução de preâmbulo genérico e tom de atendente
- base documental criada no Obsidian e espelho técnico local
- poda de skills até o mínimo útil
- skills bundladas desativadas por config
- skill ativa no prompt: `super-memoria`

## Próximos passos
1. versionar o espelho técnico deste diretório
2. trazer cópia limpa dos arquivos críticos da VPS para `runtime/`
3. criar playbooks versionáveis
4. testar ponta a ponta no Telegram
