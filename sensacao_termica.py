temperatura = float(input("Digite a temperatura atual em graus Celsius: "))

if temperatura < 7:
    print("Congelando!")
elif temperatura < 10:
    print("Frio!")
elif temperatura < 26:
    print("Ótimo!")
else:
    print("Muito quente!")
