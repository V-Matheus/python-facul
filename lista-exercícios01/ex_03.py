ano = int(input('Digite um ano: '))
if ano > 0 and (ano % 4) == 0 or (ano % 100) == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')