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

for servidor in dictServidores:
    servidor_info = servidor[0][1].split(';')
    sigla_campus = servidor_info[11] if len(servidor_info) >= 12 and servidor_info[11] and not servidor_info[11].isdigit() else None
    categoria = servidor[0][1].split(';')[0]

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
            listInfo.append([sigla_campus, {'docente': 0, 'tecnico_administrativo': 0, 'estagiario': 0, 'indefinida': 0}])
            for campus_entry in listInfo:
                if campus_entry[0] == sigla_campus:
                    campus_entry[1][categoria] += 1
                    break

diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo_csv = os.path.join(diretorio_script, "servidores_campi.csv")

with open(caminho_arquivo_csv, mode='w', newline='', encoding='UTF-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';')
    
    escritor_csv.writerow(["Sigla do Campus", "Docente", 'tecnico_administrativo', 'estagiario', 'indefinida'])
    
    for campus_entry in listInfo:
        escritor_csv.writerow([campus_entry[0], campus_entry[1]['docente'], campus_entry[1]['tecnico_administrativo'], campus_entry[1]['estagiario'], campus_entry[1]['indefinida']])

print(f"Os dados foram salvos em {caminho_arquivo_csv}.")
