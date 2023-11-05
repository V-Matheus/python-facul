PALAVRA_CHAVE = 'forca'
tentativas = 6
ocultarPalavra = ''
acertos = ''

while tentativas > 0:
  resposta = input('Digite uma letra: ').lower()
  if(resposta in PALAVRA_CHAVE):
    print('tem essa letra')
    acertos += resposta
    ocultarPalavra = ''
    for letra in PALAVRA_CHAVE:
      if letra in acertos:
        ocultarPalavra += letra
      else:
        ocultarPalavra += '_'
    print(f'Palavra: {ocultarPalavra}')
  else:
    print('Essa letra não tem')
    tentativas -= 1
    print(f'Você tem: {tentativas} tentativas')

print('Perdeu')