valor = float(input('Digite um valor para sacar: '))

if(valor > 0):
  centavos = int(valor * 100)

  notas100 = centavos // 10000
  centavos = centavos % 10000

  notas50 = centavos // 5000
  centavos = centavos % 5000

  notas20 = centavos // 2000
  centavos = centavos % 2000

  notas10 = centavos // 1000
  centavos = centavos % 1000

  notas5 = centavos // 500
  centavos = centavos % 500

  notas2 = centavos // 200
  centavos = centavos % 200

  moeda1 = centavos // 100
  centavos = centavos % 100

  moeda05 = centavos // 50
  centavos = centavos % 50

  moeda025 = centavos // 25
  centavos = centavos % 25

  moeda010 = centavos // 10
  centavos = centavos % 10

  moeda005 = centavos // 5
  centavos = centavos % 5

  moeda001 = centavos

  if notas100 > 0:
    print(f'Com esse valor vocé conseguirá sacar {notas100} nota(s) de R$ 100,00')

  if notas50 > 0:
    print(f'Com esse valor vocé conseguirá sacar {notas50} nota(s) de R$ 50,00')
    
  if notas20 > 0:
    print(f'Com esse valor vocé conseguirá sacar {notas20} nota(s) de R$ 20,00')

  if notas10 > 0:
    print(f'Com esse valor vocé conseguirá sacar {notas10} nota(s) de R$ 10,00')

  if notas5 > 0:
    print(f'Com esse valor vocé conseguirá sacar {notas5} nota(s) de R$ 5,00')

  if notas2 > 0:
    print(f'Com esse valor vocé conseguirá sacar {notas2} nota(s) de R$ 2,00')

  if moeda1 > 0:
    print(f'Com esse valor vocé conseguirá sacar {moeda1} moeda(s) de R$ 1,00')

  if moeda05 > 0:
    print(f'Com esse valor vocé conseguirá sacar {moeda05} moeda(s) de R$ 0,50')

  if moeda025 > 0:
    print(f'Com esse valor vocé conseguirá sacar {moeda025} moeda(s) de R$ 0,25')

  if moeda010 > 0:
    print(f'Com esse valor vocé conseguirá sacar {moeda010} moeda(s) de R$ 0,10')

  if moeda010 > 0:
    print(f'Com esse valor vocé conseguirá sacar {moeda001} moeda(s) de R$ 0,01')  

else:
  print('Digite um valor válido')

