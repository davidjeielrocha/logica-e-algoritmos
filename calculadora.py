while True:
    try:
        e = float(input("Digite o valor à esquerda do operador: "))
        op = input("Digite o operador. Opções: (+, -, *, /): ")
        d = float(input("Digite o valor à direita do operador: "))

        op_validos = ["+", "-", "*", "/"]
        if op in op_validos:
            if op == "/" and d == 0:
                print("Divisão por zero! Tente novamente.")
                continue
            resultado = eval(f"{e} {op} {d}")  # Usando f-strings para formatação
            print(f"{e} {op} {d} = {resultado}")  # Usando f-strings para formatação
        else:
            print("Operador inválido! Tente novamente.")
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
