# Demonstração da utilização de funções...

# Definindo os parâmetros da função!

def menor():
	print("Eis os programas ideais para você: ")
	print("Teletubies, Tom & Jerry, Xou da Xuxa...")
	print("Se passar das 22h, vá dormir!")
	return
def maior():
	print("Eis boas opções de carros para comprar: ")
	print("Fiat 147, VW Fusca, Chevette...")
	print("Se beber não dirija!")
	return
	
# Inserindo os dados do usuário!

print("Digite a sua idade: ")
idade = int(input())

# Executando as intruções da função!

if idade < 18:
	menor()
else:
	maior()