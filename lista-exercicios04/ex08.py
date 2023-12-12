import random
n = int(input('Digite o tamanho da lista: '))

lista = [random.randint(0,99) for _ in range(n)]
print(lista)

quadrante1 = list()
quadrante2 = list()
quadrante3 = list()
quadrante4 = list()

for i in lista:
  if 0 <= i <= 24:
    quadrante1.append(i)
  if 25 <= i <= 49:
    quadrante2.append(i)
  if 50 <= i <= 74:
    quadrante3.append(i)
  if 75 <= i <= 99:
    quadrante4.append(i)

if quadrante1:
  print(f'No 1º Quadrante tem os valores: {quadrante1}')

if quadrante2:
  print(f'No 2º Quadrante tem os valores: {quadrante2}')

if quadrante3:
  print(f'No 3º Quadrante tem os valores: {quadrante3}')

if quadrante4:
  print(f'No 4º Quadrante tem os valores: {quadrante4}')