a = int(input("Digite o primeiro número inteiro positivo: "))
b = int(input("Digite o segundo número inteiro positivo: "))

if a <= 0 or b <= 0:
    print("Por favor, digite números inteiros positivos.")
else:
  atemp = a
  btemp = b
  mcd = 0
  divisor  = 2
  while divisor <= atemp:
      if atemp % divisor == 0 and btemp % divisor == 0:
          mdc = divisor
      divisor += 1 
        
  print(f"O MDC de {a} e {b} é {mdc}")