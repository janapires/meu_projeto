# Programa para converter temperaturas de Celsius para Kelvin e Fahrenheit, usando termos condicionais if, else, elif ou match case

Celsius = float(input("Digite a temperatura Celsius: "))
Kelvin = Celsius + 273.15
Fahrenheit = (9 / 5 * Celsius) - 32

print("Digite a temperatura Celsius a ser convertida: ")
print("Digite 1 para converter para Kelvin")
print("Digite 2 para converter para Fahrenheit")
temperatura = float(input())

match temperatura:
    case 1:
        print(f"A temperatura digitada é equivalete a {Kelvin}")
    case 2:
        print(f"A temperatura digitada é equivalete a {Fahrenheit}")


