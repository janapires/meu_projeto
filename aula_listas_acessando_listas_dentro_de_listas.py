# Demonstração do comportamento de listas 

# Definindo os dados para inserir itens...

print("Vou almoçar em um restaurante a quilo!")

# Definindo os itens da lista 

original = ["arroz", "feijão", "batata", "alface", "frango"]
print("Eis o meu cardápio: ", original)
derivada = original
print("Meu amigo também irá comer: ", derivada)

# Manipulando os itens dentro da lista!

print("Vou alterar as opções sem ele ver...")
original.remove("arroz")
original.remove("feijão")
original.remove("alface")
original.append("picanha")
original.append("linguiça")

# Exibindo a lista com as suas alterações

print("Amiguinho, me mostre o que você vai comer!")
print("Claro, dá uma conferida: ", derivada) # A lista derivada assumiu o mesmo espaço na memória da lista original 
# e exibiu os itens que foram modificados
