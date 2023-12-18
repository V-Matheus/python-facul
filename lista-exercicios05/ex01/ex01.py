from turtle import pos
import requests, os
from datetime import date

strURL = 'https://api.cartolafc.globo.com/atletas/mercado'
dictCartola = requests.get(strURL, verify=False).json()

atletas = dictCartola.get('atletas')
maiores_pontuacoes = {}
posicoes = {1: 'goleiro', 2: 'lateral', 3: 'zagueiro', 4: 'meia', 5: 'atacante', 6: 'Técnico'}

for atleta in atletas:
    nome = atleta['nome']
    posicao_id = atleta['posicao_id']
    jogos_num = atleta['jogos_num']
    media_num = atleta['media_num']
    maior_pontuacao = round(jogos_num * media_num, 2)

   # Cria um novo dicionário para cada jogador
    info_jogador = {'nome': nome, 'posicao': posicoes[posicao_id]}

    # Armazena a maior pontuação para cada jogador no dicionário maiores_pontuacoes
    maiores_pontuacoes[nome] = {'pontuacao': maior_pontuacao, 'info_jogador': info_jogador}

# Ordena os jogadores por maior pontuação
melhores_atletas = sorted(maiores_pontuacoes.items(), key=lambda x: x[1]['pontuacao'], reverse=True)

# Criar dicionários separados para cada posição
melhores_goleiros = {}
melhores_laterais = {}
melhores_zagueiros = {}
melhores_meias = {}
melhores_atacantes = {}
melhores_tecnicos = {}

# Iterar sobre os melhores jogadores
for jogador, info in melhores_atletas:
    posicao = info['info_jogador']['posicao']

    # Adicionar o jogador ao dicionário da posição correspondente
    if posicao == 'goleiro':
        melhores_goleiros[jogador] = info
    elif posicao == 'lateral':
        melhores_laterais[jogador] = info
    elif posicao == 'zagueiro':
        melhores_zagueiros[jogador] = info
    elif posicao == 'meia':
        melhores_meias[jogador] = info
    elif posicao == 'atacante':
        melhores_atacantes[jogador] = info
    elif posicao == 'Técnico':
        melhores_tecnicos[jogador] = info

esquema_possiveis = [343, 352, 433, 442, 451, 532, 541]
