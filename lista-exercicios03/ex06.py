variavel = str(input('digite o valor da variável: '))

x = 0
y = 1
while x <= len(variavel) * 2:
  x += y
  print(variavel[0:x])
  if variavel[0:x] == variavel:
    y = -1
  if x == 0:
    break