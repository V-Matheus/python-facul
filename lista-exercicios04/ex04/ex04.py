from lista_palavras import lstPalavras

# Solicitando uma palavra ao usuário
palavra_procurada = input("Digite uma palavra: ")

# Inicializando os índices de busca
esquerda, direita = 0, len(lstPalavras) - 1

encontrou = False
while esquerda <= direita:
  # Irá cortar a lista no meio
    meio = (esquerda + direita) // 2
    palavra_meio = lstPalavras[meio]

  # Se achar a palavra encerra o loop, caso não irá verificar se a palavra está a direita ou a esquerda em comparação ao meio
    if palavra_meio == palavra_procurada:
        encontrou = True
        break
    elif palavra_procurada < palavra_meio:
        direita = meio - 1
    else:
        esquerda = meio + 1

if encontrou:
    print(f'A palavra "{palavra_procurada}" está na posição {meio}.')
else:
    print(f'A palavra "{palavra_procurada}" não está na lista.')
