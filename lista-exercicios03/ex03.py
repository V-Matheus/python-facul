dna = input('Digite o DNA: ')
rna = ''

for i in range(len(dna)):
    position = dna[i].lower()

    if position == 'a' or position =='g' or position == 't' or position == 'c':
        if position == 'a':
            position = 'U'
            rna += position

        elif position == 't':
            position = 'C'
            rna += position

        elif position == 'c':
            position = 'A'
            rna += position
        else:
            position = 'G'
            rna += position
    else:
        print('Digite um valor válido')
        break
if rna:
    print(f'A sequeéncia de RNA equivalente a {dna} é {rna}')