salario = float(input('Digite o valor do salário: '))
emprestimo = float(input('Digite o valor do emprestimo: '))
if salario > 0 and emprestimo > 0:
    if  salario * 0.20 > emprestimo:
        print('Empréstimo concedido')
    else:
        print('Empréstimo não concedido')
else:
    print('Digite um valor válido')