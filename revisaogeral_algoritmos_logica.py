# Revisão geral das aulas de algoritmos e lógica de progrmação dados até o momento...

# Definindo os dados da instrução...

nome = "Ednei"
idade = 18
altura = 1.67

# Executando os bloco de instrução...

print("Meu nome é: ", nome, "E a minha idade é: ", idade) # Bloco de instrução que era usado anteriormente
print(f"Meu nome é {nome} e a minha idade é {idade}") # Bloco de intruçõ usdo atualmente, que visa facilitar a execução de dados
print("Não vou dizer a minha idade!") # Bloco de intrução para exemplificar o uso de aspas simples

########### Novo exemplo ##############

print("Digite o seu nome: ")
nome = input()
print("Digite a sua idade: ")
idade = input()
print("Digite a sua altura: ")
altura = input()

print(type(idade))

############### Novo Exemplo ################

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura: "))

print(f"Meu nime é: {nome}")
print(f"A minha idade é: {idade}")
print(f"A minha altura é: {altura}")

print(type(nome))
print(type(idade))
print(type(altura))

############# Novo exemplo - Calculando a idade futura.....

print("QUal será a minha idade em 2036?")
tempo = 2036 - 2024
idade = idade + tempo
print(" A minha idade em 2036 será: ", idade)

############# Novo exemplo - Calculando a metade da altura....

altura = altura / 2
print("A metade da minh altura é: ", altura)
