# =============================================
# Exercício 7 - Busca Sequencial com try/except
# =============================================
# Enunciado: Corrija a função para converter a matrícula e realizar a busca sequencial tratando erros.
 
alunos = [
    {"matricula": 1001, "nome": "Ana"},
    {"matricula": 1002, "nome": "Bruno"}
]
 
def buscar_por_matricula(mat):
    try:
        mat = int(mat)
    except ValueError:
        print("Matrícula deve ser número!")
        return 
 
    for aluno in alunos:
        if aluno["matricula"] == mat:
            return aluno["nome"]
    return "Aluno não encontrado"
 
print(buscar_por_matricula("1001"))
print(buscar_por_matricula("abc"))