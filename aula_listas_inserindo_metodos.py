# Demomonstração de métodos em listas 

# Inserindo os dados da lista

inss = ["Maria", "Manoel", "José", "Isabela"]
print("Eis a fila do INSS", inss)

novo = input("Insira mais uma pessoa: ") # Adicionando novo item na lista
inss.append(novo) # Insere item no topo da lista
print("Conferindo a nova lista", inss)

print("Vou tirar a últimna pessoa desta lista...")
especial = inss.pop() # Remove um variável de um alista com base na posuição definida, como neste caso não etá definida, aqui ela removeu o último item da lista

print("Agora vou colocá-la na frente de todos os outros!")
inss.insert(0, especial) # Insere um item na lista, numa determinada posição, neste caso, a variável inserida será a primeira da lista
print("Conferindo de novo a lista: ", inss)

print("Maria não gostou e reclamou!")
inss.remove("Maria") # Aqui o item "maria foi removido, pois o método remove ums variável de aordo com  o seu valor"
print("E agora, ela saiu 'pé de vida'", inss)

print("Para não ter mais reclamações, vamos atender...")
inss.sort() # Sort é um método que ordena as variáveis, no caso de nomes, em ordem alfabética, alterando o conteúdo da lista
print("... em ordem alfabética: ", inss)

print("Onde está a nova lista de chamada pessoal", especial, "?")
print("Ela agora ficou na posição", inss.index(especial)+1 , "!") # O index informa a posição de uma variável em uma lista