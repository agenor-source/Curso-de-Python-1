# #Exercício — Classificando
# Triângulos
# Um programa deve receber o comprimento dos três lados de um possível
# triângulo.
# Primeiro, verifique se os valores informados podem formar um triângulo.
# Regra:
# A soma de dois lados deve ser maior que o terceiro.
# Depois:
# Se os três lados forem iguais → Triângulo Equilátero
# Se apenas dois lados forem iguais → Triângulo Isósceles
# Se todos os lados forem diferentes → Triângulo Escaleno
# Caso os valores não formem um triângulo, exiba:
# Os valores informados não formam um triângulo.
# Entrada
# Lado 1: 5
# Lado 2: 5
# Lado 3: 5
# Saída esperada
# Triângulo Equilátero
# Exemplo 2
# Entrada
# Exercício — Classificando Triângulos 1
# Lado 1: 7
# Lado 2: 7
# Lado 3: 4
# Saída
# Triângulo Isósceles
# Exemplo 3
# Entrada
# Lado 1: 3
# Lado 2: 4
# Lado 3: 5
# Saída
# Triângulo Escaleno
# Exemplo 4
# Entrada
# Lado 1: 2
# Lado 2: 3
# Lado 3: 6
# Saída
# Os valores informados não formam um triângulo.


# if a + b > c and a + c > b and b + c > a:
#     print(' É um triângulo')
#     if

# else:
#     print('Não forma um triângulo')



lado1 = int(input('lado 1: '))
lado2 = int(input('lado 2: '))
lado3 = int(input('lado 3: '))

if (lado1 + lado2 > lado3) and (lado3 + lado2 > lado1) and (lado1 + lado3 > lado2):
    print('É um triângulo')

    if (lado1 == lado2 == lado3):
        print('Equilátero')
    elif (lado1 == lado2) or (lado1== lado3) or (lado3 == lado2):
        print('Isósceles')
    else:
        print('Escaleno')

else:
    print('Os valores informados não formam um triângulo')
