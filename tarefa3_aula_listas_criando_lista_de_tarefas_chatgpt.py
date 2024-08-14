# Criando uma lista de tarefas para o usuário... 

def exibir_tarefas(tarefas, titulo):
    """Exibe a lista de tarefas com um título."""
    print(f"\n{titulo}:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")

def adicionar_tarefa(tarefas):
    """Adiciona uma nova tarefa à lista."""
    nova_tarefa = input("\nDigite a nova tarefa: ")
    tarefas.append(nova_tarefa)
    print("Nova tarefa adicionada!")

def selecionar_tarefa(tarefas):
    """Permite ao usuário selecionar uma tarefa concluída da lista."""
    while True:
        exibir_tarefas(tarefas, "Tarefas disponíveis")
        try:
            escolha = int(input("\nDigite o número da tarefa que você concluiu (ou 0 para sair): "))
            if escolha == 0:
                return None
            if 1 <= escolha <= len(tarefas):
                return escolha
            else:
                print("Escolha inválida, tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

def main():
    """Função principal para gerenciar o menu e a execução das tarefas."""
    tarefas_existentes = [
        "Ler um livro",
        "Fazer exercícios",
        "Escrever um artigo",
        "Cozinhar uma refeição",
        "Organizar a casa"
    ]
    tarefas_adicionadas = []
    tarefas_realizadas = []

    while True:
        print("\n--- Menu ---")
        print("1. Selecionar tarefa concluída")
        print("2. Adicionar nova tarefa")
        print("3. Sair")

        opcao = input("\nEscolha uma opção (1/2/3): ")

        if opcao == "1":
            todas_tarefas = tarefas_existentes + tarefas_adicionadas
            tarefa_concluida = selecionar_tarefa(todas_tarefas)
            if tarefa_concluida is not None:
                tarefa = todas_tarefas[tarefa_concluida - 1]
                tarefas_realizadas.append(tarefa)
                print(f"Tarefa '{tarefa}' concluída!")
        elif opcao == "2":
            adicionar_tarefa(tarefas_adicionadas)
        elif opcao == "3":
            break
        else:
            print("Opção inválida, tente novamente.")

    if tarefas_realizadas:
        print("\nVocê concluiu as seguintes tarefas hoje:")
        for tarefa in tarefas_realizadas:
            print(f"- {tarefa}")
    else:
        print("\nVocê não fez nada de útil no seu dia.")

if __name__ == "__main__":
    main()