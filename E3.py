# =============================================
# Exercício 3 - Validação de Entrada com try/except
# =============================================
# Enunciado: Corrija a função para ler uma quantidade do usuário.
# Deve tratar erros de entrada e repetir até receber um número válido.

def ler_quantidade():
    while True:
        try:
            qtd = int(input("Quantidade: "))
            return qtd
        except ValueError:
            print("Erro! Digite apenas números.")

print("Quantidade válida:", ler_quantidade())
