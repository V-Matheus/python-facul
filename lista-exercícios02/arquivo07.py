n = float(input('Digite um valor: '))
nFatorial = n
nInicial = n
if n > 0:
  while nFatorial > 1:
    nFatorial -= 1
    x = n * nFatorial
    n = x
  print(f'{nInicial}! = {x}')
elif n == 0:
  print('0! = 1')
else:
  print('Digite um valor positivo')