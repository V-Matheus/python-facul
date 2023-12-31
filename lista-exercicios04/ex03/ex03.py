from dolar import cotacoes_dolar

# Criar um dicionario que tem a relação entre mês e valor
valores_por_mes = {str(i).zfill(2): [] for i in range(1, 13)}
for dado in cotacoes_dolar:

  # Separa o mes
  data = dado[0]
  mes = data.split('-')[1]
  
  valores_por_mes[mes].append(dado[1])

for mes, valores in valores_por_mes.items():
  maximo = max(valores)
  # Procurar o valor máximo e sua data
  for index, dado in enumerate(cotacoes_dolar):
    if dado[1] == maximo:
        data = dado[0]
        break
  media = round(sum(valores) / len(valores_por_mes[mes]), 4)
  print(f'No {mes}º mês: A maior cotação: {maximo} - Data: {data} Média: - {media} \n')
  
  