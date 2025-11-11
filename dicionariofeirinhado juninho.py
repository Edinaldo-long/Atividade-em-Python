# Lista para armazenar Feirinha do Juninho
prateleira = []

while True:
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$ "))
    setor = input("Digite a setor do hortifrut : ")

    # Cada produto é um dicionário, adicionado à lista
    produto = {"nome": nome, "preco": preco, "setor": setor}
    prateleira.append(produto)

    continuar = input("Deseja cadastrar outro produto? (s/n): ").lower()
    if continuar == "n":
        break

# Exibindo os produtos cadastrados
print("\n--- Produtos cadastrados ---")
for produto in prateleira:
    print(f"Produto: {produto['nome']}" )
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Setor: {produto['setor']}")
