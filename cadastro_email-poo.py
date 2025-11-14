class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def alterar_nome(self):
        novo = input("Digite o novo nome: ")
        self.nome = novo
        print("Nome atualizado com sucesso!\n")

    def alterar_email(self):
        novo = input("Digite o novo e-mail: ")
        if "@" not in novo:
            print("E-mail inválido!\n")
            return
        self.email = novo
        print("E-mail atualizado com sucesso!\n")

    def alterar_senha(self):
        antiga = input("Digite sua senha atual: ")
        if antiga != self.senha:
            print("Senha incorreta!\n")
            return
        nova = input("Digite a nova senha: ")
        self.senha = nova
        print("Senha alterada com sucesso!\n")


# ----------------------------
# FUNÇÕES DO SISTEMA
# ----------------------------

def cadastrar_usuario(lista):
    print("\n=== Cadastro de novo usuário ===")
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    lista.append(Usuario(nome, email, senha))
    print("Usuário cadastrado com sucesso!\n")


def listar_usuarios(lista):
    if not lista:
        print("\nNenhum usuário cadastrado.\n")
        return

    print("\n=== Usuários cadastrados ===")
    for i, u in enumerate(lista):
        print(f"{i} - {u.nome} ({u.email})")
    print()


def selecionar_usuario(lista):
    listar_usuarios(lista)
    if not lista:
        return None

    indice = input("Digite o número do usuário: ")

    if not indice.isdigit():
        print("Valor inválido!\n")
        return None

    indice = int(indice)

    if 0 <= indice < len(lista):
        return lista[indice]

    print("Usuário não encontrado!\n")
    return None


def excluir_usuario(lista):
    listar_usuarios(lista)
    if not lista:
        return

    indice = input("Digite o número do usuário para excluir: ")

    if not indice.isdigit():
        print("Valor inválido!\n")
        return

    indice = int(indice)

    if 0 <= indice < len(lista):
        removido = lista.pop(indice)
        print(f"Usuário '{removido.nome}' removido com sucesso!\n")
    else:
        print("Usuário não encontrado!\n")


# ----------------------------
# PROGRAMA PRINCIPAL
# ----------------------------

usuarios = []

while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Selecionar usuário para alterar")
    print("4 - Excluir usuário")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_usuario(usuarios)

    elif opcao == "2":
        listar_usuarios(usuarios)

    elif opcao == "3":
        usuario = selecionar_usuario(usuarios)
        if usuario:
            while True:
                print(f"\n--- Alterando: {usuario.nome} ---")
                print("1 - Alterar nome")
                print("2 - Alterar e-mail")
                print("3 - Alterar senha")
                print("4 - Voltar")
                escolha = input("Escolha: ")

                if escolha == "1":
                    usuario.alterar_nome()
                elif escolha == "2":
                    usuario.alterar_email()
                elif escolha == "3":
                    usuario.alterar_senha()
                elif escolha == "4":
                    break
                else:
                    print("Opção inválida!\n")

    elif opcao == "4":
        excluir_usuario(usuarios)

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida!\n")

