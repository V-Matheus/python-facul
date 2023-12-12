import random

# Solicitar ao usuário a quantidade de listas e elementos
qtd_listas = int(input("Digite a quantidade de listas na matriz: "))
qtd_elementos = int(input("Digite a quantidade de elementos em cada lista: "))

# Criar matriz aleatória
matriz_original = [[random.randint(1, 10) for _ in range(qtd_elementos)] for _ in range(qtd_listas)]

# Exibir matriz original
print("Matriz Original:")
for linha in matriz_original:
    print(linha)

# Calcular e exibir matriz transposta
 # Ele seleciona as linhas 'l' e colunas 'c' e substitui esses valores
matriz_transposta = [[matriz_original[l][c] for l in range(len(matriz_original))] for c in range(len(matriz_original[0]))]

print("Matriz Transposta:")
for linha in matriz_transposta:
    print(linha)
