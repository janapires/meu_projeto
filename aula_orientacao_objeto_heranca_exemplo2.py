# Demonstração de orientaçõ a objetos em Python...

class cliente:
    def __init__(self, titular, conta, saldo):
        self.titular = titular
        self.conta = conta
        self.saldo = saldo

class cliente_fisico(cliente):
    def apresentar(self):
        print("Olá, eu sou: ", self.titular)
        print("Minha conta é: ", self.conta)
        print("e quero saber o meu salo: ")
        return
    
# Para criar uma instância baseada na classe cliente...

fulano = cliente("João", "423.0502205-21", 25000.00)

# Acessando os atributo da instâncias cridas... 

print("De fato, você realmente é: ", fulano.titular)
print("No momento a sua conta possui R$ ", fulano.saldo)