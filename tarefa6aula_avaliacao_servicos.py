# Construindo um programa de avaliação de servicos prestados

# Solicitando os dados para o usuário!
execucao = input("O serviço foi realizado? (S / N) ")
avaliacao = int(input("Digite a nota para a avaliação? (1 / 5)"))

# Avaliando as informações, com base na opinião do usuário!
if execucao == "S" and avaliacao == 1:
    print("O serviço foi péssimo!")
elif execucao == "S" and avaliacao == 2:
    print("O serviço foi ruim!")
elif execucao == "S" and avaliacao == 3:
    print("O serviço foi razoável!")
elif execucao == "S" and avaliacao == 4:
    print("O serviço foi bom!")
elif execucao == "S" and avaliacao == 5:
    print("O serviço foi ótimo!")
else:
    if execucao == "N" and avaliacao == 0:
        reclamacao = input("Digite a sua reclamação! ")
    else:
        print("As avaliações não fazem sentido!")

