x = int(input('Digite um número: '))

if x % 2 == 0:
    if x > 0:
        print('O número é par positivo')
    else:
        print('O número é par negativo')
elif x % 2 == 1:
    if x > 0:
        print('O número é impar positivo')
    else:
        print('O número é impar negativo')
else:
    print('O número é nulo')
