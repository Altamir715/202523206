# =============================================
# Exercício 9 - Relatório de Vendas com Dicionário
# =============================================
# Enunciado: Corrija o cálculo do total de vendas tratando possíveis erros de conversão.

vendas_dia = {"Notebook": "2500", "Mouse": 80, "Teclado": "150"}

def total_vendas(vendas):
    total = 0.0
    for produto, valor in vendas.items():
        try:
            total += float(valor)
        except (ValueError, TypeError):
            print(f"Aviso: valor inválido para {produto}: {valor}")
            continue
    return total

print("Total de vendas:", total_vendas(vendas_dia))