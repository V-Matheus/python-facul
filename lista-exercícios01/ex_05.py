jogador1 = str(input('Jogador 1: Escolha entre "Pedra", "Papel" ou "Tesoura": ')).lower()
jogador2 = str(input('Jogador 2: Escolha entre "Pedra", "Papel" ou "Tesoura": ')).lower()

if(jogador1 == 'pedra' or jogador1 == 'papel' or jogador1 == 'tesoura' ) :
  if jogador1 == jogador2:
    print('Empate')
  elif jogador1 == 'pedra' and jogador2 =='papel':
    print('Jogador 2 ganhou')
  elif jogador1 == 'pedra' and jogador2 =='tesoura':
    print('Jogador 1 ganhou')
  elif jogador1 == 'papel' and jogador2 == 'pedra':
    print('Jogador 1 ganhou')
  elif jogador1 == 'papel' and jogador2 == 'tesoura':
    print('Jogador 2 ganhou')
  elif jogador1 == 'tesoura' and jogador2 == 'pedra':
    print('Jogador 2 ganhou')
  elif jogador1 == 'tesoura' and jogador2 == 'papel':
    print('Jogador 1 ganhou')
else: 
  print('Coloque um valor válido')