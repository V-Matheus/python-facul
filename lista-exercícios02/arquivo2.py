a = int(input("Digite o primeiro número inteiro positivo: "))
b = int(input("Digite o segundo número inteiro positivo: "))

if a <= 0 or b <= 0:
    print("Por favor, digite números inteiros positivos.")
else:
  atemp = a
  btemp = b
  while btemp != 0:
        temp = btemp
        btemp = atemp % b
        atemp = temp
        mdc = atemp
  print(f"O MDC de {a} e {b} é {mdc}")