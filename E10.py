# =============================================
# Exercício 10 - Estudo de Caso: Sistema de Controle de Estoque da TechZone
# =============================================
# Enunciado:
# A TechZone precisa de um sistema de estoque. O código abaixo contém vários bugs.
# Corrija todos os problemas para que o sistema funcione corretamente com as seguintes funcionalidades:
# - Cadastrar novo produto
# - Buscar produto (busca sequencial)
# - Atualizar quantidade em estoque
# - Encontrar o produto mais barato acima de um determinado preço (usando busca binária)
# - Gerar relatório completo do estoque
# Trate todos os erros de entrada do usuário de forma amigável.

estoque = [
    {"nome": "Notebook Dell", "quantidade": 8, "preco": 2899.90},
    {"nome": "Mouse Logitech", "quantidade": 45, "preco": 89.90},
    {"nome": "Teclado Mecânico", "quantidade": 12, "preco": 249.90},
    {"nome": "Monitor 24''", "quantidade": 15, "preco": 899.90}
]


def cadastrar_produto():
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("Erro: nome do produto não pode ser vazio.")
        return

    try:
        quantidade = int(input("Quantidade inicial: ").strip())
        preco = float(input("Preço unitário: R$").strip())
    except ValueError:
        print("Erro: quantidade e preço devem ser números!")
        return

    if quantidade < 0 or preco <= 0:
        print("Erro: quantidade deve ser >= 0 e preço deve ser > 0.")
        return

    estoque.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    print(f"Produto {nome} cadastrado com sucesso!")


def buscar_produto(nome_busca):
    nome_busca = nome_busca.strip()
    for produto in estoque:
        if produto["nome"].lower() == nome_busca.lower():
            return produto
    return None


def atualizar_quantidade(nome, quantidade_alterada):
    produto = buscar_produto(nome)
    if produto:
        novo_total = produto["quantidade"] + quantidade_alterada
        if novo_total < 0:
            print("Erro: não é possível ter quantidade negativa no estoque.")
            return
        produto["quantidade"] = novo_total
        print(f"Estoque atualizado! {nome} agora tem {produto['quantidade']} unidades.")
    else:
        print("Produto não encontrado!")


def produto_mais_barato_acima_de(preco_minimo):
    if preco_minimo < 0:
        return "Preço mínimo deve ser >= 0."

    produtos_ordenados = sorted(estoque, key=lambda p: p["preco"])
    baixo, alto = 0, len(produtos_ordenados) - 1
    resultado = None

    while baixo <= alto:
        meio = (baixo + alto) // 2
        if produtos_ordenados[meio]["preco"] >= preco_minimo:
            resultado = produtos_ordenados[meio]
            alto = meio - 1
        else:
            baixo = meio + 1

    if not resultado:
        return "Nenhum produto encontrado acima desse preço."

    return (f"Produto mais barato acima de R${preco_minimo:.2f}: "
            f"{resultado['nome']} - R${resultado['preco']:.2f}")


def gerar_relatorio():
    if not estoque:
        print("Estoque vazio!")
        return

    total_estoque = 0
    print("\n--- Relatório de Estoque ---")
    for produto in estoque:
        valor_total = produto["quantidade"] * produto["preco"]
        total_estoque += valor_total
        print(f"{produto['nome']:25} | Qtd: {produto['quantidade']:3} | Preço: R${produto['preco']:.2f} | Total: R${valor_total:.2f}")

    print(f"\nValor total em estoque: R${total_estoque:.2f}")


def menu():
    while True:
        print("\n=== TechZone - Controle de Estoque ===")
        print("1. Cadastrar novo produto")
        print("2. Buscar produto")
        print("3. Atualizar quantidade")
        print("4. Produto mais barato acima de um preço")
        print("5. Gerar relatório completo")
        print("6. Sair")

        try:
            opcao = int(input("\nEscolha uma opção: ").strip())
        except ValueError:
            print("Opção inválida! Digite um número.")
            continue

        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            nome = input("Digite o nome do produto: ")
            prod = buscar_produto(nome)
            if prod:
                print(f"Encontrado: {prod['nome']} - Qtd: {prod['quantidade']} - R${prod['preco']:.2f}")
            else:
                print("Produto não encontrado.")
        elif opcao == 3:
            nome = input("Nome do produto: ")
            try:
                qtd = int(input("Quantidade a adicionar/subtrair (use negativo para saída): ").strip())
                atualizar_quantidade(nome, qtd)
            except ValueError:
                print("Quantidade inválida!")
        elif opcao == 4:
            try:
                preco = float(input("Preço mínimo: R$").strip())
                print(produto_mais_barato_acima_de(preco))
            except ValueError:
                print("Preço inválido!")
        elif opcao == 5:
            gerar_relatorio()
        elif opcao == 6:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


if __name__ == '__main__':
    menu()
