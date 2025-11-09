# Cardápio da lanchonete
cardapio = {
    "Lanches": {"X-Burger": 15.0, "X-Salada": 18.0, "Hot Dog": 12.0},
    "Bebidas": {"Refrigerante": 5.0, "Suco": 6.0, "Água": 3.0},
    "Porções": {"Batata Frita": 10.0, "Frango Empanado": 12.0, "Anel de Cebola": 8.0}
}

# Lista para armazenar o pedido do cliente
pedido = []

while True:
    print("\n--- MENU ---")
    print("1 - Ver cardápio")
    print("2 - Fazer pedido")
    print("3 - Finalizar pedido")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- CARDÁPIO ---")
        for categoria, itens in cardapio.items():
            print(f"\n{categoria}:")
            for nome, preco in itens.items():
                print(f"  {nome} - R$ {preco:.2f}")

    elif opcao == "2":
        print("\n--- CARDÁPIO ---")
        for categoria, itens in cardapio.items():
            print(f"\n{categoria}:")
            for nome, preco in itens.items():
                print(f"  {nome} - R$ {preco:.2f}")

        item_escolhido = input("Digite o nome do item que deseja pedir: ")
        encontrado = False

        for categoria in cardapio:
            if item_escolhido in cardapio[categoria]:
                pedido.append(
                    {"item": item_escolhido, "preco": cardapio[categoria][item_escolhido]})
                print(f"{item_escolhido} adicionado ao pedido!")
                encontrado = True
                break

        if not encontrado:
            print("Opção inválida! Por favor, escolha um item do cardápio.")

    elif opcao == "3":
        if not pedido:
            print("Você não fez nenhum pedido.")
        else:
            print("\n--- PEDIDO FINAL ---")
            total = 0
            for item in pedido:
                print(f"{item['item']} - R$ {item['preco']:.2f}")
                total += item['preco']
            print(f"TOTAL: R$ {total:.2f}")
        print("Obrigado pela preferência!")
        break

    else:
        print("Opção inválida! Digite 1, 2 ou 3.")
