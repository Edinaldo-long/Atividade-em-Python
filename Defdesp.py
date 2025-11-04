''' Crie um programa com funções que registram despesas, mostram todas as 
despesas e calculam o total e a média, usando uma lista global, sem passar 
parâmetros.
cadastrar_despesa() → pede ao usuário o valor de uma despesa e guarda em uma 
lista global.
mostrar_despesas() → mostra todas as despesas cadastradas.
calcular_total() → soma todas as despesas da lista global e imprime o resultado.
calcular_media() → calcula a média das despesas da lista global e imprime.'''

# Lista global para armazenar as despesas 💵
despesas = []

# Função para cadastrar uma nova despesa 📝
def cadastrar_despesa():
    valor = float(input("💸 Digite o valor da despesa: R$ "))
    despesas.append(valor)
    print("✅ Despesa cadastrada com sucesso!\n")

# Função para mostrar todas as despesas registradas 📋
def mostrar_despesas():
    if not despesas:
        print("⚠️ Nenhuma despesa cadastrada ainda!\n")
    else:
        print("📜 Lista de Despesas:")
        for i, valor in enumerate(despesas, start=1):
            print(f"   {i}️⃣ → R$ {valor:.2f}")
        print()

# Função para calcular o total das despesas 💰
def calcular_total():
    if not despesas:
        print("⚠️ Nenhuma despesa cadastrada para calcular o total!\n")
    else:
        total = sum(despesas)
        print(f"💵 Total das despesas: R$ {total:.2f}\n")

# Função para calcular a média das despesas 📊
def calcular_media():
    if not despesas:
        print("⚠️ Nenhuma despesa cadastrada para calcular a média!\n")
    else:
        media = sum(despesas) / len(despesas)
        print(f"📊 Média das despesas: R$ {media:.2f}\n")

# Menu principal 🧭
while True:
    print("========== MENU DE DESPESAS 💼 ==========")
    print("1️⃣ - Cadastrar despesa")
    print("2️⃣ - Mostrar todas as despesas")
    print("3️⃣ - Calcular total das despesas")
    print("4️⃣ - Calcular média das despesas")
    print("5️⃣ - Sair ")

    opcao = input("👉 Escolha uma opção: ")

    if opcao == "1":
        cadastrar_despesa()
    elif opcao == "2":
        mostrar_despesas()
    elif opcao == "3":
        calcular_total()
    elif opcao == "4":
        calcular_media()
    elif opcao == "5":
        print(" Saindo do programa. Até logo!")
        break
    else:
        print("❌ Opção inválida! Tente novamente.\n")
