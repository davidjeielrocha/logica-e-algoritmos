nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso em Kg: '))
imc = peso / (altura * altura)

print("Nome\tAltura\tMassa\tIMC\n{}\t{}\t{}\t{:.2f}".format(nome, altura, peso, imc))