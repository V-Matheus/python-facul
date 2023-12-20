import requests, json, os

while True:
    try:
      # Cria o Json a partir do ano
        ano = int(input(f"Escolha um ano: "))
        if ano > 2023:
            print('Digite um ano válido')
            continue

        strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
        strURL += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
        strURL += f'@dataInicial=%2701-01-{ano}%27&@dataFinalCotacao=%2712-31-{ano}%27&$format=json'
        dictCotacoes = requests.get(strURL).json()
        break
    except ValueError:
        print("\nERROR: O valor informado precisa ser inteiro de base 10!")
        continue
    except FileNotFoundError:
        print(f"\nERROR: O arquivo para o ano {ano} não foi encontrado!")
    except Exception as e:
        print(f"\nERROR: {e}")

dicDados = {}
medias_por_mes = {}

# Iterar sobre os valores no dicionário de cotações
for cotacao in dictCotacoes['value']:
    # Extrair o mês da data e o valor da compra e venda
    data_cotacao = cotacao['dataHoraCotacao'].split(' ')[0]
    mes = data_cotacao.split('-')[1]
    compra = cotacao['cotacaoCompra']
    venda = cotacao['cotacaoVenda']

    # Adicionar o valor da compra e venda ao mês correspondente no dicionário de médias
    if mes not in medias_por_mes:
        medias_por_mes[mes] = {'soma_compra': compra, 'soma_venda': venda, 'contador': 1}
    else:
        medias_por_mes[mes]['soma_compra'] += compra
        medias_por_mes[mes]['soma_venda'] += venda
        medias_por_mes[mes]['contador'] += 1

# Calcular as médias de compra e venda para cada mês
for mes, valores in medias_por_mes.items():
    media_compra = round(valores['soma_compra'] / valores['contador'], 5)
    media_venda = round(valores['soma_venda'] / valores['contador'], 5)
    dicDados[mes] = {'media_compra': media_compra, 'media_venda': media_venda}

# Criar um dicionário de tradução de número do mês para nome do mês
traducao_meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

# Substituir números de meses pelos nomes
for mes in list(dicDados.keys()):
    mes_numero = int(mes)
    mes_nome = traducao_meses[mes_numero]
    dicDados[mes_nome] = dicDados.pop(mes)

# Montar o caminho completo para o arquivo JSON
diretorio = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio, f"medias_cotacoes_{ano}.json")

# Salvar o dicionário em um arquivo JSON
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo_json:
    json.dump(dicDados, arquivo_json, ensure_ascii=False, indent=2)


# Criar arquivo CSV
caminho_arquivo_csv = os.path.join(diretorio, f"medias_cotacoes_{ano}.csv")

with open(caminho_arquivo_csv, mode='w', encoding='UTF-8') as arquivo_csv:
    # Escrever o cabeçalho
    arquivo_csv.write("mes - media_compra - media_venda\n")

    # Escrever os dados
    for mes, medias in dicDados.items():
        media_compra = f"{medias['media_compra']:.5f}"
        media_venda = f"{medias['media_venda']:.5f}"
        arquivo_csv.write(f"{mes} - {media_compra} - {media_venda}\n")

print(f"O arquivo Json e o CSV foram salvos no arquivo em: {diretorio}.")