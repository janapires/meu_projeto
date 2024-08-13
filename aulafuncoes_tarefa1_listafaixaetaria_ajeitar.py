# Tarefa da aula de funções; criando uma lista de acordo com a faixa etária...

# Definindo os intens da lista/objeto...

def listar_programas_infantis():
    programas = [
        {"nome": "Peppa Pig", "ano": 2004},
        {"nome": "Mickey Mouse Clubhouse", "ano": 2006},
        {"nome": "Paw Patrol", "ano": 2013},
        {"nome": "Dora the Explorer", "ano": 2000}
    ]
    print("Programas Infantis:")
    for programa in programas:
        print(f"Nome: {programa['nome']}, Ano de lançamento: {programa['ano']}")
        
def listar_carros_e_precos():
    carros = [
        {"modelo": "Fusca", "preço": 2_000.00},
        {"modelo": "Civic", "preço": 5_000.00},
        {"modelo": "BMW X5", "preço": 35_000.00},
        {"modelo": "Hilux", "preço": 80_000.00}
    ]
    print("Carros e seus preços:")
    for carro in carros:
        print(f"Modelo: {carro['modelo']}, Preço: R${carro['preço']: }")

# Solicitando os dados do usuásrio, para definir o que será exibido...

def main():
    idade = int(input("Digite a sua idade: "))

# Definindo o que será exibido ao usuário de acordo com a sua faixa etária do usuário...

    if idade < 18:
        listar_programas_infantis()
    else:
        listar_carros_e_precos()

if __name__ == "__main__":
    main()