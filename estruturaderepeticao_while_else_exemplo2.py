# Demonstração do uso do while/else, uando o break para interromper a instrução

contador = 0; senha = ""
while senha != "S3nh4":
    print("Digite a sua senha: ")
    senha = input()

    if senha == "S3nh4":
        print("Senha correta!")
        break
    else:
        print("Senha incorreta!")

    contador = contador + 1
    if contador == 3:
        print("Tentativas excedidas!")
        break