print('================================================')
print('Bem-vindo(a) ao conversor de Bits x Byte e Bytes x Bits')
print('opção 1 =  Bits x Byte')
print('opção 2 =  Bytes x Bits')
selection = input("Digite a opção escolhida --> ")


def bits2byte(p):
    bite = 8
    entrada = p
    global result
    result = int(entrada / bite)
    print(f'Você escolheu a opção {selection}, Bits x Bytes')
    print(f'Número Escolhido:  {entrada} Bits !')
    print(f'{entrada} Bits é = {result} Bytes')

def byte2bits(p):
    bite = 8
    entrada = p
    global result
    result = int(entrada * bite)
    print(f'Você escolheu a opção {selection}, Byte x Bits')
    print(f'Número Escolhido:  {entrada} Bytes !')
    print(f'{entrada} Bytes é = {result} Bits')

try:
    selection = int(selection)
    if selection == int(1):
        bits2byte(int(input("Digite um numero inteiro maior que 8 --> ")))
    else:
        byte2bits(int(input("Digite um numero inteiro --> ")))

except:
    print("Você digitou um texto, digite um número")