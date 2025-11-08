print("=" * 60)
print("✈️  SISTEMA DE CADASTRO DE TRIPULANTES  ✈️")
print("=" * 60)
print()

# ==============================================================
# PASSO 1: Criar as listas vazias para guardar os dados
# ==============================================================
print("📦 Criando as listas vazias...")

nomes = []           # Lista para guardar os nomes
profissoes = []      # Lista para guardar as profissões
anos = []            # Lista para guardar os anos de nascimento
horas_voo = []       # Lista para guardar as horas de voo

print("✅ Listas criadas!\n")

# ==============================================================
# PASSO 2: Criar contadores (começam com zero)
# ==============================================================
print("🔢 Criando os contadores...")

total_pilotos = 0        # Conta quantos pilotos
total_comissarios = 0    # Conta quantos comissários
total_antes_2000 = 0     # Conta quantos nasceram antes de 2000

print("✅ Contadores criados!\n")

# ==============================================================
# PASSO 3: Lista para nascidos após 1990
# ==============================================================
print("🌟 Criando lista especial...")

nascidos_apos_1990 = []  # Lista vazia que vai receber os nomes

print("✅ Lista especial criada!\n")

print("=" * 60)
print("🚀 VAMOS COMEÇAR O CADASTRO!")
print("=" * 60)
print()

# ==============================================================
# PASSO 4: Cadastrar os 10 tripulantes (um por vez)
# ==============================================================
for i in range(2):
    print(f"👤 TRIPULANTE #{i+1} de 10")
    print("-" * 40)
    
    # --- Cadastrar NOME ---
    nome = input("📝 Digite o nome: ").strip()
    nomes.append(nome)  # Adiciona o nome na lista
    print(f"   ✅ Nome '{nome}' salvo na lista!")
    
    # --- Cadastrar PROFISSÃO (com validação) ---
    while True:  # Repete até digitar certo
        print("💼 Digite a profissão (piloto/comissário/mecânico): ", end="")
        profissao = input().strip().lower()
        
        # Verifica se é uma profissão válida
        if profissao in ["piloto", "comissário", "comissario", "mecânico", "mecanico"]:
            profissoes.append(profissao)  # Adiciona a profissão na lista
            break  # Sai do loop, está correto!
        else:
            print("   ❌ Profissão inválida! Digite apenas: piloto, comissário ou mecânico")
            print()
    
    # Contar se é piloto ou comissário
    if profissao == "piloto":
        total_pilotos = total_pilotos + 1  # Aumenta o contador
        print(f"   ✈️ Piloto cadastrado! Total de pilotos: {total_pilotos}")
    elif profissao in ["comissário", "comissario"]:
        total_comissarios = total_comissarios + 1  # Aumenta o contador
        print(f"   👨‍🍳 Comissário cadastrado! Total: {total_comissarios}")
    else:
        print(f"   🔧 Mecânico cadastrado!")
    
    # --- Cadastrar ANO DE NASCIMENTO ---
    ano = int(input("📅 Digite o ano de nascimento: "))
    anos.append(ano)  # Adiciona o ano na lista
    
    # Verificar se nasceu antes de 2000
    if ano < 2000:
        total_antes_2000 = total_antes_2000 + 1  # Aumenta o contador
        print(f"   📌 Nasceu antes de 2000! Total: {total_antes_2000}")
    
    # Verificar se nasceu depois de 1990
    if ano > 1990:
        nascidos_apos_1990.append(nome)  # Adiciona o nome na lista especial
        print(f"   🌟 Nasceu após 1990! Adicionado à lista especial")
    
    # --- Cadastrar HORAS DE VOO ---
    horas = float(input("🕐 Digite as horas de voo: "))
    horas_voo.append(horas)  # Adiciona as horas na lista
    print(f"   ✅ Horas salvas!")
    
    print()  # Linha em branco para separar

# ==============================================================
# PASSO 5: Encontrar o tripulante com MAIS horas de voo
# ==============================================================
print("🏆 Procurando o recordista...")
max_horas = max(horas_voo)  # Encontra o maior número de horas
posicao = horas_voo.index(max_horas)  # Descobre em que posição está
nome_max_horas = nomes[posicao]  # Pega o nome na mesma posição
print(f"   🥇 Recordista: {nome_max_horas} com {max_horas} horas!\n")

# ==============================================================
# PASSO 6: Calcular a média de horas de voo
# ==============================================================
print("📊 Calculando a média de horas de voo...")
media_horas = sum(horas_voo) / len(horas_voo)  # Usa sum() para somar tudo!
print(f"   Soma total: {sum(horas_voo)} horas")
print(f"   Dividido por: {len(horas_voo)} tripulantes")
print(f"   Média: {media_horas:.2f} horas\n")

# ==============================================================
# PASSO 7: Mostrar o RELATÓRIO FINAL
# ==============================================================
print("=" * 60)
print("📊 RELATÓRIO FINAL DO CADASTRO")
print("=" * 60)
print()

print("👥 RESUMO DOS TRIPULANTES:")
print(f"   👨‍✈️ Total de pilotos: {total_pilotos}")
print(f"   👨‍🍳 Total de comissários: {total_comissarios}")
print()

print("📆 ANÁLISE POR IDADE:")
print(f"   📌 Pessoas nascidas antes de 2000: {total_antes_2000}")
print()

print("🏆 RECORDISTA:")
print(f"   🥇 Tripulante com mais horas: {nome_max_horas}")
print(f"   ⏱️  Total de horas: {max_horas:.1f} horas")
print()

print("📈 ESTATÍSTICAS:")
print(f"   📊 Média de horas de voo: {media_horas:.2f} horas")
print()

print("🌟 TRIPULANTES NASCIDOS APÓS 1990:")
if len(nascidos_apos_1990) > 0:
    for nome in nascidos_apos_1990:
        print(f"   ✨ {nome}")
else:
    print("   ❌ Nenhum tripulante nascido após 1990")

print()
print("=" * 60)
print("✅ CADASTRO CONCLUÍDO COM SUCESSO!")
print("=" * 60)