x = int(input('Informe a quantidade de elementos na lista: '))
lista = list()

while True:
  n = int(input('Inform um valor: '))
  lista.append(n)
  lista.sort()
  print(lista)
  if n == 0:
    break
  if len(lista) + 1 > x:
    del lista[-1]