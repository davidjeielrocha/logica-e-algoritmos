import csv

# 1. Ler dados dos vendedores
dados_vendedores = {}
with open("dados_vendedores.csv", "r") as arquivo_vendedores:
    leitor_csv = csv.reader(arquivo_vendedores)
    next(leitor_csv)  # Pular cabeçalho
    for linha in leitor_csv:
        codigo, nome = linha
        dados_vendedores[codigo] = nome

# 2. Ler dados das vendas
vendas_vendedores = {}
with open("vendas_vendedores.csv", "r") as arquivo_vendas:
    leitor_csv = csv.reader(arquivo_vendas)
    next(leitor_csv)  # Pular cabeçalho
    for linha in leitor_csv:
        codigo, valor_venda = linha
        vendas_vendedores.setdefault(codigo, []).append(float(valor_venda))

# 3. Calcular pagamentos
pagamentos = {codigo: 0 for codigo in vendas_vendedores}
for codigo, vendas in vendas_vendedores.items():
    total_vendas = sum(vendas)
    comissao = total_vendas * 0.05
    pagamentos[codigo] += comissao

# 5. Exibir pagamentos
for codigo, valor in pagamentos.items():
    nome = dados_vendedores[codigo]
    print(f"{nome}: R$ {valor:.2f}")

# 6. Preparar dados para CSV
dados_csv = [["Código do Vendedor", "Valor a ser Pago"]]
for codigo, valor in pagamentos.items():
    dados_csv.append([codigo, valor])

# 8. Gravar dados em CSV
with open("pagamentos_vendedores.csv", "w", newline="") as arquivo_pagamentos:
    escritor_csv = csv.writer(arquivo_pagamentos)
    escritor_csv.writerows(dados_csv)

# 9. Mensagem de sucesso
print("Arquivo 'pagamentos_vendedores.csv' gerado com sucesso!")
