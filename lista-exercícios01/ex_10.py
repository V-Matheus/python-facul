from re import I


cateto1 = float(input('Digite o valor do primeiro cateto: '))
cateto2 = float(input('Digite o valor do segundo cateto: '))
h = (cateto1**2 + cateto2**2)**0.5

if cateto1 > 0 and cateto2 > 0:
    print(f'A hipotenuza do {cateto1} e {cateto2} é igual a {h:.2f}')