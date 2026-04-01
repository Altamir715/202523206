# =============================================
# Exercício 4 - Busca Sequencial
# =============================================
# Enunciado: Corrija a busca sequencial para retornar o índice do item ou -1 se não for encontrado.
 
estoque = ["Mouse", "Teclado", "Monitor", "Notebook"]
 
def busca_sequencial(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return -1
 
print("Índice do Monitor:", busca_sequencial(estoque, "Monitor"))
print("Índice do Celular:", busca_sequencial(estoque, "Celular"))
 