# Programa para analisar a posição do jogador de futebol e informar informar uma mensagem

print("Digite a sua posição de jogador: ")
print("Goleiro")
print("Zagueiro")
print("Lateral")
print("Volante")
print("Meia")
print("Ponta")
print("Atacante")
print("Centroavante")
print("Outras posições")
posicao = input()

match posicao:
    case Goleiro:
        print("Defesa!")
    case Zagueiro:
        print("Defesa")
    case Lateral:
        print("Defesa")
    case Volante:
        print("Meio-campo!")
    case Meia:
        print("Meio-campo!")
    case Ponta:
        print("Ataque!")
    case Atacante:
        print("Ataque!")
    case Centroavante:
        print("Teimoso")
    case Outras posições:
        print("Teimoso")
    