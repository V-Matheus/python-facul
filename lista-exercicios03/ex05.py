fraseOriginal = input('Digite a frase: ')
palavraChave = input('Digite a palavra-chave: ')
palavraChaveRepeat = palavraChave.lower()
fraseOriginalRepeat = fraseOriginal.lower()

#  Faz que a palavra-chave tenha a mesma quantidade de caracteres da fraseOriginal
while len(palavraChaveRepeat) < len(fraseOriginal):
  palavraChaveRepeat += palavraChave
palavraChaveRepeat = palavraChaveRepeat[:len(fraseOriginal)]

# Pegando o valor do index de cada letra do alfabeto// ex: a = 0, b = 1 c = 2
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
i = 0
valorPalavraChave = 0
valorFraseOriginal = 0
somaIndex = ''
criptografia = ''

for caractere in alfabeto:
  for letra in palavraChaveRepeat:
    if caractere == letra:
      valorPalavraChave += i

  for letra in fraseOriginalRepeat:
    if caractere == letra:
      valorFraseOriginal += i

  # Somando os valores de index da palavra-chave e a fraseOriginal
  somaIndex = valorFraseOriginal + valorPalavraChave
  if somaIndex > 25:
    somaIndex = 0
  i += 1
  
criptografia += alfabeto[somaIndex]
print(criptografia)


# depois de muitas tentativas esse foi o resultado que consegui, mas ainda incompleto 