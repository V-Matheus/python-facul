
gabarito = ['A', 'C', 'B', 'A', 'E', 'D', 'D', 'C', 'A', 'A']

lista_alunos = [
    ['Aluno 01', 'B', 'D', 'E', 'E', 'C', 'D', 'A', 'B', 'C', 'D'],
    ['Aluno 02', 'C', 'D', 'A', 'B', 'D', 'A', 'A', 'C', 'B', 'E'],
    ['Aluno 03', 'A', 'A', 'B', 'D', 'C', 'E', 'E', 'A', 'A', 'C'],
    ['Aluno 04', 'B', 'B', 'C', 'C', 'D', 'E', 'D', 'D', 'E', 'E'],
    ['Aluno 05', 'B', 'B', 'D', 'A', 'A', 'E', 'B', 'D', 'E', 'C'],
    ['Aluno 06', 'C', 'C', 'D', 'E', 'B', 'B', 'C', 'D', 'E', 'A'],
    ['Aluno 07', 'B', 'A', 'A', 'B', 'B', 'C', 'D', 'E', 'A', 'B'],
    ['Aluno 08', 'D', 'E', 'A', 'B', 'B', 'C', 'C', 'D', 'A', 'A'],
    ['Aluno 09', 'A', 'A', 'A', 'C', 'B', 'D', 'D', 'E', 'D', 'C'],
    ['Aluno 10', 'B', 'B', 'D', 'E', 'C', 'D', 'C', 'E', 'B', 'A'],
]

lista_gabarito = gabarito.copy()
acertos = 0

# Calcula a quantidade de acertos
    # Criei uma biblioteca com as chaves 'aluno', na qual recebe o primeiro item de cada lista,
    # e 'acertos', primeiro compara a resposta do gabarito com a resposta do aluno e soma sempre que isso acontecer
    # e irá fazer isso para todos os alunos
lista_alunos_acertos = [{'aluno': aluno[0], 'acertos': sum(resposta_gabarito == resposta_aluno for resposta_gabarito, resposta_aluno in zip(gabarito, aluno[1:]))} for aluno in lista_alunos]

# Ordena a lista de alunos
    # Ordenei usando lambda, na qual ordena de acordo com a quaantidade de acertos e coloca de forma decrescente com o reverse
lista_alunos_ordenada = sorted(lista_alunos_acertos, key=lambda x: x['acertos'], reverse=True)

# Imprime a lista ordenada
for aluno in lista_alunos_ordenada:
    print(f"{aluno['aluno']} - acertos: {aluno['acertos']}")
