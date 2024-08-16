# Correção da tarefa cardápio de refeições... 

print("Vamos montar um cardápio personalizado?")

# Definindo as listas...

menuCafe = []
menuAlmoco = []
menuJantar = []

# Inserindo o blocos de instrução, de acordo com os ddos do usuário...

for x in range(0, 3):
    opcao = input(f'Digite a {x+1} opção: ')
    menuCafe.append(opcao)
    if opcao == "leite" or opcao == "queijo" or opcao == "pão":
        print("Alimento não recomendado!")
print("Eis as opções escolhidas: ", menuCafe)

for x in range(0, 4):
    opcao = input(f'Digite a opção {x+1}: ')
    menuAlmoco.append(opcao)
    if opcao == "camarão" or opcao == "pimenta":
        print("Alimento não recomendado!")
print("Eis as opções escolhidas: ", menuAlmoco)

for x in range(0, 4):
    opcao = input(f'Digite a opção {x+1}: ')
    menuJantar.append(opcao)
    if opcao == "camarão" or opcao == "pimenta":
        print("Alimento não recomendado!")
print("Eis as opções escolhidas: ", menuJantar)