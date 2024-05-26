nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

def calcula_media_aluno(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

media_geral = calcula_media_aluno(nota1, nota2, nota3)
print("A média do aluno é: ", media_geral)

def verifica_aprovacao(media_geral):
    if media_geral >= 7 and media_geral <= 8:
        print("Aprovado pela média mínima")
    elif media_geral >= 9:
        print("Parabéns pela aprovação, boas férias")
    elif media_geral >= 2 and media_geral <= 6:
        print("Não foi dessa vez mas você poderá fazer a prova substitutiva")
    elif media_geral < 2:
        print("Desculpe, você está reprovado")

verifica_aprovacao(media_geral)