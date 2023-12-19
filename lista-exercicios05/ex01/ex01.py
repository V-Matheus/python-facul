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

# Puxando informaçoes das posições
posicoes_get = dictCartola.get('posicoes')
posicoes = {}
for id_posicao, posicao in posicoes_get.items():
    posicoes_list = posicao['nome']
    posicoes[id_posicao] = posicoes_list

# Puxando informações dos atletas
atletas = dictCartola.get('atletas')
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
    maiores_pontuacoes[nome] = {'pontuacao': maior_pontuacao, 'posicao': posicoes[str(posicao_id)], 'apelido' : apelido, 'clube': clube}

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
    if posicao == 'Goleiro':
        melhores_goleiros[jogador] = info
    elif posicao == 'Lateral':
        melhores_laterais[jogador] = info
    elif posicao == 'Zagueiro':
        melhores_zagueiros[jogador] = info
    elif posicao == 'Meia':
        melhores_meias[jogador] = info
    elif posicao == 'Atacante':
        melhores_atacantes[jogador] = info
    elif posicao == 'Técnico':
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
      # Analisa os esquemas táticos
      print(f'Os melhores jogadores para esse esquema tático são:\n')
      if esquema == 343:
        z= 3
        l = 0
        m = 4
        a = 3

      elif esquema == 352:
        z = 3
        l = 0
        m = 5
        a = 2

      elif esquema == 433:
        z = 2
        l = 2
        m = 3
        a = 3

      elif esquema == 442:
        z = 2
        l = 2
        m = 4
        a = 2

      elif esquema == 451:
        z = 2
        l = 2
        m = 5
        a = 1

      elif esquema == 532:
        z = 3
        l = 2
        m = 4
        a = 1

      elif esquema == 541:
        z = 3
        l = 2
        m = 4
        a = 1

          
      print(f'Goleiro: {melhor_goleiro["nome"]} - apelido: {melhor_goleiro["info"]["apelido"]} - pontuação: {melhor_goleiro["info"]["pontuacao"]} - clube: {melhor_goleiro["info"]["clube"]}\n')

          # Pega as informações + nome dos jogadores a partir de uma lista de valores e chaves dentro do dicionário
      for info_zagueiros, name_zagueiros in zip(list(melhores_zagueiros.values())[:z], list(melhores_zagueiros.keys())[:z]):
          zagueiros_pontuacao = info_zagueiros['pontuacao']
          zagueiros_apelido = info_zagueiros['apelido']
          zagueiros_clube = info_zagueiros['clube']
          print(f'Zagueiro: {name_zagueiros} - apelido: {zagueiros_apelido} - pontuacao: {zagueiros_pontuacao}  - clube: {zagueiros_clube}\n')

      for info_laterais, name_laterais in zip(list(melhores_laterais.values())[:l], list(melhores_laterais.keys())[:l]):
          laterais_pontuacao = info_laterais['pontuacao']
          laterais_apelido = info_laterais['apelido']
          laterais_clube = info_laterais['clube']
          print(f'Lateral: {name_laterais} - apelido: {laterais_apelido} - pontuacao: {laterais_pontuacao}  - clube: {laterais_clube}\n')

      for info_meias, name_meias in zip(list(melhores_meias.values())[:m], list(melhores_meias.keys())[:m]):
          meias_pontuacao = info_meias['pontuacao']
          meias_apelido = info_meias['apelido']
          meias_clube = info_meias['clube']
          print(f'Meia: {name_meias} - apelido: {meias_apelido} - pontuacao: {meias_pontuacao}  - clube: {meias_clube}\n')

      for info_atacantes, name_atacantes in zip(list(melhores_atacantes.values())[:a], list(melhores_atacantes.keys())[:a]):
          atacantes_pontuacao = info_atacantes['pontuacao']
          atacantes_apelido = info_atacantes['apelido']
          atacantes_clube = info_atacantes['clube']
          print(f'Atacante: {name_atacantes} - apelido: {atacantes_apelido} - pontuacao: {atacantes_pontuacao}  - clube: {atacantes_clube}\n')

      print(f'Técnico: {melhor_tecnico["nome"]} - apelido: {melhor_tecnico["info"]["apelido"]} - pontuação: {melhor_tecnico["info"]["pontuacao"]} - clube: {melhor_tecnico["info"]["clube"]}\n')
      break
