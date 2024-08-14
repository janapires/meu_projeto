# Demonstração de como funciona uma matriz em Python...

# Definindo a matriz da instrução...

tabuada = []

# Definindo coo será utilizada a matriz

for x in range (0, 10):
    linhas = []
    for y in range (0, 10):
        linhas.append(x * y)
    tabuada.append(linhas)
 
for tabela in tabuada:
    print(tabela)