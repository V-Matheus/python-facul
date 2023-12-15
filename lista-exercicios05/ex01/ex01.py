from ctypes import pointer
import requests, os
from datetime import date
strURL = 'https://api.cartolafc.globo.com/atletas/mercado'
dictCartola = requests.get(strURL, verify=False).json()


atletas = dictCartola.get('atletas')
atleta = {'nome': '', 'num': 0, 'media': 0, 'pontuacao': 0}


for atleta in atletas:
  jogos_num = atletas[atleta]['jogos_num']
  media_num = atletas[atleta]['media_num']
  maior_pontuacao = jogos_num * media_num

  # atletas[atleta]['jogos_num'] += dicionario
  print(maior_pontuacao)

# print(jogos_num, media_num)
# print(f'\n')




# while True:
#   ano = int(input('Digite o ano que deseja: '))
#   if(ano == int(date.today().year)):
#     break


esquema_possiveis = [343, 352, 433, 442, 451, 532, 541]
# print(ano)
