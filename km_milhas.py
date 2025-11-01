'''Crie um algoritmo que receba uma distância em quilômetros e converta para 
milhas, exibindo o resultado. 
Dica: utilize a fórmula milhas = km * 0.621371. '''

#emoji

aviao = "✈️"
onibus = "🚌"

# Solicita a distância em quilômetros
km = float(input(f"Digite a distância em quilômetros: "))

# Converte para milhas
milhas = km * 0.621371

# Mostra o resultado
print(f"{km:.2f} km {onibus} correspondem a {milhas:.2f} milhas {aviao}")
