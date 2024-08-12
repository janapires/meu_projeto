# Demonstrando o uso de novas funções para manipulação de dados em Python

# Inserindo os itens da lista...

numeros = [7, 2, 9, 6, 5, 0, 3, 8, 1, 4]
palavras = ["Olá", "Alô", "Hei", "Uau", "Ops"]

print("Quantas variáveis possuem: ")
print("Números: ", len(numeros))
print("Palavras: ", len(palavras))

print("Vamos reordenar essas listas?")
print(sorted(numeros))
print(sorted(palavras))

print("O somatório de números é: ", sum(numeros))
print("Qual é o maior valor dentre os números? ", max(numeros))
print("Qual é a primeira palavra da lista? ", min(palavras))