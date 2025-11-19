class Heroi:
    def __init__(self, nome, poder, energia):
        self.nome = nome
        self.poder = poder
        self.energia = energia

    def exibirFicha(self):
        print("\n=== FICHA DO HERÓI ===")
        print(f"Nome: {self.nome}")
        print(f"Poder: {self.poder}")
        print(f"Energia: {self.energia}")
        print("======================\n")


class HeroiIniciante(Heroi):
    def __init__(self, nome, poder, energia, nivel):
        super().__init__(nome, poder, energia)
        self.nivel = nivel
        self.tipoHeroi = "iniciante"

    def treinar(self):
        self.energia += 5
        print(f"{self.nome} treinou sozinho! (+5 energia)")
        print(f"Nova energia: {self.energia}\n")


class HeroiTreinador(Heroi):
    def __init__(self, nome, poder, energia, nivel):
        super().__init__(nome, poder, energia)
        self.nivel = nivel
        self.tipoHeroi = "treinador"

    def treinar(self):
        self.energia += 10
        print(f"{self.nome} treinou e pode treinar outros heróis! (+10 energia)")
        print(f"Nova energia: {self.energia}\n")


# LISTA PARA ARMAZENAR VÁRIOS HERÓIS
herois = []

# ------------------------------------------------------
# FUNÇÃO PARA CADASTRAR UM NOVO HERÓI
# ------------------------------------------------------
def cadastrar_heroi():
    print("\n=== NOVO HERÓI ===")
    nome = input("Nome: ")
    poder = input("Poder: ")
    energia = int(input("Energia: "))

    print("\nTipo de Herói:")
    print("1 - Iniciante")
    print("2 - Treinador")
    tipo = input("Escolha: ")

    nivel = input("Nível: ")

    if tipo == "1":
        h = HeroiIniciante(nome, poder, energia, nivel)
    elif tipo == "2":
        h = HeroiTreinador(nome, poder, energia, nivel)
    else:
        print("Tipo inválido! Criado como Herói comum.")
        h = Heroi(nome, poder, energia)

    herois.append(h)
    print("\nHerói cadastrado com sucesso!\n")


# ------------------------------------------------------
# FUNÇÃO PARA LISTAR OS HERÓIS CADASTRADOS
# ------------------------------------------------------
def listar_herois():
    if not herois:
        print("\nNenhum herói cadastrado.\n")
        return
    
    print("\n=== LISTA DE HERÓIS ===")
    for i, h in enumerate(herois):
        print(f"{i} - {h.nome} ({h.__class__.__name__})")
    print()


# ------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------
while True:
    print("=== MENU PRINCIPAL ===")
    print("1 - Cadastrar herói")
    print("2 - Exibir ficha de um herói")
    print("3 - Treinar um herói")
    print("4 - Listar todos os heróis")
    print("5 - Sair")

    op = input("Escolha: ")

    if op == "1":
        cadastrar_heroi()

    elif op == "2":
        listar_herois()
        if herois:
            idx = int(input("Escolha o índice do herói: "))
            herois[idx].exibirFicha()

    elif op == "3":
        listar_herois()
        if herois:
            idx = int(input("Escolha o índice do herói: "))
            try:
                herois[idx].treinar()
            except AttributeError:
                print("Este herói não possui método de treino.\n")

    elif op == "4":
        listar_herois()

    elif op == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida!\n")
