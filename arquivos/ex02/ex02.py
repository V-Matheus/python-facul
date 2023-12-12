import os

strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)

print(strDiretorio)
strNomeArq = strDiretorio + '//suap_componentes_curriculares.csv'
arqLeitura = open(strNomeArq, 'r', encoding='utf-8')

strHeader = arqLeitura.readline()[:-1]
lstComponentes = list()
while True:
    strLinha = arqLeitura.readline()[:-1]
    if not strLinha: break
    strLinha = strLinha.split(';')
    lstComponentes.append(strLinha)
print(lstComponentes[:5])

arqLeitura.close()


