cpf = input('Digite o valor do CPF: ')
cpf = cpf.replace('.', '').replace('-', '')

if len(cpf) == 11:
  soma = 0
  i = 0

  # Faz um loop até o 9º algarimo do cpf somando e multiplicando // Ex: 123.4566.789.01 => 1 * 10 + 2 * 9 + 3 * 8
  while i < 9:
    soma += int(cpf[i]) * (10 - i)
    i += 1

    # Irá pegar a soma total e dividir por 11 e depois subtrair 11 pelo resto da divisão, assim verificando 
    # se bate com o 9º número do cpf
  resto = 11 - (soma % 11)
  if resto == 11 or resto == 10:
      resto = 0
  if resto != int(cpf[9]):
     print('cpf inválido')
  else:
    soma = 0
    i = 0

  # Faz um loop até o 10º algarimo do cpf somando e multiplicando // Ex: 123.4566.789.01 => 1 * 10 + 2 * 9 + 3 * 8
    while i < 10:
      soma += int(cpf[i]) * (11 - i)
      i += 1

    # Irá pegar a soma total e dividir por 11 e depois subtrair 11 pelo resto da divisão, assim verificando 
    # se bate com o 10º número do cpf
      resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
      resto = 0
    if resto != int(cpf[10]):
      print('CPF inválido')
  print('CPF válido')
else:
  print('Cpf inálido')
