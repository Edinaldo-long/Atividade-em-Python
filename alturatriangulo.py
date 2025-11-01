'''Crie um algoritmo que receba a área e a base de um triângulo e calcule sua 
altura.  
Dica: utilize a fórmula altura = (2 * área) / base. '''

# Emojis
triangulo = "🛆"
erro = "🙈"

# Solicita a área e a base do triângulo
area = float(input("Digite a área do triângulo: "))
base = float(input("Digite a base do triângulo: "))

# Verifica se a base não é zero para evitar divisão por zero
if base != 0:
    altura = (2 * area) / base
    print(f"{triangulo} A altura do triângulo é: {altura:.2f}  ")
else:
    print(f"{erro} Erro: a base do triângulo não pode ser zero!")
 