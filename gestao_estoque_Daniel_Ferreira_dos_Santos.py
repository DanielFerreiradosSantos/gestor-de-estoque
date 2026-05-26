#multiplica "=" por 50 usando print para criar enfeite 
print("=" * 50)
#SISTEMA DE GESTÃO DE ESTOQUE
print("=" * 50)

#Dicionário principal onde todos os produtos serão armazenados
estoque = {}

#Variável usada para gerar IDs automáticos para os produtos
proximo_id = 1

print("=" * 50)
#FUNÇÃO PARA CADASTRAR PRODUTOS
print("=" * 50)
def cadastrar_produto(nome, categoria, preço, quantidade):
    """Registra novo produto no sistema"""
    
    #Permite modificar a variável global proximo_id
    global proximo_id
    
    #criação do dicionário do produto
    produto = {
        "nome": nome,
        "categoria": categoria,
        "preço": quantidade
    }  
   
    #Armazena o produto dentro do estoque usando o ID
    estoque[proximo_id] = produto
    
    #Exibe mensagem de sucesso
    print("\n Produto cadastrado com sucesso!")

    #mostra o ID gerado para o produto
    print(f"ID do produto: {proximo_id}")

    #incrementa o ID para o próximo produto
    proximo_id += 1

print("=" * 50)
#FUNÇÃO PARA REGISTRAR ENTRADA DE PRODUTOS
print("=" * 50)
def registrar_entrada(produto_id, quantidade):
    """adiciona itens ao estoque"""
    
    #verifica se o produto existe no estoque
    if produto_id in estoque:
        
        #Soma a quantidade informada ao estoque atual
        estoque[produto_id]["quantidade"] += quantidade

        #mensagem de sucesso
        print("\n Entrada registrada com sucesso!")
    else:
        #Mensagem caso o produto não exista
        print("\n produto não encontrado!")

print("=" * 50)
#FUNÇÃO PARA REGISTRAR A SAÍDA DE PRODUTOS
print("=" * 50)
def registrar_saida(produto_id, quantidade):
    """Remove itens do estoque"""
    
    #Verifica se o produto existe
    if produto_id in estoque:
        
        #Armazena a quantidade atual do produto
        quantidade atual = estoque[produto_id]["quantidade"]
        
        #Verifica se há quantidade suficiente no estoque
        if quantidade <= quantidade_atual:
            #Subtrai a quantidade do estoque
            estoque[produto_id]["quantidade"] -= quantidade
            #mensagem de sucesso
            print("\n saída registrada com sucesso!")
         
        else:
            #mensagem de erro caso não tenha estoque suficiente
            print("\n Estoque insuficiente!")
print("=" * 50)
#FUNÇÃO PARA CONSULTAR PRODUTOS
print("=" * 50)
def consultar_estoque(produto_id):
    """Verifica saldo atual do produto"""

    #Verifica se o produto existe
    if produto_id ind estoque:
        #Armazena os dados do produto em uma variável
        produto = estoque[produto_id]

        #Exibe os dados do produto
        print("\n======== DADOS DO PRODUTOS ========")
        print(f"ID: {produto_id}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: R$ {Produto[preco]:.2f}")
        print(f"Quantidade em estoque: {produto['quantidade']}")
    else:
        #Mensagem caso o produto não exista
        print("\n produto não encontrado!")
print("=" * 50)
#FUNÇÃO PARA IDENTIFICAR ESTOQUE BAIXO
print("=" * 50)
def alertar_estoque_baixo(limite):
    """Identifica produto com estoque crítico"""
    
    #Título da área de alerta
    print("\n======== ESTOQUE BAIXO ========")
    
    #Variável de controle
    encontrou = False

    # Percorre todos os produtos do estoque
    for produto_id, produto in estoque.items():

        #Verifica se a quantidade é menor que o limite
        if produto["quantidade"] < limite:

            #Marca que encontrou um produto crítivo
            encontrou = True
            
            #Exibe dados do produto
            print(f"\nID: {produto_id}")
            print(f"Nome: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")

    #Caso nenhum produto esteja abaixo do limite
    if not encontrou:
        print("\n Nenhum produto com estoque baixo.")


print("=" * 50)
#FUNÇÃO PARA LISTAR TODOS OS PRODUTOS
print("=" * 50)
def listar_produtos():
    """Lista todos os produtos cadastrados"""

    #Verifica se o estoque está vazio
    if len(estoque) == 0:

        #Mensagem caso não existam produtos
        print("\n Nenhum produto cadastrado.")

        #Encerra a função
        return

    #Título da listagem
    print("\n========== LISTA DE PRODUTOS ==========")

    #Percorre todos os produtos cadastrados
    for produto_id, produto in estoque.items():

        #Exibe os dados do produto
        print(f"\nID: {produto_id}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")


print("=" * 50)
#MENU PRINCIPAL DO SISTEMA
print("=" * 50)

#Loop infinito para manter o sistema funcionando
while True:

    #Exibição do menu
    print("\n===================================")
    print(" SISTEMA DE GESTÃO DE ESTOQUE ")
    print("===================================")

    print("1 - Cadastrar produto")
    print("2 - Registrar entrada")
    print("3 - Registrar saída")
    print("4 - Consultar estoque")
    print("5 - Alertar estoque baixo")
    print("6 - Listar produtos")
    print("0 - Sair")

    #Recebe a opção escolhida pelo usuário
    opcao = input("\nEscolha uma opção: ")

    print("=" * 50)
    #OPÇÃO 1 - CADASTRAR PRODUTO
    print("=" * 50)
    if opcao == "1":

        try:

            #Solicita os dados do produto
            nome = input("Nome do produto: ")

            categoria = input("Categoria: ")

            preco = float(input("Preço: "))

            quantidade = int(input("Quantidade inicial: "))

            #Chama a função de cadastro
            cadastrar_produto(nome, categoria, preco, quantidade)

        except ValueError:

            #Erro caso o usuário digite valores inválidos
            print("\n Erro: digite valores válidos!")

    print("=" * 50)
    #OPÇÃO 2 - REGISTRAR ENTRADA
    print("=" * 50)
    elif opcao == "2":

        try:

            #Solicita os dados
            produto_id = int(input("ID do produto: "))

            quantidade = int(input("Quantidade de entrada: "))

            #Chama a função de entrada
            registrar_entrada(produto_id, quantidade)

        except ValueError:

            #Erro de digitação
            print("\n Erro: digite números válidos!")

    print("=" * 50)
    #OPÇÃO 3 - REGISTRAR SAÍDA
    print("=" * 50)
    elif opcao == "3":

        try:

            #Solicita os dados
            produto_id = int(input("ID do produto: "))

            quantidade = int(input("Quantidade de saída: "))

            #Chama a função de saída
            registrar_saida(produto_id, quantidade)

        except ValueError:

            #Erro de digitação
            print("\n Erro: digite números válidos!")

    print("=" * 50)
    #OPÇÃO 4 - CONSULTAR ESTOQUE
    print("=" * 50)
    elif opcao == "4":

        try:

            #Solicita o ID do produto
            produto_id = int(input("ID do produto: "))

            #Consulta o produto
            consultar_estoque(produto_id)

        except ValueError:

            #Erro de digitação
            print("\n Erro: digite um ID válido!")

    print("=" * 50)
    #OPÇÃO 5 - ALERTA DE ESTOQUE BAIXO
    print("=" * 50)
    elif opcao == "5":

        try:

            #Solicita o limite mínimo
            limite = int(input("Digite o limite mínimo: "))

            #Chama a função de alerta
            alertar_estoque_baixo(limite)

        except ValueError:

            #Erro de digitação
            print("\n Erro: digite um número válido!")

    print("=" * 50)
    #OPÇÃO 6 - LISTAR PRODUTOS
    print("=" * 50)
    elif opcao == "6":

        #Exibe todos os produtos
        listar_produtos()

    print("=" * 50)
    #OPÇÃO 0 - SAIR DO SISTEMA
    print("=" * 50)
    elif opcao == "0":

        #Mensagem de encerramento
        print("\nEncerrando o sistema...")

        #Interrompe o loop principal
        break

    print("=" * 50)
    #CASO O USUÁRIO DIGITE UMA OPÇÃO INVÁLIDA
    print("=" * 50)
    else:

        #Mensagem de erro
        print("\n Opção inválida!")
        
