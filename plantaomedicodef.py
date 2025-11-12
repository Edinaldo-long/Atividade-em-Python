nomes_profissionais = []
horas_plantao = []


def adicionar_plantao(nomes_profissionais, horas_plantao):
    nome = input("Nome do profissional: ")
    horas = float(input("Horas trabalhadas no plantão: "))
    nomes_profissionais.append(nome)
    horas_plantao.append(horas)
    print("Plantão registrado com sucesso!\n")


def mostrar_plantoes(nomes_profissionais, horas_plantao):
    if len(nomes_profissionais) == 0:
        print("Nenhum plantão registrado.\n")
        return
    
    print("\n--- Plantões Registrados ---")
    for i in range(len(nomes_profissionais)):
        print(f"{nomes_profissionais[i]} → {horas_plantao[i]} horas")
    print()


def calcular_total(horas_plantao):
    return sum(horas_plantao)


def calcular_media(horas_plantao):
    if len(horas_plantao) == 0:
        print("Não há horas registradas.\n")
        return
    media = sum(horas_plantao) / len(horas_plantao)
    print(f"Média de horas de plantão: {media:.2f} horas\n")


def mostrar_extremos(nomes_profissionais, horas_plantao):
    if len(horas_plantao) == 0:
        print("Não há dados disponíveis.\n")
        return
    
    max_horas = max(horas_plantao)
    min_horas = min(horas_plantao)

    indice_max = horas_plantao.index(max_horas)
    indice_min = horas_plantao.index(min_horas)

    print("\n--- Profissionais com extremos de horas ---")
    print(f"Mais horas: {nomes_profissionais[indice_max]} → {max_horas} horas")
    print(f"Menos horas: {nomes_profissionais[indice_min]} → {min_horas} horas\n")


# Programa principal (menu)
while True:
    print("==== MENU PLANTÕES CLÍNICA ====")
    print("1. Adicionar Plantão")
    print("2. Mostrar Plantões")
    print("3. Total de Horas de Plantão")
    print("4. Média de Horas")
    print("5. Mostrar Profissional com Mais e Menos Horas")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_plantao(nomes_profissionais, horas_plantao)
    elif opcao == "2":
        mostrar_plantoes(nomes_profissionais, horas_plantao)
    elif opcao == "3":
        print(f"Total de horas de plantão: {calcular_total(horas_plantao)}\n")
    elif opcao == "4":
        calcular_media(horas_plantao)
    elif opcao == "5":
        mostrar_extremos(nomes_profissionais, horas_plantao)
    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida! Tente novamente.\n")
