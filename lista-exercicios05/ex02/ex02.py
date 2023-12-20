import os
import csv

strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)
strNomeArq = f'{strDiretorio}/relacao_servidores_ifrn.csv'

with open(strNomeArq, 'r', encoding='UTF-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    dictServidores = [list(zip(header, row)) for row in csv_reader]

listInfo = []
listDoc = []

for servidor in dictServidores:
    # Organiza dados e separa por ;
    servidor_info = servidor[0][1].split(';')

    # Ignora os dados 'None'
    sigla_campus = servidor_info[11] if len(servidor_info) >= 12 and servidor_info[11] and not servidor_info[11].isdigit() else None
    categoria = servidor[0][1].split(';')[0]

    # Se encontrar o campus adiciona + 1 para o tipo de servidor
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
            
        # se não achar o campus adiciona a lista
        if not campus_encontrado:
            listInfo.append([sigla_campus, {'docente': 0, 'tecnico_administrativo': 0, 'estagiario': 0, 'indefinida': 0}])
            for campus_entry in listInfo:
                if campus_entry[0] == sigla_campus:
                    campus_entry[1][categoria] += 1
                    break


# Adiciona as disciplinas de ingresso na lista listDoc
for servidor_info in dictServidores:
    # Certifica-se de que há pelo menos 2 elementos e que o segundo não é vazio
    if len(servidor_info[0][1].split(';')) >= 2 and servidor_info[0][1].split(';')[1]:
        disciplina_ingresso = servidor_info[0][1].split(';')[1]
        encontrado = False
        for item in listDoc:
            if item[0] == disciplina_ingresso:
                item[1] += 1
                encontrado = True
                break
        if not encontrado:
            listDoc.append([disciplina_ingresso, 1])

# Ordenar a lista de docentes alfabeticamente pela disciplina de ingresso
listDoc.sort(key=lambda x: x[0])

# Criar arquivo dos servidores
diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo_csv = os.path.join(diretorio_script, "servidores_campi.csv")

with open(caminho_arquivo_csv, mode='w', newline='', encoding='UTF-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';')
    
    escritor_csv.writerow(["Sigla do Campus", "Docente", 'tecnico_administrativo', 'estagiario', 'indefinida'])
    
    for campus_entry in listInfo:
        escritor_csv.writerow([campus_entry[0], campus_entry[1]['docente'], campus_entry[1]['tecnico_administrativo'], campus_entry[1]['estagiario'], campus_entry[1]['indefinida']])

print(f"Os dados dos servidores foram salvos na pasta raiz.")

# criando o arquivo dos Docentes
caminho_arquivo_csv = os.path.join(diretorio_script, "docentes_disciplinas.csv")
with open(caminho_arquivo_csv, mode='w', newline='', encoding='UTF-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';')
    
    escritor_csv.writerow(['Disciplina', 'quantidade de docentes da disciplina'])
    
    for docente_entry in listDoc:
        escritor_csv.writerow([docente_entry[0], docente_entry[1]])

# Caminho do arquivo CSV para servidores
caminho_arquivo_csv_servidores = os.path.join(strDiretorio, "servidores_campi.csv")

# Escreve o arquivo CSV para servidores
with open(caminho_arquivo_csv_servidores, 'w', newline='', encoding='UTF-8') as arquivo_csv:
    # Escreve cabeçalho
    arquivo_csv.write(" - ".join(["Sigla do Campus", "Docente", 'tecnico_administrativo', 'estagiario', 'indefinida']) + '\n')

    # Escreve dados
    for campus_entry in listInfo:
        arquivo_csv.write(" - ".join([campus_entry[0], str(campus_entry[1]['docente']), str(campus_entry[1]['tecnico_administrativo']), str(campus_entry[1]['estagiario']), str(campus_entry[1]['indefinida'])]) + '\n')

print(f"Os dados dos servidores foram salvos em {caminho_arquivo_csv_servidores}.")

# Caminho do arquivo CSV para docentes
caminho_arquivo_csv_docentes = os.path.join(strDiretorio, "docentes_disciplinas.csv")

# Escreve o arquivo CSV para docentes
with open(caminho_arquivo_csv_docentes, 'w', newline='', encoding='UTF-8') as arquivo_csv:
    # Escreve cabeçalho
    arquivo_csv.write(" - ".join(['Disciplina', 'Quantidade de docentes da disciplina']) + '\n')

    # Escreve dados
    for docente_entry in listDoc:
        arquivo_csv.write(" - ".join([docente_entry[0], str(docente_entry[1])]) + '\n')

print(f"Os dados dos docentes foram salvos em {caminho_arquivo_csv_docentes}.")