frase = input('Digite uma frase: ')
carcter = input('Digite um caracter: ')
n = 0
position = 1
for letra in frase:
  if(letra.lower() == carcter.lower()):
    n += 1
    print(position, end=', ')
  position += 1
print(n)