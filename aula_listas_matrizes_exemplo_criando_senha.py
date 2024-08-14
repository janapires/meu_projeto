# Segunda demonstrçõ de como funciona o uso das matrizes em Python...

# Definindo as atribuiçoes da lista...

print("Eis o teclado numérico do terminal: ")
teclado = [[1, 2, 3],
           [4, 5, 6,],
           [7, 8, 9]]
senha = []

# Criando as instruções de acordo com os dados do usuário...

print("Digite a sua senha de 4 digitos: ")
for x in range(0, 4):
    senha.append(int(input(f'Digite o dígito {x+1}: ')))

# Criando um bloco de verificação dos dados digitados...

for x in range(0, 3):
    for y in range(0, 3):
        for z in range(0, 4):
            if teclado[x][y] == senha[z]:
                teclado[x][y] = 0

# Retorno da mensagem dada aos usuário, de acordo com os ddos inseridos...
                
print("Eis a senha digitada: ", senha)
print("Confira as teclas acionadas: ")
for listas in teclado:
    print(listas)