# OpenClaw-Ops — regras específicas deste projeto

Esta pasta `.claude/` guarda as regras **só do OpenClaw-Ops**.
Elas ficam separadas das regras pessoais globais do Tom, que vivem em `~/.claude/CLAUDE.md`
e valem em qualquer projeto (por exemplo: responder sempre em português do Brasil, de forma simples).
Aqui só entra o que é específico deste projeto.

## Qual projeto é este
- Documentação da **operação do robô BOBY/OpenClaw**: políticas, rotinas (playbooks), prompts e espelho dos arquivos críticos da VPS.
- Repositório GitHub: `LELLYS10/OpenClaw-Ops` (**público** — nunca commitar senhas, chaves, tokens, IPs de acesso ou dados de clientes/sócios).
- Pasta de trabalho no Mac: `~/Documents/Desenvolvimento/GitHub/OpenClaw-Ops`.
- Estrutura: `docs/` (políticas e estado atual), `playbooks/` (rotinas), `prompts/` (regras curtas), `runtime/` (espelho da VPS), `obsidian/` (recorte do vault do BOBY). Comece por `README.md` e `docs/arquitetura-operacional.md`.
- Relacionado, mas outro projeto: `CENTRO_HERMES_OPENCLAW` (central de mapas). Não misturar arquivos dos dois.

## Situação em 2026-09-23
- Há notas novas do Obsidian ainda não commitadas em `obsidian/Boby - Memória Mestre/` (uma alterada, duas novas). Não foram mexidas.
- O `runtime/` é um espelho: a fonte de verdade dos arquivos é a VPS (`ssh vps`).

## Regras deste projeto
1. Nunca subir credenciais (o README já diz isso). Repositório público: conferir cada arquivo antes de commitar; nunca usar `git add -A` sem revisar o que entra.
2. Nunca alterar a VPS, o OpenClaw, os containers ou o PM2 sem autorização explícita do Tom para aquele passo; antes, backup e plano de volta.
3. Não misturar projetos CredPlus nem arquivos aleatórios aqui (o foco é só a operação e a qualidade do BOBY).
4. Não apagar nada sem pedir confirmação.
5. Ao mudar o `runtime/`, deixar claro que é cópia do que está na VPS, e não a versão viva.
