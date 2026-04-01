# =============================================
# Exercício 8 - Busca Binária com Ordenação
# =============================================
# Enunciado: Corrija a função para ordenar a lista antes de realizar a busca binária.
 
vendas = [150, 80, 220, 90, 300]

def busca_binaria_vendas(lista, valor):
  
    indices = sorted(range(len(lista)), key=lambda i: lista[i])
    
    baixo, alto = 0, len(indices) - 1
    
    while baixo <= alto:
        meio = (baixo + alto) // 2
        idx = indices[meio]          
        
        if lista[idx] == valor:
            return idx
        
        elif lista[idx] < valor:
            baixo = meio + 1
        else:
            alto = meio - 1
            
    return -1

print("Índice do valor 220:", busca_binaria_vendas(vendas, 220))