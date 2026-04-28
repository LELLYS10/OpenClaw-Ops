# Crash Recovery

## Objetivo
Restabelecer o BOBY quando ele sumir, responder genérico ou perder contexto.

## Checklist
1. Confirmar se o container do OpenClaw está ativo.
2. Ler `AGENTS.md`, `BOOT.md` e `MEMORY.md` do runtime atual.
3. Verificar se as integrações Google ainda respondem com comandos locais.
4. Confirmar se o gabarito comportamental continua aplicado.
5. Validar um pedido real curto antes de devolver o sistema como estável.

## Comandos úteis
- `docker ps`
- `docker logs --tail 200 openclaw-189p-openclaw-1`
- `python3 /data/.openclaw/workspace/google_bridge.py gmail-unread`
- `python3 /data/.openclaw/workspace/google_bridge.py sheets-list`
- `python3 /data/.openclaw/workspace/google_bridge.py calendar-today`

## Critério de sucesso
O BOBY precisa voltar a responder com dados reais, sem fallback genérico e sem esquecer o contexto principal do MESTRE.
