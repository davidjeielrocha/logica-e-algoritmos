def calcular_custos(professor):
    """Calcula os custos semanais e mensais de um professor."""
    professor["carga_horaria_semanal"] = professor["carga_horaria_diaria"] * professor["dias_por_semana"]
    professor["custo_semanal"] = professor["carga_horaria_semanal"] * professor["valor_hora"]
    professor["custo_mensal"] = professor["custo_semanal"] * professor["dias_por_mes"]

professores = []

while True:
    nome = input("Nome do professor (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break

    professor = {
        "nome": nome,
        "endereco": input("Endereço: "),
        "data_admissao": input("Data de admissão (DD/MM/AAAA): "),
        "area_de_atuacao": input("Área de atuação: "),
        "carga_horaria_diaria": float(input("Carga horária diária: ")),
        "valor_hora": float(input("Valor da hora: ")),
        "dias_por_semana": float(input("Dias trabalhados por semana: ")),
        "dias_por_mes": float(input("Dias trabalhados por mês (aproximadamente): "))
    }

    calcular_custos(professor)
    professores.append(professor)

print("\nDados dos professores:")
for professor in professores:
    for chave, valor in professor.items():
        print(f"{chave.capitalize()}: {valor}")
    print("-" * 20)
