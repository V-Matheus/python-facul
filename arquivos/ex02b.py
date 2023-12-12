import os, requests, sys

# Obtendo o diretório corrente
strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)

# --------------------------------------------------
# Requisitando os dados no servidor
# strURL = 'https://dados.ifrn.edu.br/dataset/7b48f9d0-205d-46b1-8225-a3cc7d3973ff/resource/fe0e9d2c-1c02-4625-b692-13edcc3380ae/download/dados_extraidos_recursos_cursos-ofertados.json'

strURL = 'https://viacep.com.br/ws/RN/natal/salgado/xml'

retRequisicao = requests.get(strURL)
print(retRequisicao.status_code)
if retRequisicao.status_code != 200:
    print(f'ERRO: Erro ao obter os dados...\nCÓDIGO ERRO = {retRequisicao.status_code}')
    sys.exit()

# lstCursos = retRequisicao.json()
# print(lstCursos)

try:
 lstCursos = retRequisicao.json()
except:
  print(f'Error: {sys.exc_info()}')
else:
  print(lstCursos)
