# Programa para converter a temperatura

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Bloco para Celsius
def converter_celsius():
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)
    print(f"{celsius}°C é igual a {fahrenheit}°F e {kelvin}K")

# Bloco para Fahrenheit
def converter_fahrenheit():
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = fahrenheit_to_kelvin(fahrenheit)
    print(f"{fahrenheit}°F é igual a {celsius}°C e {kelvin}K")

# Bloco para Kelvin
def converter_kelvin():
    kelvin = float(input("Digite a temperatura em Kelvin: "))
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = kelvin_to_fahrenheit(kelvin)
    print(f"{kelvin}K é igual a {celsius}°C e {fahrenheit}°F")

# Menu principal
def menu():
    print("Conversor de Temperatura")
    print("Escolha a unidade da temperatura que você deseja converter:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    
    opcao = int(input("Digite o número da opção (1/2/3): "))
    
    if opcao == 1:
        converter_celsius()
    elif opcao == 2:
        converter_fahrenheit()
    elif opcao == 3:
        converter_kelvin()
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

# Executa o menu
menu()
