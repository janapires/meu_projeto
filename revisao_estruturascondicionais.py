# Revisão de estruturas condicionais...

# Definindo os dados para a instrução ...

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura: "))

# Definindo as estruções, utilizando estruturas condicionais...

if idade < 18:
    print("Você é menor de idade!")
elif idade >= 18:
    print("Você é maior de idade!")
elif idade >= 65:
    print("Você deveria se aposentar!")
else:
    print("Nada mais a se fazer...")

# Inserindo a condicional "and" para analisar várias instruções num mesmo bloco...
    
if idade < 18:
    print("Você é menor de idade!")
elif idade >= 18 and idade < 65:
    print("Você é maior de idade!")
elif idade >= 65:
    print("Você deveria se aposentar!")
else:
    print("Nada mais a se fazer...")

# Melhorando a estrutura lógica da instrução com as condicionais, simplificando o bloco de instrução...
    
if idade < 18:
    print("Você é menor de idade!")
elif idade >= 18 and idade < 65:
    print("Você é maior de idade!")
else:
    print("Você deveria se aposentar!")
