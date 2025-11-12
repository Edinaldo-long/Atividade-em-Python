def adicionar_gasto(nomes_despesas, valores_despesas):
    nome = input("Digite o nome da despesa: ")
    valor = float(input("Digite o valor da despesa: R$ "))
    nomes_despesas.append(nome)
    valores_despesas.append(valor)
    print("Gasto adicionado com sucesso!\n")


def mostrar_gastos(nomes_despesas, valores_despesas):
    if len(nomes_despesas) == 0:
        print("Nenhum gasto registrado.\n")
    else:
        print("\n--- Lista de Gastos ---")
        for i in range(len(nomes_despesas)):
            print(f"{nomes_despesas[i]} - R$ {valores_despesas[i]:.2f}")
        print()


def calcular_total(valores_despesas):
    total = sum(valores_despesas)
    print(f"Total de gastos: R$ {total:.2f}\n")


def calcular_media(valores_despesas):
    if len(valores_despesas) > 0:
        media = sum(valores_despesas) / len(valores_despesas)
        print(f"Média dos gastos: R$ {media:.2f}\n")
    else:
        print("Não é possível calcular a média, não há gastos registrados.\n")


def mostrar_extremos(nomes_despesas, valores_despesas):
    if len(valores_despesas) > 0:
        maior = max(valores_despesas)
        menor = min(valores_despesas)
        print(f"Maior gasto: {nomes_despesas[valores_despesas.index(maior)]} - R$ {maior:.2f}")
        print(f"Menor gasto: {nomes_despesas[valores_despesas.index(menor)]} - R$ {menor:.2f}\n")
    else:
        print("Ainda não há gastos para comparar.\n")


# Programa Principal
nomes_despesas = []
valores_despesas = []

while True:
    print("Menu de Controle de Gastos:")
    print("1 - Adicionar gasto")
    print("2 - Mostrar gastos")
    print("3 - Calcular total")
    print("4 - Calcular média")
    print("5 - Mostrar maior e menor gasto")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_gasto(nomes_despesas, valores_despesas)
    elif opcao == "2":
        mostrar_gastos(nomes_despesas, valores_despesas)
    elif opcao == "3":
        calcular_total(valores_despesas)
    elif opcao == "4":
        calcular_media(valores_despesas)
    elif opcao == "5":
        mostrar_extremos(nomes_despesas, valores_despesas)
    elif opcao == "6":
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida, tente novamente.\n")
