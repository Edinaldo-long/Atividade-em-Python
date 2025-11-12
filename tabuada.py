while True:
    print (" 1 - Deseja continuar executando tabuada")
    print(" 2 - Deseja sair ")
    opcao = input("Escolha:")

    if opcao == '1':
        print("Continuar")
    
    elif opcao =='2':
        print("Sair")

    break
else:
    print("Opção inválida")


while True:

    try:

        numero = int(input("digite um número inteiro"))
        break

    except ValueError:
        print("Caracter errado! Digite um número inteiro")

for i in range (0, 11):

    resultado = (numero) * (i)

    print(f'{numero} x {i} = {resultado}')
