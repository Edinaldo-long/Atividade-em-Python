'''
O comandante precisa saber se pode realizar o pouso com segurança. Crie um programa em Python que:
- Peça ao usuário para digitar a velocidade atual do avião (em km/h) e mostre uma mensagem conforme 
o valor informado: Se a velocidade for menor que 250 km/h, mostre: "Velocidade adequada para pouso. Autorizado!" 
Se a velocidade estiver entre 250 e 300 km/h, mostre: "Reduza a velocidade. Aproximação ainda alta!"
 Se a velocidade for maior que 300 km/h, mostre: "Velocidade perigosa! Arremeta imediatamente!"


'''


velocidade = int(input("Digite a velocidade atual do avião (em km/h): "))

if velocidade < 250:
    print("Velocidade adequada para pouso. Autorizado!")
elif 250 <= velocidade <= 300:
    print("Reduza a velocidade. Aproximação ainda alta!")
else:
    print("Velocidade perigosa! Arremeta imediatamente!")
