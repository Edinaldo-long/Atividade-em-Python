'''Problema: Cadastro de funcionários

Você precisa criar um sistema para cadastrar funcionários de uma empresa. Cada funcionário terá:
nome
idade
setor
salario

O programa deve permitir:
Cadastrar vários funcionários.
Mostrar todos os funcionários cadastrados.
Pesquisar funcionários por setor.'''



# Lista para armazenar os funcionários
listafuncionarios = []

while True:
    print("Menu:")
    print("1 - Cadastrar funcionário")
    print("2 - Mostrar todos os funcionários")
    print("3 - Pesquisar por setor")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")
    print()
    
    if opcao == "1":
        # Cadastrar funcionário
        nome = input("Nome do funcionário: ")
        idade = int(input("Idade: "))
        setor = input("Setor: ")
        salario = float(input("Salário: R$ "))
        
        # Adiciona o funcionário à lista
        funcionario = {"nome": nome, "idade": idade, "setor": setor, "salario": salario}
        listafuncionarios.append(funcionario)
        print(f"{nome} cadastrado com sucesso!\n")
    
    elif opcao == "2":
        # Mostrar todos os funcionários
        if not listafuncionarios:
            print("Nenhum funcionário cadastrado.\n")
        else:
            print("--- Lista de Funcionários ---")
            for funcionario in listafuncionarios:
                print(f"Nome: {funcionario['nome']} - Idade: {funcionario['idade']} - Setor: {funcionario['setor']} - Salário: R$ {funcionario['salario']:.2f}")
            print()
    
    elif opcao == "3":
        # Pesquisar por setor
        setor_busca = input("Digite o setor para pesquisar: ")
        encontrados = [funcionario for funcionario in listafuncionarios if funcionario['setor'].lower() == setor_busca.lower()]
        
        if not encontrados:
            print(f"Nenhum funcionário encontrado no setor {setor_busca}.\n")
        else:
            print(f"--- Funcionários no setor {setor_busca} ---")
            for funcionario in encontrados:
                print(f"Nome: {funcionario['nome']} - Idade: {funcionario['idade']} - Salário: R$ {funcionario['salario']:.2f}")
            print()
    
    elif opcao == "4":
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida! Tente novamente.\n")
