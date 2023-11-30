from dolar import cotacoes_dolar

# Percorre toda a lista de dolar e recolhe os dados
valores_por_mes = {str(i).zfill(2): [] for i in range(1, 13)}
for dado in cotacoes_dolar:

  # Separa o mes
  data = dado[0]
  mes = data.split('-')[1]

for mes, valores in valores_por_mes.items():
  media = round(sum(valores) / len(valores_por_mes[mes]), 4)
  print(f'No {mes}º mês: Média: {media}')
  