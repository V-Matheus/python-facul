coordenadas1X = int(input('Digite as coordenadas x do primeiro ponto: '))
coordenadas1Y = int(input('Digite as coordenadas y do primeiro ponto: '))
coordenadas2X = int(input('Digite as coordenadas x do segundo ponto: '))
coordenadas2Y = int(input('Digite as coordenadas y do segundo ponto: '))

distancia = ((coordenadas2X - coordenadas1X)**2 + (coordenadas2Y - coordenadas1Y)**2)**0.5
print(f'A distancia entre o ponto ({coordenadas1X},{coordenadas1Y}) e ({coordenadas2X,coordenadas2Y}) é {distancia:.2f})')

