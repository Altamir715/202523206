import random
import time

def Selection_sort():
    
    lista1 = []
    lista2 = []
    lista3 = []

    # Geradores de listas compatíveis
    for i in range(5000): 
        lista1.append(random.randint(0,5000))

    for i in range(10000): 
        lista2.append(random.randint(0,10000))

    for i in range(20000): 
        lista3.append(random.randint(0,20000))

    inicio = time.time() 

    def selection_sort(lista):
        # algoritimo de ordenação
        # Complexidade = O(n²)
        
        n = len(lista)
        
        # Percorre toda a lista (exceto o último elemento, que já estará ordenado)
        for i in range(n - 1):
            # Assume que o primeiro elemento não ordenado é o menor
            indice_minimo = i
            
            # Percorre o restante da lista para encontrar o verdadeiro menor elemento
            for j in range(i + 1, n):
                if lista[j] < lista[indice_minimo]:
                    indice_minimo = j
            
            # Se encontrou um elemento menor, troca com o elemento da posição inicial i
            if indice_minimo != i:
                lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
                
        return lista

    Lista_curta = selection_sort(lista1)
    fim = time.time()
    total1 = fim - inicio # Calcular tempo de execução

    print(f"\n Para até {len(lista1)} itens, o selection sort ordena a lista em cerca de: {total1:.2f} seguds")

    lista_media = selection_sort(lista2)
    fim = time.time()
    total2 = fim - inicio

    print(f"\n Para até {len(lista2)} itens, o selection sorte ordena a lista em cerca de: {total2:.2f} seguds")

    lista_grande = selection_sort(lista3)
    fim = time.time()
    total3 = fim - inicio

    print(f"\n Para até {len(lista3)} itens, o selection sorte ordena a lista em cerca de: {total3:.2f}s\n")



def Bubble_sort():
     
    # algoritimo de ordenação
    # Complexidade = O(n²)

    lista1 = []
    lista2 = []
    lista3 = []

    # Geradores de listas compatíveis
    for i in range(5000): 
        lista1.append(random.randint(0,5000))

    for i in range(10000): 
        lista2.append(random.randint(0,10000))

    for i in range(20000): 
        lista3.append(random.randint(0,20000))

    inicio1 = time.time()
    def bubble_sort(lista):

        # Complexidade = O(n²)
        
        n = len(lista)
        
        # Percorre todos os elementos da lista
        for i in range(n):
            # Flag para otimizar: se não houver trocas, a lista já está ordenada
            trocado = False
            
            # Últimos i elementos já estão em suas posições corretas
            for j in range(0, n - i - 1):
                if lista[j] > lista[j + 1]:
                    # Troca os elementos se estiverem fora de ordem
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocado = True
                    
            if not trocado:
                break
                
        return lista    
    
    
    lista_curta = bubble_sort(lista1)
    fim1 = time.time()
    total = fim1 - inicio1

    print(f"\nPara até {len(lista1)} itens, o bubble sorte ordena a lista em cerca de: {total:.2f} seguds")

    lista_media = bubble_sort(lista2)
    fim1 = time.time()
    total1 = fim1 - inicio1

    print(f"\nPara até {len(lista2)} itens, o bubble sorte ordena a lista em cerca de: {total1:.2f} seguds")
    
    lista_grande = bubble_sort(lista3)
    fim1 = time.time()
    total2 = fim1 - inicio1

    print(f"\nPara até {len(lista3)} itens, o bubble sorte ordena a lista em cerca de: {total2:.2f} seguds\n")



def Insertion_sort():
    
    # algoritimo de ordenação
    # Complexidade = O(n²)

    lista1 = []
    lista2 = []
    lista3 = []

    # Geradores de listas compatíveis
    for i in range(5000): 
        lista1.append(random.randint(0,5000))

    for i in range(10000): 
        lista2.append(random.randint(0,10000))

    for i in range(20000): 
        lista3.append(random.randint(0,20000))

    inicio = time.time()
    def insertion_sort(lista):
    # Começa do segundo elemento (índice 1) até o final da lista
        for i in range(1, len(lista)):
            chave = lista[i]
            j = i - 1
            
            # Move os elementos da lista[0..i-1] que são maiores que a chave
            # para uma posição à frente da sua posição atual
            while j >= 0 and lista[j] > chave:
                lista[j + 1] = lista[j]
                j -= 1
                
            # Insere a chave na posição correta
            lista[j + 1] = chave
        return lista

    lista_curta = insertion_sort(lista1)
    fim = time.time()
    total = fim - inicio

    print(f"\nPara até {len(lista1)} itens, o insertion sort ordena a lista em cerca de: {total:.2f} seguds")

    lista_media = insertion_sort(lista2)
    fim = time.time()
    total1 = fim - inicio

    print(f"\nPara até {len(lista2)} itens, o insertion sort ordena a lista em cerca de: {total1:.2f} seguds")
 
    lista_grande = insertion_sort(lista3)
    fim = time.time()
    total2 = fim - inicio

    print(f"\nPara até {len(lista3)} itens, o insertion sort ordena a lista em cerca de: {total2:.2f} seguds")
 


def Merge_sort():

    # algoritmo de ordenação
    # Complexidade = melhor caso O(nlogn)

    lista1 = []
    lista2 = []
    lista3 = []

    # Geradores de listas compatíveis
    for i in range(50000): 
        lista1.append(random.randint(0,50000))

    for i in range(80000): 
        lista2.append(random.randint(0,80000))

    for i in range(100000): 
        lista3.append(random.randint(0,100000))

    inicio = time.time()
    def merge_sort(lista):
        # Caso base: uma lista com 0 ou 1 elemento já está ordenada
        if len(lista) <= 1:
            return lista
        
        # Divide a lista no meio
        meio = len(lista) // 2
        metade_esquerda = merge_sort(lista[:meio])
        metade_direita = merge_sort(lista[meio:])
        
        # Junta as duas metades ordenadas
        return merge(metade_esquerda, metade_direita)

    def merge(esquerda, direita):
        lista_ordenada = []
        i = j = 0
        
        # Compara os elementos das duas listas e os adiciona em ordem
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] <= direita[j]:
                lista_ordenada.append(esquerda[i])
                i += 1
            else:
                lista_ordenada.append(direita[j])
                j += 1
                
        # Se sobraram elementos na metade esquerda ou direita, adiciona ao final
        lista_ordenada.extend(esquerda[i:])
        lista_ordenada.extend(direita[j:])
        
        return lista_ordenada

    lista_curta = merge_sort(lista1)
    fim = time.time()
    total = fim - inicio

    print(f"\nPara até {len(lista1)} itens, o merge sort ordena a lista em cerca de: {total:.2f} seguds")

    lista_media = merge_sort(lista2)
    fim = time.time()
    total1 = fim - inicio

    print(f"\nPara até {len(lista2)} itens, o merge sort ordena a lista em cerca de: {total1:.2f} seguds")
 
    lista_grande = merge_sort(lista3)
    fim = time.time()
    total2 = fim - inicio

    print(f"\nPara até {len(lista3)} itens, o merge sort ordena a lista em cerca de: {total2:.2f} seguds")

 

def Quick_sort():
    
    lista1 = []
    lista2 = []
    lista3 = []

    # Geradores de listas compatíveis
    for i in range(50000): 
        lista1.append(random.randint(0,50000))

    for i in range(80000): 
        lista2.append(random.randint(0,80000))

    for i in range(100000): 
        lista3.append(random.randint(0,100000))
    
    inicio = time.time()
    def quick_sort(lista):
        # Caso base: listas vazias ou com 1 elemento já estão ordenadas
        if len(lista) <= 1:
            return lista
    
        # Escolhe o último elemento como pivô (pode ser qualquer um)
        pivo = lista[-1]
        
        # Divide os elementos em três grupos em relação ao pivô
        esquerda = [x for x in lista[:-1] if x <= pivo]
        direita  = [x for x in lista[:-1] if x > pivo]
        
        # Ordena recursivamente as sublistas e junta com o pivô no meio
        return quick_sort(esquerda) + [pivo] + quick_sort(direita)

    lista_curta = quick_sort(lista1)
    fim = time.time()
    total = fim - inicio

    print(f"\nPara até {len(lista1)} itens, o quick sort ordena a lista em cerca de: {total:.2f} seguds")

    lista_media = quick_sort(lista2)
    fim = time.time()
    total1 = fim - inicio

    print(f"\nPara até {len(lista2)} itens, o quick sort ordena a lista em cerca de: {total1:.2f} seguds")
 
    lista_grande = quick_sort(lista3)
    fim = time.time()
    total2 = fim - inicio

    print(f"\nPara até {len(lista3)} itens, o quick sort ordena a lista em cerca de: {total2:.2f} seguds")



def Heap_sort():

    lista1 = []
    lista2 = []
    lista3 = []

    # Geradores de listas compatíveis
    for i in range(50000): 
        lista1.append(random.randint(0,50000))

    for i in range(80000): 
        lista2.append(random.randint(0,80000))

    for i in range(100000): 
        lista3.append(random.randint(0,100000))

    inicio = time.time()
    def heapify(lista, n, i):
        # Inicializa o maior elemento como a raiz
        maior = i
        esquerda = 2 * i + 1  # Índice do filho da esquerda
        direita = 2 * i + 2   # Índice do filho da direita

        # Verifica se o filho da esquerda existe e é maior que a raiz
        if esquerda < n and lista[esquerda] > lista[maior]:
            maior = esquerda

        # Verifica se o filho da direita existe e é maior que o maior atual
        if direita < n and lista[direita] > lista[maior]:
            maior = direita

        # Se o maior não for a raiz, troca-os e continua o processo
        if maior != i:
            lista[i], lista[maior] = lista[maior], lista[i]
            # Aplica o heapify recursivamente na subárvore afetada
            heapify(lista, n, maior)

    def heap_sort(lista):
        n = len(lista)

        # Passo 1: Constrói o Max-Heap (reorganiza a lista)
        for i in range(n // 2 - 1, -1, -1):
            heapify(lista, n, i)

        # Passo 2: Extrai os elementos um a um do heap
        for i in range(n - 1, 0, -1):
            # Move a raiz atual (maior elemento) para o fim da lista
            lista[i], lista[0] = lista[0], lista[i]
            # Recalcula o Max-Heap para a árvore restante
            heapify(lista, i, 0)
            
        return lista

    lista_curta = heap_sort(lista1)
    fim = time.time()
    total = fim - inicio

    print(f"\nPara até {len(lista1)} itens, o heap sort ordena a lista em cerca de: {total:.2f} seguds")

    lista_media = heap_sort(lista2)
    fim = time.time()
    total1 = fim - inicio

    print(f"\nPara até {len(lista2)} itens, o heap sort ordena a lista em cerca de: {total1:.2f} seguds")
 
    lista_grande = heap_sort(lista3)
    fim = time.time()
    total2 = fim - inicio

    print(f"\nPara até {len(lista3)} itens, o heap sort ordena a lista em cerca de: {total2:.2f} seguds")



def Counting_sort():
     
    lista1 = []
    lista2 = []
    lista3 = []

    # Geradores de listas compatíveis
    for i in range(50000): 
        lista1.append(random.randint(0,50000))

    for i in range(80000): 
        lista2.append(random.randint(0,80000))

    for i in range(100000): 
        lista3.append(random.randint(0,100000))

    inicio = time.time()
    def counting_sort(lista):
        if not lista:
            return lista

        # Encontra o maior elemento para definir o tamanho do array de contagem
        max_val = max(lista)
        
        # Cria o array de contagem preenchido com zeros
        contagem = [0] * (max_val + 1)
        
        # Conta a frequência de cada número
        for num in lista:
            contagem[num] += 1
            
        # Reconstrói a lista original de forma ordenada
        lista_ordenada = []
        for i in range(len(contagem)):
            # Adiciona o número 'i', 'contagem[i]' vezes na lista final
            lista_ordenada.extend([i] * contagem[i])
            
        return lista_ordenada

    lista_curta = counting_sort(lista1)
    fim = time.time()
    total = fim - inicio

    print(f"\nPara até {len(lista1)} itens, o counting sort ordena a lista em cerca de: {total:.2f} seguds")

    lista_media = counting_sort(lista2)
    fim = time.time()
    total1 = fim - inicio

    print(f"\nPara até {len(lista2)} itens, o counting sort ordena a lista em cerca de: {total1:.2f} seguds")
 
    lista_grande = counting_sort(lista3)
    fim = time.time()
    total2 = fim - inicio

    print(f"\nPara até {len(lista3)} itens, o counting sort ordena a lista em cerca de: {total2:.2f} seguds")



def Radix_sort():
    
    lista1 = []
    lista2 = []
    lista3 = []

    # Geradores de listas compatíveis
    for i in range(50000): 
        lista1.append(random.randint(0,50000))

    for i in range(80000): 
        lista2.append(random.randint(0,80000))

    for i in range(100000): 
        lista3.append(random.randint(0,100000))

    inicio = time.time()
    def counting_sort_para_radix(lista, exp):
        n = len(lista)
        saida = [0] * n
        contagem = [0] * 10 # Base 10 (algarismos de 0 a 9)

        # Armazena a contagem das ocorrências do dígito atual
        for i in range(n):
            indice = (lista[i] // exp) % 10
            contagem[indice] += 1

        # Altera contagem[i] para que ele contenha a posição real
        # deste dígito no vetor de saída
        for i in range(1, 10):
            contagem[i] += contagem[i - 1]

        # Constrói o vetor de saída de trás para frente (garante estabilidade)
        i = n - 1
        while i >= 0:
            indice = (lista[i] // exp) % 10
            saida[contagem[indice] - 1] = lista[i]
            contagem[indice] -= 1
            i -= 1

        # Copia o vetor de saída para a lista original
        for i in range(n):
            lista[i] = saida[i]

    def radix_sort(lista):
        if not lista:
            return lista

        # Encontra o valor máximo para saber a quantidade de dígitos
        max_val = max(lista)

        # Executa o Counting Sort para cada dígito. 
        # 'exp' muda de 1 (unidade) para 10 (dezena), 100 (centena), etc.
        exp = 1
        while max_val // exp > 0:
            counting_sort_para_radix(lista, exp)
            exp *= 10
            
        return lista

    lista_curta = radix_sort(lista1)
    fim = time.time()
    total = fim - inicio

    print(f"\nPara até {len(lista1)} itens, o radix sort ordena a lista em cerca de: {total:.2f} seguds")

    lista_media = radix_sort(lista2)
    fim = time.time()
    total1 = fim - inicio

    print(f"\nPara até {len(lista2)} itens, o radix sort ordena a lista em cerca de: {total1:.2f} seguds")
 
    lista_grande = radix_sort(lista3)
    fim = time.time()
    total2 = fim - inicio

    print(f"\nPara até {len(lista3)} itens, o radix sort ordena a lista em cerca de: {total2:.2f} seguds")



def Bucket_sort():

    lista1 = []
    lista2 = []
    lista3 = []

    # Geradores de listas compatíveis
    for i in range(10000): 
        lista1.append(random.randint(0,50000))

    for i in range(15000): 
        lista2.append(random.randint(0,80000))

    for i in range(20000): 
        lista3.append(random.randint(0,100000))

    inicio = time.time()
    def insertion_sort(balde):
        # Algoritmo auxiliar estável para ordenar cada balde individualmente
        for i in range(1, len(balde)):
            chave = balde[i]
            j = i - 1
            while j >= 0 and balde[j] > chave:
                balde[j + 1] = balde[j]
                j -= 1
            balde[j + 1] = chave
        return balde

    def bucket_sort(lista):
        if not lista:
            return lista

        # 1. Cria 'n' baldes vazios, onde n é o tamanho da lista
        num_baldes = len(lista)
        baldes = [[] for _ in range(num_baldes)]

        # 2. Distribui os elementos nos baldes baseando-se no valor absoluto
        for num in lista:
            # A fórmula define em qual balde o número decimal vai cair
            indice_balde = int(num_baldes * num)
            # Evita estouro de índice caso o número seja exatamente 1.0
            if indice_balde >= num_baldes:
                indice_balde = num_baldes - 1
            baldes[indice_balde].append(num)

        # 3. Ordena os baldes individualmente e concatena o resultado
        lista_ordenada = []
        for balde in baldes:
            balde_ordenado = insertion_sort(balde)
            lista_ordenada.extend(balde_ordenado)

        return lista_ordenada

    lista_curta = bucket_sort(lista1)
    fim = time.time()
    total = fim - inicio

    print(f"\nPara até {len(lista1)} itens, o bucket sort ordena a lista em cerca de: {total:.2f} seguds")

    lista_media = bucket_sort(lista2)
    fim = time.time()
    total1 = fim - inicio

    print(f"\nPara até {len(lista2)} itens, o bucket sort ordena a lista em cerca de: {total1:.2f} seguds")
 
    lista_grande = bucket_sort(lista3)
    fim = time.time()
    total2 = fim - inicio

    print(f"\nPara até {len(lista3)} itens, o bucket sort ordena a lista em cerca de: {total2:.2f} seguds")



while True:
    
    print("\n=== Algoritmos de ordenação ===\n")
    print("1- Selection sort")
    print("2- Buble sort")
    print("3- Inserton sort")
    print("4- Merge sort")
    print("5- Quick sort")
    print("6- Heap sort")
    print("7- Counting sort")
    print("8- Radix sort")
    print("9- Bucket sort")
    print("0- Sair\n")

    a= True
    while a:
        try:
            entry = int(input("Escolha uma opção: "))
            if entry > 9 or entry < 0:
                print("Entrada inválida! digite um numero entre 0 - 9")
                a= True
            else:
                a= False
        except ValueError:
            print("Não digite letras! tente novamente.")
            a= True

    if entry == 1:
        Selection_sort()
    elif entry == 2:
        Bubble_sort()
    elif entry == 3:
        Insertion_sort()
    elif entry == 4:
        Merge_sort()
    elif entry == 5:
        Quick_sort()
    elif entry == 6:
        Heap_sort()
    elif entry == 7:
        Counting_sort()
    elif entry == 8:
        Radix_sort()
    elif entry == 9:
        Bucket_sort()
    elif entry == 0:
        print("Encerrando...")
        break   
