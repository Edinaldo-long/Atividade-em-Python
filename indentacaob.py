listanumero = []  # 0 espaços (nível 0)

while True:  # 0 espaços (nível 0)
    opcao = input("1-Adicionar  2-Soma  3-Sair: ")  # 4 espaços (nível 1)

    if opcao == "1":  # 4 espaços (nível 1)
        while True:  # 8 espaços (nível 2)
            try:  # 12 espaços (nível 3)
                # 16 espaços (nível 4)
                num = float(input("Digite um número qualquer: "))
                listanumero.append(num)  # 16 espaços (nível 4)
                break  # 16 espaços (nível 4) -> sai do loop interno
            except ValueError:  # 12 espaços (nível 3)
                print("Erro! Digite um número válido.")  # 16 espaços (nível 4)

    elif opcao == "2":  # 4 espaços (nível 1)
        soma = sum(listanumero)  # 8 espaços (nível 2)
        print(f"A soma dos números na lista é: {soma}")  # 8 espaços (nível 2)

    elif opcao == "3":  # 4 espaços (nível 1)
        print("Saindo...")  # 8 espaços (nível 2)
        break  # 8 espaços (nível 2) -> sai do loop principal

    else:  # 4 espaços (nível 1)
        print("Opção inválida")  # 8 espaços (nível 2)
