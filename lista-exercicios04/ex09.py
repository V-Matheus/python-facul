import enum
import random
# n = int(input('Digite o tamanho da lista: '))

# lista = [random.randint(0,999) for _ in range(n)]
lista = [1,2,3,4,5,6,7,8,9,9,9]

v = int(input('Digite um valor: '))
print()

if v in lista:
  print('O valor conta na lista')
  indexs = [index for index, elemento in enumerate(lista) if elemento == v]
  print(f'O valor aparece {lista.count(v)} vezes e nas posições {indexs}')
else:
  print('O valor não consta na lista')