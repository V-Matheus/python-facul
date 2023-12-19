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

diretorio_script = os.path.dirname(os.path.abspath(__file__))

# Caminho do arquivo CSV
caminho_arquivo_csv = os.path.join(diretorio_script, "servidores_campi.csv")

# Abrir o arquivo CSV para escrita
with open(caminho_arquivo_csv, mode='w', newline='', encoding='UTF-8') as arquivo_csv:
    # Criar um objeto de escrita CSV
    escritor_csv = csv.writer(arquivo_csv, delimiter=';')

    # Escrever o cabeçalho
    escritor_csv.writerow(["Sigla do Campus", "Docente", 'tecnico_administrativo', 'estagiario', 'indefinida'])

    # Escrever os dados
    for campus_entry in listInfo:
        escritor_csv.writerow(campus_entry)

print(f"Os dados foram salvos em {caminho_arquivo_csv}.")
