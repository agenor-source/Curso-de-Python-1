# Pergunte ao usuario 5 numeros e diga se o numero e positivo ou negativo
# Exemplo: 1 positivo, -2 negativo...  

for i in range(5):
    numero = int(input('Digite um numero: '))

    if numero > 0:
        print(f'O numero {numero} que voce digitou é positivo')
    elif numero < 0:
        print(f'O numero {numero} que voce digitou é negativo')
    else:
        print(f'O numero é igual a 0')




