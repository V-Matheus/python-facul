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
# Inicialize uma lista para armazenar os resultados
listInfo = [["Sigla do Campus", "Tipo de servidores"]]

for servidor in dictServidores:
    # Acesse diretamente o índice correto, mas verifique se a lista tem pelo menos 12 elementos
    servidor_info = servidor[0][1].split(';')
    sigla_campus = servidor_info[11] if len(servidor_info) >= 12 and servidor_info[11] and not servidor_info[11].isdigit() else None
    categoria = servidor[0][1].split(';')[0]

    # Se a sigla_campus já existe na lista de resultados e não é 'None' ou um número, atualize a quantidade correspondente à categoria
    if sigla_campus and not sigla_campus.isdigit():
        campus_encontrado = False
        for campus_entry in listInfo:
            if campus_entry[0] == sigla_campus:
                if categoria in campus_entry[1]:
                    campus_entry[1][categoria] += 1
                else:
                    campus_entry[1][categoria] = 1
                campus_encontrado = True
                break

        if not campus_encontrado:
            # Se a sigla_campus não foi encontrada, adicione uma nova entrada à lista
            listInfo.append([sigla_campus, {categoria: 1}])

# Exibir o resultado final
for campus_entry in listInfo:
    print(campus_entry)

