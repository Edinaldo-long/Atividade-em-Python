# Emojis
EMOJI_SOMA = "➕"
EMOJI_SUB = "➖"
EMOJI_MULT = "✖️"
EMOJI_DIV = "➗"

listagemvalor = []

# Solicita dois valores ao usuário
for i in range(0,2):
    valor = float(input(f"Digite o {i+1}º valor: "))
    listagemvalor.append(valor)

# Pega o valor da lista

valor1 = listagemvalor[0]
valor2 = listagemvalor [1]

# Calcula as operações
soma= sum(listagemvalor)
subtracao = valor1 - valor2
multiplicacao = valor1 * valor2

# Evita divisão por zero
if valor2 != 0:
    divisao = valor1 / valor2
else:
    divisao = "Não é possível dividir por zero"

# Mostra os resultados com emojis
print(f"\nSoma {EMOJI_SOMA}: {soma}")
print(f"Subtração {EMOJI_SUB}: {subtracao}")
print(f"Multiplicação   {EMOJI_MULT}: {multiplicacao}")
print(f"Divisão   {EMOJI_DIV}: {divisao}")          


