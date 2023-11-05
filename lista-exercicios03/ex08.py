string = input('Digite uma palavra ou frase: ')
vogais = 'aeiouáéíóúâêîôûãõ'
quantidade = 0

for letra in string.lower():
  if(letra in vogais):
    quantidade += 1
print(f'Existe {quantidade} vogais nessa string')