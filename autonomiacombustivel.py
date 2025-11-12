# Emojis
GASOLINA = "⛽"
CARRO = "🚗"
AUTONOMIA = "📏"

# Solicita os dados ao usuário
litros = float(input(f"Digite a quantidade de combustível abastecido (litros) {GASOLINA}: "))


# Verifica se o combustível não é zero
if litros == 0:
     print("Erro: a quantidade de combustível não pode ser zero!")
   
else:

     # Solicita a quilometragem percorrida apenas se litros > 0
    km_percorridos = float(input(f"Digite a quilometragem percorrida (km) {CARRO}: "))
    autonomia = km_percorridos / litros
    print(f"{AUTONOMIA} A autonomia do veículo é: {autonomia:.2f} km/l")