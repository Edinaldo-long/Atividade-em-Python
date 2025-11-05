altitude = int(input("Digite a altitude atual do avião (em pés): "))

if 30000 <= altitude <= 40000:
    print("Altitude ideal! Mantenha o nível de voo.")
elif altitude < 30000:
    print("Suba mais um pouco!")
else:
    print("Desça imediatamente!")
