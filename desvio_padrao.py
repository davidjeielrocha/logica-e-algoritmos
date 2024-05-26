import numpy as np

# Dicionários para armazenar os valores de PV por SP e os resultados (média e desvio padrão)
pvs_por_sp = {}
resultados = {}

# Exemplo de dados (substitua com seus dados reais)
dados = [(25, 24.8), (25, 25.2), (30, 29.5), (30, 30.1), (25, 24.9)]

# Agrupando valores de PV por SP
for sp, pv in dados:
    if sp in pvs_por_sp:
        pvs_por_sp[sp].append(pv)
    else:
        pvs_por_sp[sp] = [pv]

# Calculando média e desvio padrão para cada SP
for sp, pvs in pvs_por_sp.items():
    media = np.mean(pvs)
    desvio_padrao = np.std(pvs)
    resultados[sp] = {'media': media, 'desvio_padrao': desvio_padrao}

# Imprimindo os resultados
for sp, resultado in resultados.items():
    print(f'SP: {sp}')
    print(f'  Média: {resultado["media"]:.2f}')
    print(f'  Desvio Padrão: {resultado["desvio_padrao"]:.2f}')
