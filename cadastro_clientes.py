def cadastrar_cliente():
    """Cadastra um novo cliente no arquivo 'clientes.txt'."""

    nome = input("Nome completo: ")
    telefone = input("Telefone: ")
    idade = input("Idade: ")

    with open("clientes.txt", "a") as arquivo:
        arquivo.write(f"{nome},{telefone},{idade}\n")

    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    """Lista todos os clientes cadastrados no arquivo 'clientes.txt'."""

    try:
        with open("clientes.txt", "r") as arquivo:
            for linha in arquivo:
                nome, telefone, idade = linha.strip().split(",")
                print(f"Nome: {nome}, Telefone: {telefone}, Idade: {idade}")
    except FileNotFoundError:
        print("Nenhum cliente cadastrado ainda.")

def menu():
    """Exibe o menu interativo e gerencia as opções do usuário."""

    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
