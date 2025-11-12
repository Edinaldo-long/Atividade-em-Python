prateleira = []

while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    # OPÇÃO 1 - CADASTRAR PRODUTO
    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: R$ "))
        setor = input("Digite o setor do hortifrut: ")

        produto = {"nome": nome, "preco": preco, "setor": setor}
        prateleira.append(produto)

        print("✅ Produto cadastrado com sucesso!")

    # OPÇÃO 2 - LISTAR PRODUTOS
    elif opcao == "2":
        if len(prateleira) == 0:
            print("\nNenhum produto cadastrado ainda.")
        else:
            print("\n--- Produtos cadastrados ---")
            for produto in prateleira:
                print(f"Produto: {produto['nome']}")
                print(f"Preço: R$ {produto['preco']:.2f}")
                print(f"Setor: {produto['setor']}\n")

    # OPÇÃO 3 - SAIR
    elif opcao == "3":
        print("Encerrando o sistema...")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida! Digite apenas 1, 2 ou 3.")

