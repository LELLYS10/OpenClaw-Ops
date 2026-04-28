# BOBY - Prefixo fallback e lentidao

## Sintoma
- respostas apareciam com prefixo tecnico como `[fallback:Mistral]`
- identidade do bot ficava inconsistente
- respostas corretas, mas com latencia perceptivel

## Causa raiz
- havia fallback automatico de modelo no OpenClaw
- o runtime podia trocar de provider silenciosamente
- o contexto do agente estava grande demais para perguntas simples

## Correcao aplicada
- fallback automatico removido do `openclaw.json`
- regra adicionada no workspace para nunca exibir prefixos tecnicos ao usuario
- smoke test executado no agente com resposta limpa

## Validacao
- resposta validada sem prefixo tecnico
- identidade validada com tratamento `MESTRE`
- integracoes Google continuaram funcionais

## Proximo ajuste
- reduzir skills carregadas por padrao
- limpar plugin stale com warning no boot
- enxugar contexto base do workspace
