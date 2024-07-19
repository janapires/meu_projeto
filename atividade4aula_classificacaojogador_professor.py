# Programa para analisar a posição do jogador e exibir uma mensagem

posicao = input("Digite a posição em que joga: ")

if posicao == "goleiro" or posicao == "zagueiro" or posicao == "lateral":
    print("Você joga na defesa!")
elif posicao == "volante" or posicao "meia":
    print("Você joga no meio-campo!")
elif posicao == "ponta" or posicao "atacante" or posicao == "centroavante":
    print("Você joga no ataque!")
else:
    print("Você joga de teimoso!")