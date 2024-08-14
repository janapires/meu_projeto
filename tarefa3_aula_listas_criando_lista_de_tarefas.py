# Tarefa da aula de lista, métodos e funções

# Declarando a lista de tarefas... 

print("Eis a minha lista de tarefas do dia: ")
listaTarefas = ["1. Arrumar casa",
                "2. Ir às compras",
                "3. Fazer almoço",
                "4. Passear com o cachorro",
                "5. Tirar o lixo"]

# Definindo a execução da lista de tarefas..

print(" Você já realizou a sua primeira tarefa hoje? (S/N)")
resposta = input()
print(listaTarefas)

# Determinando as ações de acordo com os dados inseridos pelo usuário...

resposta = input("QUal item da sua lista de tarefas você realizou?")
if resposta == "S":
    for item in listaTarefas(0, 4):
        item.remove[item]
        print("Deseja passar para o próximo item? (S/N)")
        print(listaTarefas) == resposta(input())
        if resposta == "S":
            item.remove[item]
        else:
            print("Ok, você foi bem hoje, pode descansar!")
elif resposta == "N":
            input("Deseja realizar alguma tarefa hoje:")
    if resposta == "S":
            print(listaTarefas)
    else:
            print("Ok, mas você não fez nada de útil hoje!")

else:
    print("Você precisa realizar as suas tarefas!")