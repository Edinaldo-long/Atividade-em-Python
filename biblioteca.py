lista_biblioteca = []

while True:
    print("\n---MENU---")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    # Opção 1 - cadastrar livro
    if opcao == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano_publicacao = int(input("Digite o ano de publicação do livro: "))
        genero = input("Digite o gênero do livro: ")

        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano_publicacao": ano_publicacao,
            "genero": genero
        }
        lista_biblioteca.append(livro)

        print("Livro cadastrado com sucesso!")

    # Opção 2 - listar livros
    elif opcao == "2":
        if len(lista_biblioteca) == 0:
            print("\nNenhum livro cadastrado.")
        else:
            # 🔤 Ordena a lista de dicionários pelo título
            lista_ordenada = sorted(lista_biblioteca, key=lambda x: x["titulo"].lower())

            print("\n--- Livros cadastrados (em ordem alfabética) ---")
            for livro in lista_ordenada:
                print(f"Título: {livro['titulo']}")
                print(f"Autor: {livro['autor']}")
                print(f"Ano de publicação: {livro['ano_publicacao']}")
                print(f"Gênero: {livro['genero']}")
                print("-" * 20)

    # Opção 3 - sair
    elif opcao == "3":
        print("Encerrando o sistema...")
        break

    # Opção inválida
    else:
        print("Opção inválida. Digite apenas 1, 2 ou 3.")


            
                