#  Demonstrando o uso das funções junto com as listas 

# Inserindo os dados da lista dos sonhos...

print("Eis os meus maiores sonhos...")
sonhos = ["1. Me divertir na Disney",
          "2. Me banhar na praia de Sepetiba",
          "3. Tirar féria em Paris",
          "4. Fazer compras no West Shopping",
          "5. Visitar as pirâmides do Egito"]
for x in sonhos:
    print(x)

print("Ops, não quero Sepetiba!")
del(sonhos[1]) # Quando a função delete excluiu o item na posição "1", a lista reduziu de tamanho, ficando apenas com 4 itens e, por isso...
print("E nem West Shopping...")
del(sonhos[3]) # esse item precisava ser alterado antes de colocar o programa para rodar, pois só assim iria excluir o item relacionad às compras no west shopping

print("Conferindo a lista de sonhos...")
for x in sonhos:
    print(x)