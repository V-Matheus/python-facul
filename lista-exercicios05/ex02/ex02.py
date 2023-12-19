import os
import csv

strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)
strNomeArq = f'{strDiretorio}/relacao_servidores_ifrn.csv'

with open(strNomeArq, 'r', encoding='UTF-8') as file:
    csv_reader = csv.reader(file)

    # A primeira linha geralmente contém os cabeçalhos
    header = next(csv_reader)
    dictServidores = [list(zip(header, row)) for row in csv_reader]

# Inicialize um dicionário para armazenar os resultados
# Inicialize um dicionário para armazenar os resultados
listInfo = {}

for servidor in dictServidores:
    # Acesse diretamente o índice correto, mas verifique se a lista tem pelo menos 12 elementos
    campus_info = servidor[0][1].split(';')
    sigla_campus = campus_info[11] if len(campus_info) >= 12 and campus_info[11] and not campus_info[11].isdigit() else None

    categoria = servidor[0][1].split(';')[0]

    # Se a sigla_campus já existe no dicionário de resultados e não é 'None' ou um número, atualize a quantidade correspondente à categoria
    if sigla_campus and not sigla_campus.isdigit():
        if sigla_campus in listInfo:
            if categoria in listInfo[sigla_campus]:
                listInfo[sigla_campus][categoria] += 1
            else:
                listInfo[sigla_campus][categoria] = 1
        else:
            # Se a sigla_campus não foi encontrada, adicione uma nova entrada ao dicionário
            listInfo[sigla_campus] = {categoria: 1}

# Exibir o resultado final
for sigla, categorias in listInfo.items():
    print(sigla, categorias)




# print(listInfo)
# print(dictServidores[0])
# print(chave[0])
