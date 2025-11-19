# Classe pai
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def exibir_dados(self):
        print("=== Dados do Usuário ===")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")


# Classe filha herdando de Usuario
class Cliente(Usuario):
    def __init__(self, nome, email, telefone):
        super().__init__(nome, email)  # chama o construtor da classe pai
        self.telefone = telefone

    # Polimorfismo: sobrescrevendo o método da classe pai
    def exibir_dados(self):
        print("=== Dados do Cliente ===")
        super().exibir_dados()  # aproveita o método da classe pai
        print(f"Telefone: {self.telefone}")


# Programa principal
cliente1 = Cliente("João Silva", "joao@gmail.com", "11 99999-0000")

cliente1.exibir_dados()
