# Demostrando como criar uma lista de tarefas...

# Definindo a exibição da lista de tarefas para o usuário...

def mostrarTarefas(tarefas):
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")

# Permitindo que o usuário adicione uma nova tarefa na lista...

def adicionarTarefa(tarefas):
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")
    mostrarTarefas(tarefas)  # Exibe a lista atualizada após adicionar a nova tarefa

# Permitindo que o uswuário remova da lista uma tarefa já concluída... 

def removerTarefa(tarefas):
    mostrarTarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa que deseja marcar como concluída: "))
        if 1 <= indice <= len(tarefas):
            tarefa = tarefas.pop(indice - 1)
            print(f"Tarefa '{tarefa}' concluída e removida da lista!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número.")

# Controle de fluxo principal do programa, permitindo que o usuário interaja com o sistema...

def main():
    tarefas = []
    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Concluir Tarefa")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionarTarefa(tarefas)
        elif opcao == '2':
            if tarefas:
                removerTarefa(tarefas)
            else:
                print("Nenhuma tarefa para concluir!")
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Garantindo que a função main seja executada

if __name__ == "__main__":
    main()
