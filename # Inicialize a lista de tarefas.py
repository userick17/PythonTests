# Inicialize a lista de tarefas
tarefas = []

# Função para adicionar uma tarefa à lista
def adicionar_tarefa():
    tarefa = input("Digite a tarefa que você deseja adicionar: ")
    tarefas.append({"tarefa": tarefa, "concluída": False})
    print("Tarefa adicionada com sucesso!")

# Função para exibir as tarefas na lista
def exibir_tarefas():
    print("\nTarefas:")
    for i, tarefa in enumerate(tarefas):
        status = "✔" if tarefa["concluída"] else " "
        print(f"{i+1}. [{status}] {tarefa['tarefa']}")

# Função para marcar uma tarefa como concluída
def marcar_como_concluida():
    exibir_tarefas()
    try:
        indice = int(input("Digite o número da tarefa que você concluiu: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluída"] = True
            print("Tarefa marcada como concluída.")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Loop principal
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar tarefa")
    print("2. Exibir tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Sair")
    
    opcao = input("Digite o número da opção: ")
    
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        exibir_tarefas()
    elif opcao == "3":
        marcar_como_concluida()
    elif opcao == "4":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
