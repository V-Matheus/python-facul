n = int(input('Digite a quantidade de números: '))
i = int(input('Digite o primeiro valor: '))
j = int(input('Digite o segundo valor: '))
x = 0

if n != 0 or i != 0 or j != 0:
    while x < n:
        print(f'{x * j * i}', end=', ')
        x += 1
    
else: 
    print('digite um valor positivo')

