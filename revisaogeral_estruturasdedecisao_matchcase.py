# Revisão as estrutura de Decisão match case

# Definição da inserção de dados para a análise...

print("O que você achou dos servições prestados?")
print("1. Péssimo, 1. Ruim, 3.Razoável, 4. Bom, 5. Ótimo")
avaliacao = int(input("Digite a opção para a sua avaliação: "))

# Estruturando o bloco de análise dos dados inseridos...

match avaliacao:
    case 1:
        print("O serviço precisa melhorar muito!")
        print("Avaliação: Reprovado")
    case 2:
        print("O serviço precisa melhorar em alguns quesitos!")
        print("Avaliação: Reprovado")
    case 3:
        print("O serviço foi regular")
        print("Avaliação: Recuperação")
    case 4:
        print("O serviço foi aceitável, embora possa melhorar!")
        print("Avaliação: Aprovado")
    case 5:
        print("O serviço foi perfeito! Parabéns!")
        print("Avaliação: Aprovado")
    case _:
        print("Opção digitada inválida!")


print("Obrigada pela sua avaliação!")