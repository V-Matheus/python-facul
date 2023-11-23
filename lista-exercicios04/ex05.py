import random
n = int(input('Digite o tamanho da lista: '))

lista = [random.randint(0,9) for _ in range(n)]
print(lista)
contagem = [lista.count(i) for i in range(n)]

for i in range(n):
  if contagem[i] != 0:
    print(f"Número {i}: {contagem[i]} ocorrência(s)")