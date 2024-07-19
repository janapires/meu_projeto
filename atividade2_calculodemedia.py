# Programa para calcular a média de um aluno e verificar se ele foi aprovado, etá em recuperação ou reprovado

nota1 = float(input('valor da nota 1'))
nota2 = float(input('valor da nota 2'))
nota3 = float(input('valor da nota 3'))
nota4 = float(input('valor da nota 4'))
soma = nota1 + nota2 + nota3 + nota4
media = soma / 4

print("Digite a primeira nota: ")
nota1 = float(input())
print("Digite a segunda nota: ")
nota2 = float(input())
print("Digite a terceira nota: ")
nota3 = float(input())
print("Digite a quarta nota: ")
nota4 = float(input())




print("Boas festas!")

if media <= 7.5:
        print("Você está aprovado!")
    elif media 6.0 or 7.5:
        print("Você está de recuperação!")
    else media < 6.0:
    print("Você foi reprovado!")