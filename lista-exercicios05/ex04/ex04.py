import os

# Obtendo o caminho da pasta do script
caminho_script = os.path.dirname(os.path.abspath(__file__))

# Caminho completo para o diretório dados_estatisticos
caminho_dados_estatisticos = os.path.join(caminho_script, 'dados_estatisticos')

# Verificando se o diretório já existe ou não
if not os.path.exists(caminho_dados_estatisticos):
    # Criando o diretório se não existir
    os.makedirs(caminho_dados_estatisticos)
    print(f"Diretório 'dados_estatisticos' criado em: {caminho_dados_estatisticos}")
else:
    print(f"Diretório 'dados_estatisticos' já existe em: {caminho_dados_estatisticos}")

# Caminho da pasta contendo os arquivos CSV
pasta_csv = os.path.join(caminho_script, 'serie_historica_anp')

# Lista para armazenar as informações
informacoes = []

print('Carregando dados....')
# Iterar sobre os arquivos na pasta
for arquivo in os.listdir(pasta_csv):
        caminho_arquivo = os.path.join(pasta_csv, arquivo)

        # Abrir o arquivo CSV e ler linha por linha
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            linhas = file.readlines()

            # Ignorar caracteres iniciais '\ufeff'
            linhas[0] = linhas[0].lstrip('\ufeff')

            # Ignorar o cabeçalho
            cabecalho = linhas[0].strip().split(';')
            # Encontrar os índices das colunas desejadas
            indices = [cabecalho.index(coluna) for coluna in ['Regiao - Sigla', 'Estado - Sigla', 'Produto', 'Data da Coleta', 'Valor de Venda', 'Bandeira']]
            
            # Iterar sobre as linhas do arquivo
            for linha in linhas[1:]:
                dados = linha.strip().split(';')
                # Extrair as informações desejadas
                informacao = {
                    'Regiao – Sigla': dados[indices[0]],
                    'Estado – Sigla': dados[indices[1]],
                    'Produto': dados[indices[2]],
                    'Data da Coleta': dados[indices[3]],
                    'Valor de Venda': dados[indices[4]],
                    'Bandeira': dados[indices[5]]
                }
                informacoes.append(informacao)

# Caminho completo para o arquivo CSV
caminho_arquivo_csv = os.path.join(caminho_dados_estatisticos, 'serie_historica_anp.csv')

# Escrevendo no arquivo CSV
with open(caminho_arquivo_csv, 'w', encoding='utf-8') as csvfile:
    # Escrevendo o cabeçalho
    csvfile.write(';'.join(informacoes[0].keys()) + '\n')

    # Escrevendo as informações
    for info in informacoes:
        csvfile.write(';'.join(map(str, info.values())) + '\n')

# Calculando média de valor de venda por bandeira e produto
media_bandeira = {}
# Calculando média de valor de venda por produto, região e ano
media_produto_regiao = {}

# Processando as informações
for info in informacoes:
    bandeira = info['Bandeira']
    produto = info['Produto']
    regiao = info['Regiao – Sigla']
    ano = info['Data da Coleta'][-4:]  # Obtendo o ano dos dados
    valor_venda = float(info['Valor de Venda'].replace(',', '.'))

    # Calculando média por bandeira e produto
    chave_bandeira_produto = f"{bandeira} - {produto} - {ano}"
    if chave_bandeira_produto not in media_bandeira:
        media_bandeira[chave_bandeira_produto] = {'soma': 0, 'quantidade': 0}
    media_bandeira[chave_bandeira_produto]['soma'] += valor_venda
    media_bandeira[chave_bandeira_produto]['quantidade'] += 1

    # Calculando média por produto, região e ano
    chave_produto_regiao = f"{produto} - {regiao} - {ano}"
    if chave_produto_regiao not in media_produto_regiao:
        media_produto_regiao[chave_produto_regiao] = {'soma': 0, 'quantidade': 0}
    media_produto_regiao[chave_produto_regiao]['soma'] += valor_venda
    media_produto_regiao[chave_produto_regiao]['quantidade'] += 1

# Salvando média por bandeira e produto
caminho_arquivo_media_bandeira = os.path.join(caminho_dados_estatisticos, 'media_bandeira.txt')
with open(caminho_arquivo_media_bandeira, 'w', encoding='utf-8') as arquivo:
    arquivo.write("bandeira;produto;ano;valor_medio_venda;quantidade_postos\n")
    for chave, dados in media_bandeira.items():
        bandeira, produto, ano = chave.split(' - ')
        valor_medio_venda = dados['soma'] / dados['quantidade']
        quantidade_postos = dados['quantidade']
        arquivo.write(f"{bandeira};{produto};{ano};{valor_medio_venda:.2f};{quantidade_postos}\n")

# Salvando média por produto, região e ano
caminho_arquivo_media_produto_regiao = os.path.join(caminho_dados_estatisticos, 'media_produto_regiao.txt')
with open(caminho_arquivo_media_produto_regiao, 'w', encoding='utf-8') as arquivo:
    arquivo.write("produto;regiao;ano;valor_medio;quantidade_postos\n")
    for chave, dados in media_produto_regiao.items():
        produto, regiao, ano = chave.split(' - ')
        valor_medio = dados['soma'] / dados['quantidade']
        quantidade_postos = dados['quantidade']
        arquivo.write(f"{produto};{regiao};{ano};{valor_medio:.2f};{quantidade_postos}\n")

print(f'Seus dados foram salvos no caminho: {caminho_dados_estatisticos}')
