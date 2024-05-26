import numpy as np

# Dados de Janeiro (Matriz 1)
janeiro = np.array([
    [40, 30, 45],  # Compartilhamentos
    [90, 95, 90],  # Visualizações
    [32, 3, 8],    # Curtidas
    [23, 33, 33]   # Comentários
])

# Dados de Fevereiro (Matriz 2)
fevereiro = np.array([
    [0, 35, 10],   # Compartilhamentos
    [1, 32, 30],   # Visualizações
    [1, 3, 0],     # Curtidas
    [0, 9, 9]      # Comentários
])

# Soma das Matrizes (Relatório Geral)
relatorio_geral = janeiro + fevereiro

# Apresentação do Relatório em Formato de Matriz
print("Relatório Geral de Engajamento (Janeiro + Fevereiro):")
print(relatorio_geral)
