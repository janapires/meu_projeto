# Tarefa da aula de funções; criando uma list de prugramação de acordo com a faixa etária... Ajeitar essa função.


def listar_programas_infantis(): 
    programas = [ 
    {"nome": "Peppa Pig", "ano": 2004}, 
    {"nome": "Mickey Mouse Clubhouse", "ano": 2006}, 
    {"nome": "Paw Patrol", "ano": 2013}, 
    {"nome": "Dora the Explorer", "ano": 2000}
    ] 
    print("Programas Infantis:") 

for programa in programas: 
    print(f"Nome: {programa['nome']}, Ano de Lançamento: {programa['ano']}") 

def listar_carros_e_precos(): 
    carros = [ 
    {"modelo": "Fusca", "preço": 20000}, 
    {"modelo": "Civic", "preço": 95000}, 
    {"modelo": "BMW X5", "preço": 350000}, 
    {"modelo": "Hilux", "preço": 130000} 
    ] 
    print("Carros e seus preços:") 

for carro in carros: 
    print(f"Modelo: {carro['modelo']}, Preço: R${carro['preço']:,}") 

def main(): 
idade = int(input("Digite a sua idade: ")) 

if idade < 18: 
    listar_programas_infantis() 
else: 
    listar_carros_e_precos() 

if __name__ == "__main__": 
    main() 