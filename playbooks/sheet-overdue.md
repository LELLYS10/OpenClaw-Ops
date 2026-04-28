# Sheet Overdue

## Objetivo
Consultar vencidos de uma planilha nomeada e devolver apenas os campos pedidos.

## Comando
`python3 /data/.openclaw/workspace/google_bridge.py sheet-overdue "NOME_DA_PLANILHA"`

## Resposta esperada
- `JUROS`
- `NOME`
- `DATA`

## Regra
Se houver dados suficientes no resultado local, nunca responder que não conseguiu acessar a planilha.
