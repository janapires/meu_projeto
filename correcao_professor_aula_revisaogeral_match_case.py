# Correção do professor da tarefa de consulta bancária, usando macth case...

print("Qual operção você deseja executar?")
print("1. Consultar saldo, 2. Realizar um depósito, 3. Realizar um saque")
operacao = int(input("Digite a opção desejada: "))
saldo = 0

# Executando o bloco de instruções, de acondo com a opção desejada!

match operacao:
    case 1:
        print(f"O saldo atual é: {saldo}")
    case 2: