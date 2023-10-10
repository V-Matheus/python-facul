while True:
  inicial = int(input('Indique o valor inicial da P.A: '))
  razao = int(input('Indique o valor da razão da P.A: '))
  qElementos = int(input('Indique a quantidade de elementos da P.A: '))
  x = (inicial+razao)*qElementos

  if inicial >= 1 and qElementos > 0:
    soma = (qElementos * (inicial + x)) /2
    while x > 0:
      x = x - razao
      if razao > x:
        break
      print(f'Os valores da P.A é, {x}')
    
    print(f'A soma dessa P.A é {soma}')

    if(razao == 0):
        print(f'A razão é constante \n ')
        
    elif(razao > 0):
        print('A razão é crescente')
    elif (razao < 0):
      print('A razão é decrescente')
  else:
    print('Digite um valor positivo')
    break
 

 # (inicial  inicial *2  inicial*3)  == qElementos