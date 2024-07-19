# Tarefa 2 de estruturas condicionais if/else/elif

print("Digite a ua idade: ")
idade = int(input())

if idade < 18:
    print("Você não é maior de idade")
    print("Não poderá realizar a operação!")

elif idade >= 65:
    print("Você ja etá pronto para se aposentar!")
    print("Poemos oferecer suporte técnico...")
    
else:
    print("Você é maior de idade,")
    print("Portanto poderá realizar operação!")

print("Obrigada por optar pelos nossos serviços!")