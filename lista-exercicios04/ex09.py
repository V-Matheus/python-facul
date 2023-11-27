import random

n = int(input('Digite o tamanho da lista: '))
lista = [random.randint(0,999) for _ in range(n)]

numero = int(input('Digite um valor: '))

if numero in lista:
  print('O valor consta na lista')
# Verifica em cada item da lista se o número está presente e se estiver entrega o valor e o seu index
  indexs = [index for index, elemento in enumerate(lista) if elemento == numero]
  print(f'O valor aparece {lista.count(numero)} vezes e nas posições {indexs}')
else:
  print('O valor não consta na lista')