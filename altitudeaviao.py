'''
Exercício — Controle de Altitude O comandante precisa verificar se o avião está voando na altitude correta para
 a rota. Crie um programa em Python que: - Peça ao usuário para digitar a altitude atual do avião (em pés) e mostre
 na tela uma mensagem de acordo com o valor digitado. Se a altitude estiver entre 30.000 e 40.000 pés,
 mostre: "Altitude ideal! Mantenha o nível de voo." Se a altitude for menor que 30.000 pés, mostre:
 "Suba mais um pouco!" Se a altitude for maior que 40.000 pés, mostre: "Desça imediatamente!
'''


altitude = int(input("Digite a altitude atual do avião (em pés): "))

if 30000 <= altitude <= 40000:
    print("Altitude ideal! Mantenha o nível de voo.")
elif altitude < 30000:
    print("Suba mais um pouco!")
else:
    print("Desça imediatamente!")
