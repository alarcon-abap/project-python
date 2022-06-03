valorEntr_String = input("Digite um número inteiro Decimal: ")
valorEntrada = int(valorEntr_String)
guardaValor = int(valorEntrada)
resultado = ""

while valorEntrada > 0:
  if (valorEntrada % 2) == 0:
    resultado = "0" + resultado
  else:
    resultado = "1" + resultado
  
  valorEntrada = valorEntrada // 2

print(f'Você Digitou o número inteiro: {guardaValor} \nO Equivalente em Binário é: {resultado}')