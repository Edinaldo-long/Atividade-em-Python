lista_carros = []

while True:
    print("\n---MENU---")
    print("1 -Cadastrar Veículo")
    print("2 - Listar veículos")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    # Opção 1 - cadastrar um veículo
    if opcao == "1":
        placa = input("Digite a placa do veículo: ")
        modelo = input("Digite o modelo do veículo: ")
        ano = int(input("Digite o ano do veículo: "))
        dono = input("digite o nome do dono do veículo")
        
        carro = {"placa": placa, "modelo": modelo, "ano": ano, "dono": dono} 
        lista_carros.append(carro)
        
        print("Veículo cadastrado com sucesso!")
        
    # opção 2 - Listar veículos
    elif opcao == "2":
        if len(lista_carros) == 0:
            print("\nMenhum Veículo cadastrado")
        else: 
            print("\n---LISTA DE VEÍCULOS---")
            
            for carro in lista_carros:
                print(f"placa: {carro["placa"]}")
                print(f"Modelo: {carro["modelo"]}")
                print(f"Ano: {carro["ano"]}")
                print(f"Dono: {carro["dono"]}")
                
    # opcção 3 - Sair
    elif opcao -- "3":
        print("Encerraando o sistema...")
        break
    
    # opção Inválida
    else:
        print("Opção inválida. TDigite apenas 1, 2 ou 3.")
        
                
