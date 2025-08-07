#Projeto Dev2K Mobile

filename = "base.txt"

while True:
    print("\n== Sistema de Estoque Dev2K Mobile ==")
    print("1. Cadastrar Registro de Celular")
    print("2. Listar Registro de Celulares")
    print("3. Editar Registro de Celulares")
    print("4. Deletar Registro de Celular")
    print("5. Sair")

    opcao = input("Informe a opção desejada (1-5): ")

    if opcao == '1':

        print("\n== Adicionando um novo celular ==")
        imei = input("Informe o IMEI (15 dígitos, apenas números) do celular: ")

        arquivo = open(filename, 'r', encoding='utf-8')
        total_linhas = arquivo.readlines()
        arquivo.close()

        encontrado = False

        for posicao in total_linhas:
            conteudo = posicao.strip().split(',')

            if imei == conteudo[0]:
                encontrado = True

        if encontrado:
            print(f"\n{imei}: Esse IMEI já existe")
        else:
            marca = input("Informe a marca do celular: ")
            modelo = input("Informe o modelo do celular: ")
            capacidade = input("Informe a capacidade (GB) do celular: ")
            cor = input("Informe a cor do celular: ")
            valor = input("Informe o valor do celular: ")

            arquivo = open(filename, 'a', encoding='utf-8')
            arquivo.write(f"{imei}, {marca}, {modelo}, {capacidade}, {cor}, {valor}\n")
            arquivo.close()

            print(f"\nCelular com IMEI {imei} adicionado com sucesso!")
    elif opcao == '2':

        print("\n== Listando celulares  ==")
        arquivo = open(filename, 'r', encoding='utf-8')
        total_linhas = arquivo.readlines()
        arquivo.close()

        if total_linhas:
            for contador,linha in enumerate(total_linhas,1):
                conteudo = linha.strip().split(',')
                print(f"({contador})- IMEI: {conteudo[0]} - Marca:{conteudo[1]} - Modelo:{conteudo[2]} - Capacidade:{conteudo[3]}gb -  Cor:{conteudo[4]} - Valor: R${(float(conteudo[5])):.2f} ")
        else:
            print("\nNenhum celular cadastrado...")

    elif opcao == '3':
        print("\n== Atualizando lista de celulares  ==")

        imei_busca = input("Digite o IMEI do celular a ser atualizado: ")

        arquivo = open(filename, 'r', encoding='utf-8')
        total_linhas = arquivo.readlines()
        arquivo.close()

        novas_linhas = []
        encontrado = False

        for posicao in range(len(total_linhas)):
            conteudo = total_linhas[posicao].strip().split(',')

            if imei_busca == conteudo[0]:
                encontrado = True
                nova_marca = input("Digite a nova marca do celular: ")
                novo_modelo = input("Digite o novo modelo do celular: ")
                nova_capacidade = int(input("Digite a nova capacidade do celular: "))
                nova_cor = input("Digite a nova cor do celular: ")
                novo_valor = float(input("Digite o novo valor do celular: "))

                total_linhas[posicao] = f"{imei_busca}, {nova_marca}, {novo_modelo}, {nova_capacidade}, {nova_cor}, {novo_valor:.2f}\n"

        if encontrado:
            arquivo = open(filename, 'w', encoding='utf-8')
            arquivo.writelines(total_linhas)
            arquivo.close()

            print(f"Dados do celular com IMEI {imei_busca} atualizados com sucesso!!")

        else:
            print(f" Celular com o imei {imei_busca} nao encontrado!!!")

    elif opcao == '4':

        print("\n== Deletando lista de celulares  ==")
        imei_remover = input("Digite um IMEI a ser deletado: ")
        arquivo = open(filename, 'r', encoding='utf-8')
        total_linhas = arquivo.readlines()
        arquivo.close()

        novas_linhas = []
        encontrado = False
        
        for linha in total_linhas:
            conteudo = linha.strip().split(',')

            if imei_remover == conteudo[0]:
                encontrado = True
            else:
                novas_linhas.append(linha)
        if encontrado:
            arquivo = open(filename, 'w',encoding='utf-8')
            arquivo.writelines(novas_linhas)
            arquivo.close()
            print(f"O Celular com o imei {imei_remover} removido com sucesso!")
        else:
            print(f" Celular com o imei {imei_remover} nao encontrado!!!")

    elif opcao == '5':
        print("\nMuito obrigado por visitar nosso estoque, até logo!\n")
        break
    else:
        print("\nOpção Inválida! Digite novamente um número entre 1 e 5: \n")