# =========================================================
# SISTEMA DE GESTÃO DE ESTOQUE
# =========================================================


# Dicionário principal onde todos os produtos serão armazenados
estoque = {}

# Variável usada para gerar IDs automáticos para os produtos
proximo_id = 1


# =========================================================
# FUNÇÃO PARA CADASTRAR PRODUTOS
# =========================================================
def cadastrar_produto(nome, categoria, preco, quantidade):
    """Registra novo produto no sistema"""

    # Permite modificar a variável global proximo_id
    global proximo_id

    # Criação do dicionário do produto
    produto = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

    # Armazena o produto dentro do estoque usando o ID
    estoque[proximo_id] = produto

    # Exibe mensagem de sucesso
    print("\n Produto cadastrado com sucesso!")

    # Mostra o ID gerado para o produto
    print(f"ID do produto: {proximo_id}")

    # Incrementa o ID para o próximo produto
    proximo_id += 1


# =========================================================
# FUNÇÃO PARA REGISTRAR ENTRADA DE PRODUTOS
# =========================================================
def registrar_entrada(produto_id, quantidade):
    """Adiciona itens ao estoque"""

    # Verifica se o produto existe no estoque
    if produto_id in estoque:

        # Soma a quantidade informada ao estoque atual
        estoque[produto_id]["quantidade"] += quantidade

        # Mensagem de sucesso
        print("\n Entrada registrada com sucesso!")

    else:
        # Mensagem caso o produto não exista
        print("\n Produto não encontrado!")


# =========================================================
# FUNÇÃO PARA REGISTRAR SAÍDA DE PRODUTOS
# =========================================================
def registrar_saida(produto_id, quantidade):
    """Remove itens do estoque"""

    # Verifica se o produto existe
    if produto_id in estoque:

        # Armazena a quantidade atual do produto
        quantidade_atual = estoque[produto_id]["quantidade"]

        # Verifica se há quantidade suficiente no estoque
        if quantidade <= quantidade_atual:

            # Subtrai a quantidade do estoque
            estoque[produto_id]["quantidade"] -= quantidade

            # Mensagem de sucesso
            print("\n Saída registrada com sucesso!")

        else:
            # Mensagem de erro caso não tenha estoque suficiente
            print("\n Estoque insuficiente!")

    else:
        # Mensagem caso o produto não exista
        print("\n Produto não encontrado!")


# =========================================================
# FUNÇÃO PARA CONSULTAR PRODUTOS
# =========================================================
def consultar_estoque(produto_id):
    """Verifica saldo atual do produto"""

    # Verifica se o produto existe
    if produto_id in estoque:

        # Armazena os dados do produto em uma variável
        produto = estoque[produto_id]

        # Exibe os dados do produto
        print("\n========== DADOS DO PRODUTO ==========")
        print(f"ID: {produto_id}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Quantidade em estoque: {produto['quantidade']}")

    else:
        # Mensagem caso o produto não exista
        print("\n Produto não encontrado!")


# =========================================================
# FUNÇÃO PARA IDENTIFICAR ESTOQUE BAIXO
# =========================================================
def alertar_estoque_baixo(limite):
    """Identifica produtos com estoque crítico"""

    # Título da área de alerta
    print("\n========== ESTOQUE BAIXO ==========")

    # Variável de controle
    encontrou = False

    # Percorre todos os produtos do estoque
    for produto_id, produto in estoque.items():

        # Verifica se a quantidade é menor que o limite
        if produto["quantidade"] < limite:

            # Marca que encontrou um produto crítico
            encontrou = True

            # Exibe os dados do produto
            print(f"\nID: {produto_id}")
            print(f"Nome: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")

    # Caso nenhum produto esteja abaixo do limite
    if not encontrou:
        print("\n Nenhum produto com estoque baixo.")


# =========================================================
# FUNÇÃO PARA LISTAR TODOS OS PRODUTOS
# =========================================================
def listar_produtos():
    """Lista todos os produtos cadastrados"""

    # Verifica se o estoque está vazio
    if len(estoque) == 0:

        # Mensagem caso não existam produtos
        print("\n Nenhum produto cadastrado.")

        # Encerra a função
        return

    # Título da listagem
    print("\n========== LISTA DE PRODUTOS ==========")

    # Percorre todos os produtos cadastrados
    for produto_id, produto in estoque.items():

        # Exibe os dados do produto
        print(f"\nID: {produto_id}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")


# =========================================================
# MENU PRINCIPAL DO SISTEMA
# =========================================================

# Loop infinito para manter o sistema funcionando
while True:

    # Exibição do menu
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

    # Recebe a opção escolhida pelo usuário
    opcao = input("\nEscolha uma opção: ")

    # =====================================================
    # OPÇÃO 1 - CADASTRAR PRODUTO
    # =====================================================
    if opcao == "1":

        try:

            # Solicita os dados do produto
            nome = input("Nome do produto: ")

            categoria = input("Categoria: ")

            preco = float(input("Preço: "))

            quantidade = int(input("Quantidade inicial: "))

            # Chama a função de cadastro
            cadastrar_produto(nome, categoria, preco, quantidade)

        except ValueError:

            # Erro caso o usuário digite valores inválidos
            print("\n Erro: digite valores válidos!")

    # =====================================================
    # OPÇÃO 2 - REGISTRAR ENTRADA
    # =====================================================
    elif opcao == "2":

        try:

            # Solicita os dados
            produto_id = int(input("ID do produto: "))

            quantidade = int(input("Quantidade de entrada: "))

            # Chama a função de entrada
            registrar_entrada(produto_id, quantidade)

        except ValueError:

            # Erro de digitação
            print("\n Erro: digite números válidos!")

    # =====================================================
    # OPÇÃO 3 - REGISTRAR SAÍDA
    # =====================================================
    elif opcao == "3":

        try:

            # Solicita os dados
            produto_id = int(input("ID do produto: "))

            quantidade = int(input("Quantidade de saída: "))

            # Chama a função de saída
            registrar_saida(produto_id, quantidade)

        except ValueError:

            # Erro de digitação
            print("\n Erro: digite números válidos!")

    # =====================================================
    # OPÇÃO 4 - CONSULTAR ESTOQUE
    # =====================================================
    elif opcao == "4":

        try:

            # Solicita o ID do produto
            produto_id = int(input("ID do produto: "))

            # Consulta o produto
            consultar_estoque(produto_id)

        except ValueError:

            # Erro de digitação
            print("\n Erro: digite um ID válido!")

    # =====================================================
    # OPÇÃO 5 - ALERTA DE ESTOQUE BAIXO
    # =====================================================
    elif opcao == "5":

        try:

            # Solicita o limite mínimo
            limite = int(input("Digite o limite mínimo: "))

            # Chama a função de alerta
            alertar_estoque_baixo(limite)

        except ValueError:

            # Erro de digitação
            print("\n Erro: digite um número válido!")

    # =====================================================
    # OPÇÃO 6 - LISTAR PRODUTOS
    # =====================================================
    elif opcao == "6":

        # Exibe todos os produtos
        listar_produtos()

    # =====================================================
    # OPÇÃO 0 - SAIR DO SISTEMA
    # =====================================================
    elif opcao == "0":

        # Mensagem de encerramento
        print("\nEncerrando o sistema...")

        # Interrompe o loop principal
        break

    # =====================================================
    # CASO O USUÁRIO DIGITE UMA OPÇÃO INVÁLIDA
    # =====================================================
    else:

        # Mensagem de erro
        print("\n Opção inválida!")
        
