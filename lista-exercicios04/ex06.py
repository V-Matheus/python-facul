valor = float(input('Digite um valor para sacar: '))

if valor <= 0:
    print('Digite um valor válido')
else:
    centavos = int(valor * 100)

    moedas = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
    moedas_stg = ['R$ 100,00', 'R$ 50,00', 'R$ 20,00', 'R$ 10,00', 'R$ 5,00', 'R$ 2,00', 'R$ 1,00', 'R$ 0,50', 'R$ 0,25', 'R$ 0,10', 'R$ 0,05', 'R$ 0,01']

# Irá comparar as duas listas
    for moeda, moeda_stg in zip(moedas, moedas_stg):
      # Faz uma divisão inteira para saber a quantidade a partir do valor digitado em centavos e depois retorna o resto
        quantidade = centavos // moeda
        centavos = centavos % moeda

      # Se existir notas ou moedas para aquele valor ele irá mostrar
        if quantidade > 0:
            print(f'Com esse valor você conseguirá sacar {quantidade} {moeda_stg}')
