n = int(input('informe um valor: '))

listPares = [i for i in range(1, n*2 +1) if i%2 == 0]
print(listPares)