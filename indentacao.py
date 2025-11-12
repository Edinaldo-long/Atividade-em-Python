lista = []

while True:
    print("1 - Cadastrar número")
    print("2 - Mostrar números")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero = int(input("Digite um número: "))
        lista.append(numero)

    elif opcao == "2":
        print("Números cadastrados:", lista)

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
