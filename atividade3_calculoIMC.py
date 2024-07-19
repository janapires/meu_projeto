# Cálculo de IMC

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso * altura ** 2

print(f"O seu IMC é {imc}")
if imc > 25:
    print("Você está acima do peso!")
elif imc < 18:
    print("Você está abaixo do peso.")
else:
    print("O seu peso está ok!")
                                 