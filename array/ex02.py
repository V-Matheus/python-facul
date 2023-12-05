# Fazer um programa que gere uma lista
# c/10 números lidos do teclado e no final imprima
contagem = 0
somaN = 0
lista = list()
while contagem < 10:
  n = int(input('Digite 10 números: '))
  lista.append(n)
  print(lista)
  contagem += 1
  somaN += n
media = somaN/10
print(f'O maior número é: {max(lista)}')
print(f'O menor número é: {min(lista)}')
print(f'A média é: {media}')