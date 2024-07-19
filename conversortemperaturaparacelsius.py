
print("Qual temperatura que você deseja converter?")
escolha = float(input("Digite 1. Celsius / Digite 2. Kelvin / Digite 3. Fahrenheit"))
temperatura = float(input("Digite o valor da temperatura: "))

Celsius = Kelvin - 273.15
Celsius = (Fahrenheit - 32) / 1.8

print("Digite a temperatura a ser convertida: ")
print("Digite 1 para converter de Kelvin para Celsius")
print("Digite 2 para converter de Fahrenheit para Celsius")
temperatura = float(input())

match temperatura:
    case 1:
        print(f"A temperatura digitada é equivalete a {Celsius}")
    case 2:
        print(f"A temperatura digitada é equivalete a {Celsius}")

    