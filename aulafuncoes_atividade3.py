# Nova demonstração do uso de funções...

# Definindo o bloco de instruções!

def adicao(x, y):
    return x + y
def subtracao(x, y):
    return x - y
def multiplicacao(x, y):
    return x * y
def divisao(x, y):
    return x / y

# Inserindo dados para determinar a operação:

print("Digite dois valores de números inteiro: ")
n1 = int(input("x: "))
n2 = int(input("y: "))
op = input("Qual operação deseja realizar? (+, -, *, /)")

# Definindo o resultado da intrução:

if op == "+":
    z = adicao(n1, n2)
    print("O resultado da soma é: ", z)
elif op == "-":
    z = subtracao(n1, n2)
    print("O resultado da subtração é: ", z)
elif op == "*":
    z = multiplicacao(n1, n2)
    print("O resultado d multiplicação é: ", z)
elif op == "/":
    z = divisao(n1, n2)
    print("O resultado da divisão é: ", z)
else:
    print("Operação digitada inexistente!")