# Segunda demonstrçõ de como funciona o uso das matrizes em Python...

# Definindo as atribuiçoes da lista...

print("Eis o teclado numérico do terminal: ")
teclado = [["1", "2", "3"],
            ["4", "5", "6"],
           ["7", "8", "9"],
           ["*", "0", "#"] # Inserindo novas variáveis na lista
           ]
senha = []

# Criando as instruções de acordo com os dados do usuário...

print("Digite a sua senha de 4 digitos: ")
for x in range(0, 4):
    senha.append(input(f'Digite o dígito {x+1}: ')) # Retirando o int para evitar erros e o programa reconhecer uma senha alfanumérica

# Criando um bloco de verificação dos dados digitados...

for x in range(0, 4): # Alterando o número de linhas, pois foi inserida uma nova linha na tabela
    for y in range(0, 3): # O número de colunas não teve nenhuma alteração
        for z in range(0, 4):
            if teclado[x][y] == senha[z]:
                teclado[x][y] = "x" # Alterando par uma variável alfanumérica...

# Retorno da mensagem dada aos usuário, de acordo com os ddos inseridos...
                
print("Eis a senha digitada: ", senha)
print("Confira as teclas acionadas: ")
for listas in teclado:
    print(listas)