while True:
    print(" 1 - Deseja executar program")
    print(" 2 - Deseja sair ")
    opcao = input("Escolha:")

    if opcao == '1':
        print("Continuar")

    elif opcao == '2':
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

while True:

    listanumero = []

for i in range(0, 5):

    numero = float(input("Digite um número qualquer"))
    listanumero.append(numero)

soma = sum(listanumero)
minimo = min(listanumero)
maximo = max(listanumero)
media = sum(listanumero)/len(listanumero)

print(F"Os número escolhidos foram: {listanumero}")

print(f"A soma dos número escolhidos é: {soma}")

print(f"O maior número escolhido é o: {maximo}")

print(f"O menor numero escolhido é: {minimo}")

print(f"A média dos numeros digitados são: {media}")
