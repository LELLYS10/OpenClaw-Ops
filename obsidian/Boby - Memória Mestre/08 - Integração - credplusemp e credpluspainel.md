# Integração - credplusemp e credpluspainel

## Objetivo
Registrar no hub do BOBY os dois domínios já existentes na VPS para futura integração operacional.

## Domínios
- `credplusemp.com.br`
- `credpluspainel.com`

## O que já foi identificado na VPS

### credpluspainel.com
- já está roteado no `Traefik`
- container principal: `credplus-app`
- stack local: `/docker/credplus-app`
- porta interna do app: `3000`
- tipo de app: `Next.js`
- comportamento HTTP observado: `307` redirecionando para `/login?redirect=%2F`
- regra atual do Traefik:
  - `credpluspainel.com`
  - `www.credpluspainel.com`
  - `credplus.srv1416255.hstgr.cloud`

### credplusemp.com.br
- existe configuração dedicada no `Traefik`
- arquivo localizado em:
  - `/docker/traefik-wvkg/dynamic/credplusemp.yml`
- backend real: `http://127.0.0.1:3000`
- runtime observado no host:
  - processo: `node /usr/bin/serve dist -l 3000 -s`
  - diretório: `/root/CredPlus1.0`
  - gerenciamento: `PM2`
- tipo de app: frontend estático servido a partir de `dist/`
- comportamento HTTP observado: `200 OK`

## Containers relevantes na VPS
- `credplus-app`
- `openclaw-189p-openclaw-1`
- `n8n-credplus-n8n-1`
- `traefik-wvkg-traefik-1`
- `evolution-api-evolution-1`

## Diretriz de integração com BOBY
- BOBY deve conhecer esses dois domínios como ativos da operação
- BOBY deve tratar `credpluspainel.com` como painel principal em `Next.js`, exposto pelo `Traefik`
- BOBY deve tratar `credplusemp.com.br` como frontend estático legado/operacional servido no host por `PM2`
- ambos devem entrar na memória operacional e no knowledge hub

## Próximos passos
1. abrir e documentar o conteúdo de `/docker/traefik-wvkg/dynamic/credplusemp.yml`
2. documentar a stack de `/docker/credplus-app`
3. documentar `/root/CredPlus1.0`
4. definir o papel de cada domínio no negócio
5. criar notas separadas por sistema se eles representarem produtos diferentes

---
Voltar para [[10 - Projetos/BOBY OpenClaw/Boby - Memória Mestre/00 - Index - Boby Memória Mestre|Índice]]
