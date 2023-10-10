num = int(input('Digite um número: '))
numCalc = num

if(numCalc > 0):
  total = 0
  while numCalc > 1:
    div = 10
    x = numCalc / div
    div * 10
    numCalc = x
    y = int((float(x) - int(x)) * 10)
    cal = (y ** 3)
    total += cal
  if total == num:
    print('Esse é um némero de Armstrong')
  else: 
    print('Não é um número de Armstrong')
else: 
  print('Digite um valor positivo')
