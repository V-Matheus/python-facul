frase = input('Digite uma frase: ').lower().replace(' ', '').replace('-', '')
fraseInvertida = frase[::-1]

if frase == fraseInvertida:
  print('Essa frase é um palíndromo')