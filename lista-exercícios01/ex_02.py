temperatura = float(input('Digite o valor da temperatura em Celsius: '))
if temperatura > 0:
    fahrenheit = float(((temperatura * 9) + 160)/5)
    print(f'O valor {temperatura} convertido para Fahrenheit é {fahrenheit}')
else: 
    print('Digite um valor acima de 0')