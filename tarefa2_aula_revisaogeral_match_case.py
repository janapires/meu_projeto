# Elaboração de um programa para cliente de uma conta bancária verificar se é possível sacar o saldo da conta bancária... 

# Definindo os dados para a instrução...

nomeCompleto = print("José dos Santos Aguiar")
dataNascimento = print("Data de nascimento: 27/06/1979")
documento = int(print("CPF: 096.868.654-74"))
valorLimiteSaque = int == 1_000.00
opcao = print("1. Consultar Saldo, 2. Realizar Depósito, 3. Realizar Saque ")

#Estrururando os blocos de instrução, usando match case para decisão...

match opcao:
    case 1:
        print("Seu saldo atual é: R$ 1.000,00 ")
    case 2:
        print("Qual é o valor que deseja depositar?")
    case 3:
        print("Você deseja sacar qual vaalor?")
    case _:
        print("Opcção inválida!")

print("Obrigada por escolher os nossos serviços!")

