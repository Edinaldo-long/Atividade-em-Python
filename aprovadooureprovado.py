'''DESAFIO
- Solicite 4 notas ao usuário;
- Calcule e mostre a média das 4 notas válidas no final;
- Caso a média fique maior ou igual 9 e menor ou igual 10 
- Mostre: Aprovado com A.
- Caso a média fique maior ou igual 8 e menor que 9 
- Mostre: Aprovado com B.
- Caso a média fique maior ou igual 7 e menor que 8 
- Mostre: Aprovado com C.
- Caso a média fique menor que 7
- Mostre: Reprovado.'''


# Códigos de cores ANSI
VERDE = "\033[92m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
VERMELHO = "\033[91m"
RESET = "\033[0m"

# Emojis
TROFEU = "🏆"
FESTA = "🎉"
JOINHA = "👍"
TRISTE = "🤢"

listagemnota = []


# Solicita as 4 notas ao usuário

for i in range (0,4):
    nota = float(input(f"Digite a {i+1} ª nota: "))
    listagemnota.append(nota)

# Calcula a média
media = sum(listagemnota)/len(listagemnota)

# Mostra a média com cor azul
print(f"\n{AZUL}Média final: {media:.2f}{RESET}")

# Verifica e mostra o resultado com cor + emoji
if media >= 9 and media <= 10:
    print(f"{VERDE}Aprovado com A {TROFEU}{RESET}")
elif media >= 8 and media < 9:
    print(f"{AMARELO}Aprovado com B {FESTA}{RESET}")
elif media >= 7 and media < 8:
    print(f"{AMARELO}Aprovado com C {JOINHA}{RESET}")
else:
    print(f"{VERMELHO}Reprovado {TRISTE}{RESET}")
