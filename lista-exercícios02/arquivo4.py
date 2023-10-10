senha_padrao = 'swordfish'
tentativa = input('Digite a senha: ')
contagem = 1
while tentativa != senha_padrao:
  tentativa = input('Digite a senha: ')
  contagem += 1
print(f'Parabéns, você acertou a senha. Número de tentativas: {contagem}')