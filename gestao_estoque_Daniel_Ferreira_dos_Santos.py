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
    
    #Permite modificar a variável golobal proximo_id
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

