while True:

    try:

        numero = int(input("digite um número inteiro"))
        break

    except ValueError:
        print("Caracter errado! Digite um número inteiro")

for i in range (0, 11):

    resultado = (numero) * (i)

    print(f'{numero} x {i} = {resultado}')
