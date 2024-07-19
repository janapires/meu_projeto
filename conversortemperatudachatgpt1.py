# Construindo, com a ajuda do chat GPT, um conversor de temperatura cque converte de Celsius, para Fahrenheit e Kelvin e, assim, sucessivamente

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

def converter_temperatura():
    print("Conversor de Temperatura")
    print("Escolha a unidade da temperatura que você deseja converter:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    
    opcao = int(input("Digite o número da opção (1/2/3): "))
    temperatura = float(input("Digite a temperatura: "))
    
    if opcao == 1:  # Celsius
        fahrenheit = celsius_to_fahrenheit(temperatura)
        kelvin = celsius_to_kelvin(temperatura)
        print(f"{temperatura}°C é igual a {fahrenheit}°F e {kelvin}K")
    
    elif opcao == 2:  # Fahrenheit
        celsius = fahrenheit_to_celsius(temperatura)
        kelvin = fahrenheit_to_kelvin(temperatura)
        print(f"{temperatura}°F é igual a {celsius}°C e {kelvin}K")
    
    elif opcao == 3:  # Kelvin
        celsius = kelvin_to_celsius(temperatura)
        fahrenheit = kelvin_to_fahrenheit(temperatura)
        print(f"{temperatura}K é igual a {celsius}°C e {fahrenheit}°F")
    
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

# Executa o conversor
converter_temperatura()
