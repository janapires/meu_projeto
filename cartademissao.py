# Inserção de informações em um documento

print("Digite o nome da empresa:")
NomeEmpresa = input()
print("Digite o nome do gestor:")
NomeGestor = input()
print("Digite o seu cargo:")
CargoFuncionario = input()
print("Digite a data de início do aviso prévio:")
InicioDataAviso = input()
print("Digite a data do fim do aviso prévio:")
FimDataAviso = input()
print("Digite o loca e a data de entrega da carta:")
DataEntregaCarta = input()
print("Linha para assinatura:")
LinhaAssinatura = (input("________________________________________"))
print("Digite o nome completo do funcionário:")
NomeCompletoFuncionario = input()

# Impressão da carta de demissão

print(f" À {NomeEmpresa},")
print(f"Prezado {NomeGestor}",)
print(f"Venho por meio desta carta comunicar o meu desligamento do cargo de {CargoFuncionario} . Estarei à disposição da empresa durante o aviso prévio, entre {InicioDataAviso} e {FimDataAviso}.")
print(f"{LinhaAssinatura}")
print(f"{NomeCompletoFuncionario}")

