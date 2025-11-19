class PlanoNetflix:
    def __init__(self, nome, tipo_plano, telas, qualidade):
        self.nome = nome
        self.tipo_plano = tipo_plano
        self.telas = telas
        self.qualidade = qualidade

    def exibirInfo(self):
        print("\n=== FICHA DO PLANO ===")
        print(f"Usuário: {self.nome}")
        print(f"Plano: {self.tipo_plano}")
        print(f"Telas simultâneas: {self.telas}")
        print(f"Qualidade: {self.qualidade}")
        print("======================\n")


class PlanoBasico(PlanoNetflix):
    def __init__(self, nome):
        super().__init__(nome, "Básico", 1, "SD")

    def detalhes(self):
        print("Apenas 1 tela por vez, qualidade SD.\n")


class PlanoPadrao(PlanoNetflix):
    def __init__(self, nome):
        super().__init__(nome, "Padrão", 2, "HD")

    def detalhes(self):
        print("Até 2 telas simultâneas, qualidade HD.\n")


class PlanoPremium(PlanoNetflix):
    def __init__(self, nome):
        super().__init__(nome, "Premium", 4, "4K")

    def detalhes(self):
        print("Até 4 telas simultâneas, qualidade 4K.\n")


# LISTA PARA ARMAZENAR PLANOS
planos = []


# ------------------------------------------------------
# FUNÇÃO PARA CADASTRAR UM NOVO PLANO
# ------------------------------------------------------
def cadastrar_plano():
    print("\n=== NOVO PLANO ===")
    nome = input("Nome do usuário: ")

    print("\nTipo de Plano:")
    print("1 - Básico")
    print("2 - Padrão")
    print("3 - Premium")
    tipo = input("Escolha: ")

    if tipo == "1":
        p = PlanoBasico(nome)
    elif tipo == "2":
        p = PlanoPadrao(nome)
    elif tipo == "3":
        p = PlanoPremium(nome)
    else:
        print("Tipo inválido! Criado como plano comum.")
        p = PlanoNetflix(nome, "Comum", 1, "SD")

    planos.append(p)
    print("\nPlano cadastrado com sucesso!\n")


# ------------------------------------------------------
# FUNÇÃO PARA LISTAR OS PLANOS CADASTRADOS
# ------------------------------------------------------
def listar_planos():
    if not planos:
        print("\nNenhum plano cadastrado.\n")
        return
    
    print("\n=== LISTA DE PLANOS ===")
    for i, p in enumerate(planos):
        print(f"{i} - {p.nome} ({p.tipo_plano})")
    print()


# ------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------
while True:
    print("=== MENU PRINCIPAL ===")
    print("1 - Cadastrar plano")
    print("2 - Exibir ficha de um plano")
    print("3 - Detalhes de um plano")
    print("4 - Listar todos os planos")
    print("5 - Sair")

    op = input("Escolha: ")

    if op == "1":
        cadastrar_plano()

    elif op == "2":
        listar_planos()
        if planos:
            try:
                idx = int(input("Escolha o índice do plano: "))
                planos[idx].exibirInfo()
            except (ValueError, IndexError):
                print("Índice inválido!\n")

    elif op == "3":
        listar_planos()
        if planos:
            try:
                idx = int(input("Escolha o índice do plano: "))
                planos[idx].detalhes()
            except (ValueError, IndexError):
                print("Índice inválido!\n")
            except AttributeError:
                print("Este plano não possui detalhes específicos.\n")

    elif op == "4":
        listar_planos()

    elif op == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida!\n")
