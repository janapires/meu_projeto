# Tarefa da última aula de algoritmos e lógica...

# Criando um cardápio para o usuário com listas de opções e possibilidade de adicionar itens no cardápio...

menuCafe = ["1. Café com leite, pão na chapa, maçã vermlha",
            "2. Chá de erva-doce, bolo de banana. mamão papaya",
            "3. Café puro, misto quente, uva verde"]

menuAlmoco = ["1. Arroz, feijão preto, bife, batata frita, pudim",
              "2. Arroz, feijão mulatinho, frango grelhado, purê de batata, doce de abóbora",
              "3. Arroz, estrogonofe de carne, batata frita, goiabada",
              "4. Arroz à piamontese, escalopinho ao molho mandeira, batata palha, doce de leite"]

menuJantar = ["1. Arroz, estrogonofe de frango, batata palha, salada verde, maçã verde",
              "2. Arroz, salada de legumes, carne moída, salada ceasar, uva verde",
              "3. Sopa de legumes com carne vermelha, torradas, melão amarelo",
              "4. Caldo verde com linguiça e bacon, mamão formosa"]

# Definindo os blocos de instrução, informando as opções de menu para o usuário...

while True:
     escolhaOpcao = input("n/Deseja alterar algum item da lista? (S/N)").upper()

# Definindo os blocos de instrução, informando as opções de menu para o usuário...
    
    if escolhaOpcao == "S":
        input("Digite a refeição: (menuCafe, menuAlmoco, menuJantar): ")

# Terminar a tarefa, rever funções e métodos...
