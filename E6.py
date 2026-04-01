# =============================================
# Exercício 6 - Inventário com Dicionário
# =============================================
# Enunciado: Corrija a função para consultar um produto e mostrar quantidade e preço corretamente.
 
inventario = {
    "Notebook": {"qtd": 10, "preco": 2500},
    "Mouse": {"qtd": 50, "preco": 80}
}
 
def consultar_produto(nome):
    if nome in inventario:
        dados = inventario.get(nome)
        print(f"{nome} - Estoque: {dados['qtd']} | Preço: R${dados['preco']}")
    else:
        print("Produto não encontrado")
 
consultar_produto("Mouse")
consultar_produto("Notebook")