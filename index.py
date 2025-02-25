
inventario = {}


def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    inventario[nome] = {'preco': preco, 'quantidade': quantidade}
    print(f"Produto {nome} adicionado ao inventário.\n")


def remover_produto():
    nome = input("Digite o nome do produto a ser removido: ")
    if nome in inventario:
        del inventario[nome]
        print(f"Produto {nome} removido do inventário.\n")
    else:
        print(f"O produto {nome} não está no inventário.\n")


def listar_produtos():
    if inventario:
        for nome, info in inventario.items():
            print(f"Nome: {nome}, Preço: R${info['preco']}, Quantidade: {info['quantidade']}")
        print()
    else:
        print("O inventário está vazio.\n")


def main():
    while True:
        print("Escolha uma opção:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Sair")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            remover_produto()
        elif opcao == '3':
            listar_produtos()
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()


