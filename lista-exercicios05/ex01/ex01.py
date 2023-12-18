import requests, datetime, os, sys, json


strURL = 'https://api.cartolafc.globo.com/atletas/mercado'
strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)

# Obter o ano atual
while True:
    try:
        ano = int(input(f"Escolha um ano (0 para sair): "))
        if ano == 0:
            print("Saindo do programa!")
            sys.exit()
        elif ano == datetime.datetime.now().year:
            dictCartola = requests.get(strURL, verify=True).json()
            break
        else:
            strNomeArq = strDiretorio + f'\\cartola_fc_{ano}.json'
            dictOpen = open(strNomeArq,'r',encoding='UTF-8')
            dictCartola = dictOpen.read()
            dictCartola = json.loads(dictCartola)
            dictOpen.close()
            break
    except ValueError:
        print("\nERROR: O valor informado precisa ser inteiro de base10!")
        continue
    except FileNotFoundError:
        print("\nERROR: O ano desejado não possui arquivo!")
    except:
        print(f"\nERROR: {sys.exc_info()[0]}")

# Puxando informações dos clubes

clubes = dictCartola.get('clubes')
clubes_dic = {}
for id_clube, info_clube in clubes.items():
    nome_clube = info_clube['nome']
    clubes_dic[id_clube] = nome_clube

maiores_pontuacoes = {}
posicoes = {1: 'goleiro', 2: 'lateral', 3: 'zagueiro', 4: 'meia', 5: 'atacante', 6: 'tecnico'}

atletas = dictCartola.get('atletas')
# Puxando informações dos atletas
for atleta in atletas:
    nome = atleta['nome']
    apelido = atleta['apelido']
    clube_id = atleta['clube_id']
    clube = clubes_dic[str(clube_id)]
    posicao_id = atleta['posicao_id']
    jogos_num = atleta['jogos_num']
    media_num = atleta['media_num']
    maior_pontuacao = round(jogos_num * media_num, 2)

    # Armazena a maior pontuação para cada jogador no dicionário maiores_pontuacoes
    maiores_pontuacoes[nome] = {'pontuacao': maior_pontuacao, 'posicao': posicoes[posicao_id], 'apelido' : apelido, 'clube': clube}

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
        melhores_goleiros[jogador] = info
    elif posicao == 'lateral':
        melhores_laterais[jogador] = info
    elif posicao == 'zagueiro':
        melhores_zagueiros[jogador] = info
    elif posicao == 'meia':
        melhores_meias[jogador] = info
    elif posicao == 'atacante':
        melhores_atacantes[jogador] = info
    elif posicao == 'tecnico':
        melhores_tecnicos[jogador] = info

esquema_possiveis = [343, 352, 433, 442, 451, 532, 541]

# Exibir Resultados

while  True:
    esquema = int(input(f'Escolha um esquema tático: \n {esquema_possiveis}\n'))
    melhor_goleiro = {'nome': list(melhores_goleiros.keys())[1], 'info': list(melhores_goleiros.values())[1]}
    melhor_tecnico = {'nome': list(melhores_tecnicos.keys())[1], 'info': list(melhores_tecnicos.values())[1]}

    if esquema not in esquema_possiveis: 
        print('Digite um esquema válido')
        continue
    else:
            print(f'Os melhores jogadores para esse esquema tático são:\n')
            if esquema == 343:
                # x= 3
                print(f'goleiro: {melhor_goleiro["nome"]} - apelido: {melhor_goleiro["info"]["apelido"]} - pontuação: {melhor_goleiro["info"]["pontuacao"]} - clube: {melhor_goleiro["info"]["clube"]}\n')

                # Pega as informações + nome dos jogadores a partir de uma lista de valores e chaves dentro do dicionário
                for info_zagueiros, name_zagueiros in zip(list(melhores_zagueiros.values())[:3], list(melhores_zagueiros.keys())[:3]):
                    zagueiros_pontuacao = info_zagueiros['pontuacao']
                    zagueiros_apelido = info_zagueiros['apelido']
                    zagueiros_clube = info_zagueiros['clube']
                    print(f'zagueiro: {name_zagueiros} - apelido: {zagueiros_apelido} - pontuacao: {zagueiros_pontuacao}  - clube: {zagueiros_clube}\n')

                for info_meias, name_meias in zip(list(melhores_meias.values())[:4], list(melhores_meias.keys())[:4]):
                    meias_pontuacao = info_meias['pontuacao']
                    meias_apelido = info_meias['apelido']
                    meias_clube = info_meias['clube']
                    print(f'meias: {name_meias} - apelido: {meias_apelido} - pontuacao: {meias_pontuacao}  - clube: {meias_clube}\n')

                for info_atacantes, name_atacantes in zip(list(melhores_atacantes.values())[:3], list(melhores_atacantes.keys())[:3]):
                    atacantes_pontuacao = info_atacantes['pontuacao']
                    atacantes_apelido = info_atacantes['apelido']
                    atacantes_clube = info_atacantes['clube']
                    print(f'atacantes: {name_atacantes} - apelido: {atacantes_apelido} - pontuacao: {atacantes_pontuacao}  - clube: {atacantes_clube}\n')

                print(f'tecnico: {melhor_tecnico["nome"]} - apelido: {melhor_tecnico["info"]["apelido"]} - pontuação: {melhor_tecnico["info"]["pontuacao"]} - clube: {melhor_tecnico["info"]["clube"]}\n')
                break

            if esquema == 352:
                print(f'goleiro: {melhor_goleiro}\n')

                melhores_zagueiros_352 = list(melhores_zagueiros.keys())[:3]
                print(f'zagueiros: {melhores_zagueiros_352}\n')

                melhores_meias_352 = list(melhores_meias.keys())[:5]
                print(f'meias: {melhores_meias_352}\n')

                melhores_atacantes_352 = list(melhores_atacantes.keys())[:2]
                print(f'atacantes: {melhores_atacantes_352}\n')

                print(f'tecnico: {melhor_tecnico}\n')
                break

            if esquema == 433:
                print(f'goleiro: {melhor_goleiro}\n')

                melhores_zagueiros_433 = list(melhores_zagueiros.keys())[:2]
                print(f'zagueiros: {melhores_zagueiros_433}\n')

                melhores_laterais_433 = list(melhores_laterais.keys())[:2]
                print(f'laterais: {melhores_laterais_433}\n')

                melhores_meias_433 = list(melhores_meias.keys())[:3]
                print(f'meias: {melhores_meias_433}\n')

                melhores_atacantes_433 = list(melhores_atacantes.keys())[:3]
                print(f'atacantes: {melhores_atacantes_433}\n')

                print(f'tecnico: {melhor_tecnico}\n')
                break

            if esquema == 442:
                print(f'goleiro: {melhor_goleiro}\n')

                melhores_zagueiros_442 = list(melhores_zagueiros.keys())[:2]
                print(f'zagueiros: {melhores_zagueiros_442}\n')

                melhores_laterais_442 = list(melhores_laterais.keys())[:2]
                print(f'laterais: {melhores_laterais_442}\n')

                melhores_meias_442 = list(melhores_meias.keys())[:4]
                print(f'meias: {melhores_meias_442}\n')

                melhores_atacantes_442 = list(melhores_atacantes.keys())[:2]
                print(f'atacantes: {melhores_atacantes_442}\n')

                print(f'tecnico: {melhor_tecnico}\n')
                break

            if esquema == 451:
                print(f'goleiro: {melhor_goleiro}\n')

                melhores_zagueiros_451 = list(melhores_zagueiros.keys())[:2]
                print(f'zagueiros: {melhores_zagueiros_451}\n')

                melhores_laterais_451 = list(melhores_laterais.keys())[:2]
                print(f'laterais: {melhores_laterais_451}\n')

                melhores_meias_451 = list(melhores_meias.keys())[:5]
                print(f'meias: {melhores_meias_451}\n')

                melhores_atacantes_451 = list(melhores_atacantes.keys())[:1]
                print(f'atacantes: {melhores_atacantes_451}\n')

                print(f'tecnico: {melhor_tecnico}\n')
                break

            if esquema == 532:
                print(f'goleiro: {melhor_goleiro}\n')

                melhores_zagueiros_532 = list(melhores_zagueiros.keys())[:3]
                print(f'zagueiros: {melhores_zagueiros_532}\n')

                melhores_laterais_532 = list(melhores_laterais.keys())[:2]
                print(f'laterais: {melhores_laterais_532}\n')

                melhores_meias_532 = list(melhores_meias.keys())[:3]
                print(f'meias: {melhores_meias_532}\n')

                melhores_atacantes_532 = list(melhores_atacantes.keys())[:2]
                print(f'atacantes: {melhores_atacantes_532}\n')

                print(f'tecnico: {melhor_tecnico}\n')
                break

            if esquema == 541:
                print(f'goleiro: {melhor_goleiro}\n')

                melhores_zagueiros_541 = list(melhores_zagueiros.keys())[:3]
                print(f'zagueiros: {melhores_zagueiros_541}\n')

                melhores_laterais_541 = list(melhores_laterais.keys())[:2]
                print(f'laterais: {melhores_laterais_541}\n')

                melhores_meias_541 = list(melhores_meias.keys())[:4]
                print(f'meias: {melhores_meias_541}\n')

                melhores_atacantes_541 = list(melhores_atacantes.keys())[:1]
                print(f'atacantes: {melhores_atacantes_541}\n')

                print(f'tecnico: {melhor_tecnico}\n')
                break
            
