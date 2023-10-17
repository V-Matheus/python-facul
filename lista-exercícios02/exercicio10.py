n = int(input('Digite um valor: '))
resultado = ''
if n > 0:
  while n > 0:
    resto = n % 2
    resultado = str(resto) + resultado
    n = n // 2
  print(resultado)
else:
  print('Digite um valor positivo')
