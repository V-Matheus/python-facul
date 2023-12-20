import requests
import datetime

while True:
    try:
        ano = int(input(f"Escolha um ano: "))
        if ano > datetime.datetime.now().year:
            print('Digite um ano válido')
            continue

        strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
        strURL += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
        strURL += f'@dataInicial=%2701-01-{ano}%27&@dataFinalCotacao=%2712-31-{ano}%27&$format=json'
        dictCotacoes = requests.get(strURL).json()
        break
    except ValueError:
        print("\nERROR: O valor informado precisa ser inteiro de base 10!")
        continue
    except FileNotFoundError:
        print(f"\nERROR: O arquivo para o ano {ano} não foi encontrado!")
    except Exception as e:
        print(f"\nERROR: {e}")

print(dictCotacoes['value'])
