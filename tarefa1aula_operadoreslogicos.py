# Construindo um programa papa caucular a média
# Solicita ao usuário que digite as duas notas

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média das notas
media = (nota1 + nota2) / 2

# Verifica a situação do aluno baseado na média
if media < 4:
    print("Aluno Reprovado")
elif media > 6:
    print("Aluno Aprovado Direto")
else:  # Se a média está entre 4 e 6
    print("Aluno em recuperação")
    
    # Solicita a nota da recuperação
    nota_recuperacao = float(input("Digite a nota da recuperação: "))
    
    # Verifica se o aluno foi aprovado ou reprovado na recuperação
    if nota_recuperacao < 5:
        print("Reprovado na recuperação")
    else:
        print("Aprovado na recuperação")
