# Matriz de Validacao

## Casos obrigatorios

### Identidade
- Pergunta: `qual e o seu nome?`
- Esperado: responder `BOBY`

### Tratamento
- Pergunta: `como deve me chamar?`
- Esperado: responder `MESTRE`

### Hora
- Pergunta: `me diga a hora exata de brasilia agora`
- Esperado: consultar comando local e responder hora atual de Brasilia

### Gmail
- Pergunta: `liste meus 5 emails nao lidos mais recentes`
- Esperado: usar comando local e trazer dados reais

### Drive
- Pergunta: `liste minhas 5 planilhas mais recentes do google drive`
- Esperado: listar arquivos reais do Drive

### Sheets
- Pergunta: `na planilha MARCOS, na aba ABRIL - 2026, liste apenas JUROS e NOME dos atrasados`
- Esperado: consultar a planilha real e devolver uma unica lista, sem repetir bloco

### Agenda
- Pergunta: `me mostre meus eventos de hoje na agenda`
- Esperado: usar agenda real de hoje

### Memoria
- Pergunta: `registre na memoria de hoje: teste validado`
- Esperado: gravar no arquivo diario e confirmar sem prometer em falso

## Regras de aprovacao
- Nao pode responder com tutorial se o dado local existir.
- Nao pode responder com frase generica de falha se o comando local funcionar.
- Nao pode repetir lista de planilha.
- Nao pode mostrar prefixos tecnicos ao usuario.

## Frequencia
- Revalidar apos mudancas em `BOOT.md`, `AGENTS.md`, `google_bridge.py` ou Telegram.
