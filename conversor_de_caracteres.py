def converter_caractere():
    """
    Recebe um caractere digitado pelo usuário, converte e exibe seus valores em Decimal, Hexadecimal e Binário.
    """

    caractere = input("Digite um caractere: ")

    # Verifica se o usuário digitou mais de um caractere
    if len(caractere) > 1:
        print("Por favor, digite apenas um caractere.")
        return

    # Converte para Decimal (código Unicode)
    decimal = ord(caractere)

    # Converte para Hexadecimal
    hexadecimal = hex(decimal)

    # Converte para Binário
    binario = bin(decimal)

    print(f"Decimal: {decimal}")
    print(f"Hexadecimal: {hexadecimal}")
    print(f"Binário: {binario}")


# Chama a função para iniciar o programa
converter_caractere()
