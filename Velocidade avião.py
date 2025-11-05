velocidade = int(input("Digite a velocidade atual do avião (em km/h): "))

if velocidade < 250:
    print("Velocidade adequada para pouso. Autorizado!")
elif 250 <= velocidade <= 300:
    print("Reduza a velocidade. Aproximação ainda alta!")
else:
    print("Velocidade perigosa! Arremeta imediatamente!")
