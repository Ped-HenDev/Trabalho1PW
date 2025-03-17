nome = []
preco = []
estoque = []
produtos = {}
while True:
    escolha = int(input("1- Cadastrar produto\n2- Listar produto\n3- Sair\n escolha: "))
    if escolha == 1:
        cadastro_nome = input("Nome do produto: ")
        cadastro_preco = float(input("Digite o valor do produto: "))
        cadastro_estoque = int(input("Digite seu estoque: "))
        produtos[cadastro_nome] = (cadastro_preco, cadastro_estoque)
    elif escolha == 2:
        print(produtos) 
    elif escolha == 3:
        print("saiu")
        break
