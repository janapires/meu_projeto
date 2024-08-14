# Novo exemplo de como utilizar as matrizes em listas...

# Inserindo os dados da matriz...

print("Eis a tabela numerica original: ")
tabuada = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Definindo a instrução...

multiplicar = int(input("Digite o multiplicador: "))

# Criando o bloco de instrução de acordo com os dados inseridos pelo usuário...

for x in range(0, 3):
    for y in range(0, 3):
        tabuada[x][y] = tabuada[x][y] * multiplicar

# Exibindo o resultado da instrução...

print("Eis o multiplicador: ", multiplicar)
print("Confira o resultado das oprações: ")
for resultado in tabuada:
    print(resultado)