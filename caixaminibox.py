# Emojis
MOEDA = "💲"
FALTA = "⚠️"

# Solicita o valor da compra e o valor pago
valor_compra = float(input("Digite o valor total da compra: R$ "))
valor_pago = float(input("Digite o valor pago: R$ "))

# Calcula o troco
troco = valor_pago - valor_compra

# Verifica se o pagamento foi suficiente
if troco < 0:
    print(f"{FALTA} Pagamento insuficiente! Faltam R$ {abs(troco):.2f}")
else:
    print(f"{MOEDA} Troco: R$ {troco:.2f} ")
