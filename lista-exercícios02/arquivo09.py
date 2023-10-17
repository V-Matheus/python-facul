mensal = float(input('Informe o valor mensal a ser aplicado (R$): '))
taxa = (float(input('Informe a taxa de juros mensal (%): '))) / 100
x = 0
total = 0
ano = 1
if mensal > 0 or taxa > 0:
    while True:
        taxaValor = total * taxa
        total = total + mensal + taxaValor
        x += 1
        
        if x %12 == 0:
            print(f'O valor acumulado do {ano}º ano é (R$): {total:.2f}')
            op = input('Deseja calcular mais um ano (S/N)?')
            op.lower()
            ano += 1

            if op == 'n':
                break
else:
    print('Digite um valor positivo')
