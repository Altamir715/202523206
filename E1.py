# =============================================
# Exercício 1 - Estoque de Produtos
# =============================================
# Enunciado: Corrija o código para adicionar um produto na lista apenas se ele ainda não existir.
# O programa deve mostrar o estoque atualizado após cada tentativa.

estoque = ["Notebook", "Mouse", "Teclado"]
 
def adicionar_produto(lista, produto):
    if produto not in lista:
        lista.append(produto)
    print("Estoque atual:", lista)
 
adicionar_produto(estoque, "Monitor")
adicionar_produto(estoque, "Mouse")