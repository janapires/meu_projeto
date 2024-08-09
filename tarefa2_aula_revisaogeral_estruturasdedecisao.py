# Elaboração de um programa para cadastro de um novo cliente para uma conta bancária e verificando o saldo da conta bancária

# Definindo os dados para a instrução...

nomeCompleto = str(input("Digite o seu nome complteto: "))
dataNascimento = input("Digite a sua data de nacimento: ")
documento = int(input("Digite o seu CPF: "))
valorDepositado = float(input("Digite o valor a ser depositado pra a abertura da conta: "))
enderecoCompleto = input("Digite o seu endereço completo: ")

#Estrururando os blocos de instrução

if valorDepositado < 1000.00:
    print("Você precisa fazer um depósito nasua conta!")
elif valorDepositado >= 1_000.01 and valorDepositado <= 5_000.00:
    print("Você tem um vlor razoável em sua conta; cuidado para não gastar demais!")
else:
    print("Seu saldo está positivo!")

