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
        
