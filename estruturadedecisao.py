# Demonstra operadores lógicos num estrutura de decisão em condicionais

print("O que você vai fazer amanhã de manhã?")
print("dormir / estudar / planejar")
manha = input()
print("O que você vai fazer amanhã de tarde?")
print("jogar / treinar / trabalhar")
tarde = input()

if not manha or not tarde:
    print("Você precisa dizer o que vai fazer!")
else:
    if manha == "dormir" or tarde == "jogar":
        print("Você está desperdiçando o seu dia!")
    elif manha == "estudar" or tarde == "jogar":
        print("Que bom, você irá se aperfeiçoar!")
    elif manha == "planejar" and tarde == "trabalhar":
        print("Para trabalhar melhor, devo planejar!")
    else:
        print("Não combinmos nestas ações...")

print("Tenha um bom dia!")
          