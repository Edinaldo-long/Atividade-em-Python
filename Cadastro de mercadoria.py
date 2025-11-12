'''Crie um programa que registre informações sobre produtos vendidos em uma loja.
O programa deve usar listas e um loop while, e encerrar quando o nome do produto 
for "fim".
Para cada produto, o usuário deve informar:
• Nome do produto
• Quantidade vendida
• Preço unitário
Depois que o cadastro terminar, o programa deve exibir:
• A quantidade total de produtos cadastrados.
• A média das quantidades vendidas.
• A média dos preços unitários.
• O produto mais caro e seu preço.
• O produto mais barato e seu preço.
• Uma lista unificada com todos os produtos no formato:
"Produto - Quantidade: X - Preço: R$Y"

'''

# Listas para armazenar os dados
nomes = []
quantidades = []
precos = []

while True:
    nome = input("Digite o nome do produto (ou 'fim' para encerrar): ")
    if nome.lower() == "fim":
        break
    
    try:
        quantidade = int(input(f"Digite a quantidade vendida de {nome}: "))
        preco = float(input(f"Digite o preço unitário de {nome}: R$"))
    except ValueError:
        print("Erro: quantidade deve ser inteira e preço deve ser número. Tente novamente.")
        continue
    
    nomes.append(nome)
    quantidades.append(quantidade)
    precos.append(preco)

# Verifica se foram cadastrados produtos
if len(nomes) == 0:
    print("Nenhum produto cadastrado.")
else:
    # Quantidade total de produtos
    total_produtos = len(nomes)
    
    # Média das quantidades vendidas
    media_quantidade = sum(quantidades) / total_produtos
    
    # Média dos preços unitários
    media_preco = sum(precos) / total_produtos
    
    # Produto mais caro
    max_preco = max(precos)
    produto_mais_caro = nomes[precos.index(max_preco)]
    
    # Produto mais barato
    min_preco = min(precos)
    produto_mais_barato = nomes[precos.index(min_preco)]
    
    # Lista unificada
    lista_unificada = []
    for i in range(total_produtos):
        lista_unificada.append(f"{nomes[i]} - Quantidade: {quantidades[i]} - Preço: R${precos[i]:.2f}")
    
    # Exibindo os resultados
    print("\n--- Relatório da Loja ---")
    print(f"Quantidade total de produtos cadastrados: {total_produtos}")
    print(f"Média das quantidades vendidas: {media_quantidade:.2f}")
    print(f"Média dos preços unitários: R${media_preco:.2f}")
    print(f"Produto mais caro: {produto_mais_caro} - R${max_preco:.2f}")
    print(f"Produto mais barato: {produto_mais_barato} - R${min_preco:.2f}")
    print("\nLista de produtos cadastrados:")
    for item in lista_unificada:
        print(item)
