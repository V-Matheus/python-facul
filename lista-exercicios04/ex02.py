import random
n = int(input('Digite o tamanho da lista: '))

listaRandom = [random.randint(0,99) for _ in range(n)]
print(f'Lista original: {listaRandom}')

# for i in range(1, len(listaRandom)):
#     key = listaRandom[i]
#     j = i - 1
#     while j >= 0 and key < listaRandom[j]:
#         listaRandom[j + 1] = listaRandom[j]
#         j -= 1
#     listaRandom[j + 1] = key
# print("Lista Ordenada:", listaRandom)