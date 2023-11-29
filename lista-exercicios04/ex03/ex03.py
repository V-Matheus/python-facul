from dolar import cotacoes_dolar

# Percorre toda a lista de dolar e recolhe os dados
valores = []
for dado in cotacoes_dolar:

  # Separa o mes
  data = dado[0]
  mes = data.split('-')[1]
  

  if mes == '01':
    valores.append(dado[1])
    janeiroList = sum(valores)
    janeiro = f'Janeiro: {janeiroList}'
    # print(janeiro)
    valores.clear()

  if mes == '02':
    valores.append(dado[1])
    FevereiroList = sum(valores)
    fevereiro = f'Fevereiro: {valores}'

  if mes == '03':
    valores.append(dado[1])

  if mes == '04':
    valores.append(dado[1])

  if mes == '05':
    valores.append(dado[1])

  if mes == '06':
    valores.append(dado[1])

  if mes == '07':
    valores.append(dado[1])

  if mes == '08':
    valores.append(dado[1])

  if mes == '09':
    valores.append(dado[1])

  if mes == '10':
    valores.append(dado[1])
  
  if mes == '11':
    valores.append(dado[1])

  if mes == '12':
    valores.append(dado[1])
print(janeiro)
print(fevereiro)