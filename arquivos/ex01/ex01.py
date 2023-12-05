from lstCapitais import lstCapitais

arqSaida = open('./python-facul/arquivos/ex01/nordeste.txt', 'w', encoding='utf-8')

popTotal = 0
for cidade in lstCapitais:
  arqSaida.write(f'{cidade[1]}/{cidade[0]}:{cidade[2]}\n')
  popTotal += cidade[2]

arqSaida.write(f'\nPopulação total:{popTotal}')
arqSaida.close()