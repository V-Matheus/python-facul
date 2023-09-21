angulo1 = float(input('Informe o angulo 1: '))
angulo2 = float(input('Informe o angulo 2: '))
angulo3 = float(input('Informe o angulo 3: '))

if angulo1 + angulo2 + angulo3 == 180 and angulo1 > 0 and angulo2 > 0 and angulo3 > 0: 
    if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        print('O triangulo é um Triângulo acutângulo')
    elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print('O triangulo é um Triângulo retângulo')
    else: 
        print('O triangulo é um Triângulo obtusângulo')
else:
    print('Informe dados válidos')