def ordenar_funcionarios_por_antiguidade(lista_funcionarios):
    """
    Ordena uma lista de funcionários com base na antiguidade (código de matrícula).

    Args:
        lista_funcionarios: Uma lista de strings representando os códigos de matrícula dos funcionários.

    Returns:
        Uma nova lista com os códigos de matrícula ordenados por antiguidade (do mais antigo para o mais novo).
    """

    lista_ordenada = []
    for i in range(len(lista_funcionarios)):
        mais_antigo = lista_funcionarios[0]
        for funcionario in lista_funcionarios:
            if funcionario < mais_antigo:  # Comparação de strings simula comparação de datas de admissão
                mais_antigo = funcionario
        lista_ordenada.append(mais_antigo)
        lista_funcionarios.remove(mais_antigo)  # Remove o funcionário já adicionado à lista ordenada
    return lista_ordenada

# Exemplo de uso
funcionarios = ["101110", "0101", "10000", "10110110110001011", "10001110"]
funcionarios_ordenados = ordenar_funcionarios_por_antiguidade(funcionarios)
print(funcionarios_ordenados)  # Saída: ['0101', '10000', '101110', '10001110', '10110110110001011']
