'''Você foi contratado para desenvolver um pequeno sistema que ajude uma família a 
controlar seus gastos mensais. O programa deve permitir registrar novas despesas, 
visualizar todas as despesas já registradas e calcular tanto o total gasto quanto a 
média dos valores das despesas. Além disso, o programa deve guardar o nome de 
cada despesa e ser capaz de mostrar qual foi a maior e qual foi a menor despesa 
registrada.
Para isso, utilize duas listas globais separadas:
Uma lista para armazenar os nomes das despesas e outra lista para armazenar os 
valores correspondentes.
As duas listas devem ter o mesmo tamanho e os elementos devem estar na 
mesma ordem — ou seja, o nome da despesa na posição i corresponde ao valor 
na posição i da lista de valores.
Implemente funções sem parâmetros que realizem as seguintes tarefas:
adicionar_gasto() → solicita ao usuário o nome da despesa e o valor, e adiciona 
ambos às listas globais correspondentes.
mostrar_gastos() → exibe todas as despesas cadastradas, mostrando o nome e o 
valor de cada uma.
calcular_total() → soma todos os valores e mostra o total gasto.
calcular_media() → calcula e mostra a média dos valores registrados.
mostrar_extremos() → mostra qual foi a maior despesa e qual foi a menor despesa, 
informando seus respectivos nomes.'''

''' Crie um programa com funções que registram despesas, mostram todas as 
despesas e calculam o total e a média, usando uma lista global, sem passar 
parâmetros.
cadastrar_despesa() → pede ao usuário o valor de uma despesa e guarda em uma 
lista global.
mostrar_despesas() → mostra todas as despesas cadastradas.
calcular_total() → soma todas as despesas da lista global e imprime o resultado.
calcular_media() → calcula a média das despesas da lista global e imprime.'''

# Listas globais
nomes_despesas = []
valores_despesas = []

def adicionar_gasto():
    """Solicita nome e valor da despesa e adiciona às listas globais."""
    nome = input("Digite o nome da despesa: ")
    try:
        valor = float(input("Digite o valor da despesa: R$ "))
        nomes_despesas.append(nome)
        valores_despesas.append(valor)
        print("Despesa adicionada com sucesso!\n")
    except ValueError:
        print("Valor inválido! Tente novamente.\n")

def mostrar_gastos():
    """Mostra todas as despesas cadastradas."""
    if not nomes_despesas:
        print("Nenhuma despesa cadastrada.\n")
        return
    print("\n--- Lista de Despesas ---")
    for i in range(len(nomes_despesas)):
        print(f"{i+1}. {nomes_despesas[i]} - R$ {valores_despesas[i]:.2f}")
    print("--------------------------\n")

def calcular_total():
    """Calcula o total gasto."""
    if not valores_despesas:
        print("Nenhuma despesa cadastrada.\n")
        return
    total = sum(valores_despesas)
    print(f"Total gasto: R$ {total:.2f}\n")

def calcular_media():
    """Calcula a média das despesas."""
    if not valores_despesas:
        print("Nenhuma despesa cadastrada.\n")
        return
    media = sum(valores_despesas) / len(valores_despesas)
    print(f"Média das despesas: R$ {media:.2f}\n")

def mostrar_extremos():
    """Mostra a maior e a menor despesa."""
    if not valores_despesas:
        print("Nenhuma despesa cadastrada.\n")
        return
    maior = max(valores_despesas)
    menor = min(valores_despesas)
    indice_maior = valores_despesas.index(maior)
    indice_menor = valores_despesas.index(menor)
    print(f"Maior despesa: {nomes_despesas[indice_maior]} - R$ {maior:.2f}")
    print(f"Menor despesa: {nomes_despesas[indice_menor]} - R$ {menor:.2f}\n")

# --- Menu principal ---
while True:
    print("Controle de Gastos Familiares")
    print("1 - Adicionar despesa")
    print("2 - Mostrar todas as despesas")
    print("3 - Mostrar total gasto")
    print("4 - Mostrar média das despesas")
    print("5 - Mostrar maior e menor despesa")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_gasto()
    elif opcao == "2":
        mostrar_gastos()
    elif opcao == "3":
        calcular_total()
    elif opcao == "4":
        calcular_media()
    elif opcao == "5":
        mostrar_extremos()
    elif opcao == "6":
        print("Encerrando o programa... Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.\n")

