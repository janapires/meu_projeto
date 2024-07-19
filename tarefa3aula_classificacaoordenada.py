# Solicita ao usuário que digite os três números distintos

X = float(input("Digite o primeiro número (X): "))
Y = float(input("Digite o segundo número (Y): "))
Z = float(input("Digite o terceiro número (Z): "))

# Verifica se os números estão em ordem crescente
if X < Y < Z:
    print("Os números estão em ordem crescente!")
    
# Verifica se os números estão em ordem decrescente
elif X > Y > Z:
    print("Os números estão em ordem decrescente!")
else:
    print("Os números estão fora de ordem!")
