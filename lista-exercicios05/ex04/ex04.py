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

# Exibir a lista final de informações
for info in informacoes:
    print(info)
