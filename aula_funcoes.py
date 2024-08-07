# Minha primeira tarefa de funções no Python

# Definindo os blocos da função!

def apresentar():
    print("Meu nome é: ", MyName, ".")
    print("Minha altura é: ", MyHeigh, "metros")
    print("Minha idade é: ", MyAge, "anos")
    return
def conferir(X):
    if X >=18:
        print("Você é maior de idade!")
    else:
        print("Ops, menor de idade não pode!")
    return

# Definindo os parâmetros e inserção de dados!

MyName = str(input("Digite o seu nome: "))
MyHeigh = float(input("Digite a sua altura: "))
MyAge = int(input("Digite a sua idade: "))

# Verificando os dados inseridos

apresentar()
conferir(MyAge)