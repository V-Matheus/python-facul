print('Digite os valores para mover o robó | U (cima); D (baixo); R (direita); L (esquerda); O (noroeste/cima-esquerda); N (nordeste/cima-direita); E (sudeste/baixo-direita) e W (sudoeste/baixo-esquerda)')
inicialX = int(input('Indique a coordenada inicial no Eixo X: '))
inicialY = int(input('Indique a coordenada inicial no Eixo Y: '))

finalX = int(inicialX)
finalY = int(inicialY)

movimentoUser = input('Digite os movimentos que o robó deverá fazer: ').upper()
movimentosValidos = ''

if inicialX > 0 and inicialY > 0:
  quadranteInicial = 1
elif inicialX < 0 and inicialY > 0:
  quadranteInicial = 2
elif inicialX < 0 and inicialY < 0:
  quadranteInicial = 3
elif inicialX > 0 and inicialY < 0:
  quadranteInicial = 4
else:
  quadranteInicial = 0

quadranteFinal = quadranteInicial

for letra in movimentoUser:
  if letra in 'UDRLONEW':
    if letra == 'U':
      finalY += 1

    elif letra == 'D':
      finalY -= 1

    elif letra == 'R':
      finalX += 1

    elif letra == 'L':
      finalX -= 1

    elif letra == 'O':
      finalY += 1
      finalX -= 1

    elif letra == 'N':
      finalY += 1
      finalX += 1

    elif letra == 'E':
      finalY -= 1
      finalX += 1

    elif letra == 'W':
      finalY -= 1
      finalX -= 1

    movimentosValidos += letra
  else:
    print(f'Digite um valor de movimento dentro das regras: UDRLONEW')
movimentosQ = len(movimentosValidos)

if finalX > 0 and finalY > 0:
      quadranteFinal = 1

if finalX > 0 and finalY > 0:
      quadranteFinal = 1
elif finalX < 0 and finalY > 0:
      quadranteFinal = 2
elif finalX < 0 and finalY < 0:
      quadranteFinal = 3
elif finalX > 0 and finalY < 0:
      quadranteFinal = 4
else:
      quadranteFinal = 0

print(f'A posição inicial do robô é: ({inicialX}, {inicialY})')
print(f'A posição final do robô é: ({finalX}, {finalY})')
print(f'Ele executou {movimentosQ} movimentos')
print(f'Ele se moveu: {movimentosValidos}')
if quadranteInicial == 0:
  print('Um dos eixos está no ponto 0, então não está em nenhum quadrante inicialmente')
else:
  print(f'Ele começa no {quadranteInicial}º quadrante')
if quadranteFinal == 0:
  print('Um dos eixos está no ponto 0, então não está em nenhum quadrante depois de movido')
else:
  print(f'Ele termina no {quadranteFinal}º quadrante')
