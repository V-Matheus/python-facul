from turtle import pos
import requests, os
from datetime import date


# Criando o Json
strURL = 'https://api.cartolafc.globo.com/atletas/mercado'
dictCartola = requests.get(strURL, verify=False).json()
atletas = dictCartola.get('atletas')

maiores_pontuacoes = {}
posicoes = {1: 'goleiro', 2: 'lateral', 3: 'zagueiro', 4: 'meia', 5: 'atacante', 6: 'tecnico'}

# Puxando informações do Json
for atleta in atletas:
    nome = atleta['nome']
    posicao_id = atleta['posicao_id']
    jogos_num = atleta['jogos_num']
    media_num = atleta['media_num']
    maior_pontuacao = round(jogos_num * media_num, 2)

    # Armazena a maior pontuação para cada jogador no dicionário maiores_pontuacoes
    maiores_pontuacoes[nome] = {'pontuacao': maior_pontuacao, 'posicao': posicoes[posicao_id]}

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
    posicao = info['posicao']

    # Adicionar o jogador ao dicionário da posição correspondente
    if posicao == 'goleiro':
        melhores_goleiros[jogador] = info['pontuacao']
    elif posicao == 'lateral':
        melhores_laterais[jogador] = info['pontuacao']
    elif posicao == 'zagueiro':
        melhores_zagueiros[jogador] = info['pontuacao']
    elif posicao == 'meia':
        melhores_meias[jogador] = info['pontuacao']
    elif posicao == 'atacante':
        melhores_atacantes[jogador] = info['pontuacao']
    elif posicao == 'tecnico':
        melhores_tecnicos[jogador] = info['pontuacao']

esquema_possiveis = [343, 352, 433, 442, 451, 532, 541]


# Exibir Resultados

while  True:
    esquema = int(input(f'Escolha um esquema tático: \n {esquema_possiveis}\n'))
    melhor_goleiro = list(melhores_goleiros.keys())[:1]
    melhor_tecnico = list(melhores_tecnicos.keys())[:1]

    if esquema not in esquema_possiveis: 
        print('Digite um esquema válido')
        continue
    else:
            print(f'Os melhores jogadores para esse esquema tático são:\n')
            if esquema == 343:
                melhores_zagueiros_343 = list(melhores_zagueiros.keys())[:3]
                print(f'zagueiros: {melhores_zagueiros_343}\n')

                melhores_meias_343 = list(melhores_meias.keys())[:3]
                print(f'meias: {melhores_meias_343}\n')

                melhores_atacantes_343 = list(melhores_atacantes.keys())[:3]
                print(f'atacantes: {melhores_atacantes_343}\n')

                print(f'goleiro: {melhor_goleiro}\n')

                print(f'tecnico: {melhor_tecnico}\n')
                break

            if esquema == 352:
                melhores_zagueiros_352 = list(melhores_zagueiros.keys())[:3]
                print(f'zagueiros: {melhores_zagueiros_352}\n')

                melhores_meias_352 = list(melhores_meias.keys())[:5]
                print(f'meias: {melhores_meias_352}\n')

                melhores_atacantes_352 = list(melhores_atacantes.keys())[:2]
                print(f'atacantes: {melhores_atacantes_352}\n')

                print(f'goleiro: {melhor_goleiro}\n')

                print(f'tecnico: {melhor_tecnico}\n')
                break

            if esquema == 433:
                melhores_zagueiros_433 = list(melhores_zagueiros.keys())[:2]
                print(f'zagueiros: {melhores_zagueiros_433}\n')

                melhores_laterais_433 = list(melhores_laterais.keys())[:2]
                print(f'laterais: {melhores_laterais_433}\n')

                melhores_meias_433 = list(melhores_meias.keys())[:3]
                print(f'meias: {melhores_meias_433}\n')

                melhores_atacantes_433 = list(melhores_atacantes.keys())[:3]
                print(f'atacantes: {melhores_atacantes_433}\n')

                print(f'goleiro: {melhor_goleiro}\n')

                print(f'tecnico: {melhor_tecnico}\n')
                break

            if esquema == 442:
                melhores_zagueiros_442 = list(melhores_zagueiros.keys())[:2]
                print(f'zagueiros: {melhores_zagueiros_442}\n')

                melhores_laterais_442 = list(melhores_laterais.keys())[:2]
                print(f'laterais: {melhores_laterais_442}\n')

                melhores_meias_442 = list(melhores_meias.keys())[:4]
                print(f'meias: {melhores_meias_442}\n')

                melhores_atacantes_442 = list(melhores_atacantes.keys())[:2]
                print(f'atacantes: {melhores_atacantes_442}\n')

                print(f'goleiro: {melhor_goleiro}\n')

                print(f'tecnico: {melhor_tecnico}\n')
                break

            if esquema == 451:
                melhores_zagueiros_451 = list(melhores_zagueiros.keys())[:2]
                print(f'zagueiros: {melhores_zagueiros_451}\n')

                melhores_laterais_451 = list(melhores_laterais.keys())[:2]
                print(f'laterais: {melhores_laterais_451}\n')

                melhores_meias_451 = list(melhores_meias.keys())[:5]
                print(f'meias: {melhores_meias_451}\n')

                melhores_atacantes_451 = list(melhores_atacantes.keys())[:1]
                print(f'atacantes: {melhores_atacantes_451}\n')

                print(f'goleiro: {melhor_goleiro}\n')

                print(f'tecnico: {melhor_tecnico}\n')
                break

            if esquema == 532:
                melhores_zagueiros_532 = list(melhores_zagueiros.keys())[:3]
                print(f'zagueiros: {melhores_zagueiros_532}\n')

                melhores_laterais_532 = list(melhores_laterais.keys())[:2]
                print(f'laterais: {melhores_laterais_532}\n')

                melhores_meias_532 = list(melhores_meias.keys())[:3]
                print(f'meias: {melhores_meias_532}\n')

                melhores_atacantes_532 = list(melhores_atacantes.keys())[:2]
                print(f'atacantes: {melhores_atacantes_532}\n')

                print(f'goleiro: {melhor_goleiro}\n')

                print(f'tecnico: {melhor_tecnico}\n')
                break

            if esquema == 541:
                melhores_zagueiros_541 = list(melhores_zagueiros.keys())[:3]
                print(f'zagueiros: {melhores_zagueiros_541}\n')

                melhores_laterais_541 = list(melhores_laterais.keys())[:2]
                print(f'laterais: {melhores_laterais_541}\n')

                melhores_meias_541 = list(melhores_meias.keys())[:4]
                print(f'meias: {melhores_meias_541}\n')

                melhores_atacantes_541 = list(melhores_atacantes.keys())[:1]
                print(f'atacantes: {melhores_atacantes_541}\n')

                print(f'goleiro: {melhor_goleiro}\n')

                print(f'tecnico: {melhor_tecnico}\n')
                break
            
