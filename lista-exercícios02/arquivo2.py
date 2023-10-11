num1 = int(input("Digite o primeiro número inteiro positivo: "))
num2 = int(input("Digite o segundo número inteiro positivo: "))
temp1 = num1
temp2 = num2

if temp1 <= 0 or temp2 <= 0:
    print("Por favor, digite números inteiros positivos.")
else:
    while temp2:
        temp = temp2
        temp2 = temp1 % temp2
        temp1 = temp
    mdc = temp1
    print(f"O MDC de {num1} e {num2} é {mdc}")