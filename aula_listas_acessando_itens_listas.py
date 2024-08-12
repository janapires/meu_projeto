# Demostrando como acessar um elemento dentro de uma lista

# Declarando a lista e inserindo os alertas

print("Vou montar uma marmita com cinco elementos!")
marmita = ["feijão", "arroz", "legumes", "salada", "carne"]
print("Eis a nossa recomendação: ", marmita)

resposta = input("Você quer montar ua marmita diferente? (S/N)")
if resposta == "S":
    for x in range(0, 5):
        print(f'Digite o {x+1}º item do cardápio:')
        marmita[x] = input()
    print("A marmita montada foi: ", marmita)
    print("Os três primeiros itens foram: ", marmita[0:3])
    print("O último item da marmita foi: ", marmita[-1])
else:
    print("Ok, você decide!")
