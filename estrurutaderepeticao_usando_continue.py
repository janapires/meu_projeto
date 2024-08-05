# Demonstração do uso de laços de repetição, usado continue

numero = 1
while numero >= 0:
    print("Digite um número negativo para sair: ")
    numero = int(input())
    break
    print("Este texto não será exibido! Mas...")
else:
    print("O número digitado foi: ", numero)