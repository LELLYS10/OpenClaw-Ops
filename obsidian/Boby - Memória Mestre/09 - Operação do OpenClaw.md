# Operação do OpenClaw

## Objetivo
Definir a estrutura operacional mínima para o BOBY/OpenClaw funcionar com consistência.

## Núcleos
### 1. Workspace ativo
- `/data/.openclaw/workspace`
- regras do agente
- scripts críticos
- memória diária local

### 2. Knowledge hub
- `/data/.openclaw/knowledge-hub/boby-openclaw`
- memória estrutural
- checklists
- projetos
- pessoas
- sistemas

### 3. Sync remoto
- origem: `GitHub`
- destino: espelho local na VPS
- rotina: `sync_boby_hub.sh`

## Regras operacionais
- resposta crítica deve consultar fonte real
- memória importante deve virar arquivo
- sistema novo deve ser documentado antes de automação
- integração nova deve ter checklist próprio

## Áreas obrigatórias
- `daily/`
- `projects/`
- `people/`
- `checklists/`
- `systems/`

## Próximos blocos de estrutura
1. checklist de boot
2. checklist de revisão diária
3. projeto mestre do BOBY/OpenClaw
4. nota de sistemas ativos

---
Voltar para [[10 - Projetos/BOBY OpenClaw/Boby - Memória Mestre/00 - Index - Boby Memória Mestre|Índice]]
