massaInicial = float(input('Digite a massa inicial em gramas: '))
massaFinal = massaInicial
segundosPorLoop = 0
hours = 0
minuts = 0
seg = 0

while massaFinal > 0.5:
    metade = massaFinal / 2
    massaFinal = metade
    segundosPorLoop += 50
    if massaFinal < 0.5:
        break

horas = segundosPorLoop // 3600
minutos = (segundosPorLoop % 3600) // 60
segundos = segundosPorLoop % 60

print(f'Massa Inicial: {massaInicial} gramas')
print(f'Massa Final: {metade} gramas')
print(f"Tempo de Decaimento: {horas:02d}:{minutos:02d}:{segundos:02d}")