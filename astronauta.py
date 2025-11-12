'''Crie um programa que leia o nome de um astronauta e calcule a distância 
percorrida no espaço, onde cada letra equivale a 50 mil km. O nome deve conter no 
mínimo 3 letras'''

# Emojis
ASTRONAUTA = "👨‍🚀"
FOGUETE = "🚀"

# Solicita o nome do astronauta
nome = input(f"Digite o nome do astronauta {ASTRONAUTA}: ")

# Verifica se o nome tem pelo menos 3 letras
if len(nome) < 3:
    print("Erro: o nome deve conter no mínimo 3 letras!")
else:
    # Calcula a distância percorrida
    distancia = len(nome) * 50000  # cada letra = 50.000 km
    print(f"O astronauta {nome} percorreu {distancia:,} km no espaço {FOGUETE}")
