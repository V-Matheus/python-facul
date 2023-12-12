import random
n = int(input('Digite o tamanho da lista: '))

listaRandom = [random.randint(0,99) for _ in range(n)]
print(f'Lista original: {listaRandom}')

for i in range(len(listaRandom)):
    for j in range(0, len(listaRandom)-i-1):
      # Verica se o número atual é maior que o próximo número
        if listaRandom[j] > listaRandom[j+1]:
            # Troca os elementos se estiverem fora de ordem
            listaRandom[j], listaRandom[j+1] = listaRandom[j+1], listaRandom[j]

print("Lista Ordenada:", listaRandom)