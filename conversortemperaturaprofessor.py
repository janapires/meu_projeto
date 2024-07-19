# Modelo de conversor de temperatura do professor

print("Qual temperatura que você deseja converter?")
escolha = float(input("Digite 1. Celsius / Digite 2. Kelvin / Digite 3. Fahrenheit"))
temperatura = float(input("Digite o valor da temperatura: "))

match escolha:
    case 1:
        Kelvin = temperatura + 273.15
        Fahrenheit = (9 / 5 * temperatura) -32
        print(f"A conversão de Celsius para Kelvin será {Kelvin}")
        print(f"A conversão de Celsius para Fahrenheit será {Fahrenheit}")
    case 2:
        Celsius = temperatura - 273.15
        Fahrenheit = 1.8 * (temperatura - 273) + 32
        print(f"A conversão de Kelvin para Celsius será {Celsius}")
        print(f"A conversão de Kelvin para Fahrenheit será {Fahrenheit}")
    case 1:
        Celsius = 5 / 9 * (temperatura - 32)
        Kelvin = (temperatura - 32) / 1.8 + 273.15
        print(f"A conversão de Farenheit para Celsius será {Celsius}")
        print(f"A conversão de Fahrenheit para Kelvin será {Kelvin}")