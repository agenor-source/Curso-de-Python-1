lado1 = int(input('Lado 1: '))
lado2= int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))

if (lado1 + lado2 > lado3) and (lado3 + lado2 > lado1) and (lado1 + lado3 > lado2):
    print('E um triangulo \n')

    if (lado1 == lado2 == lado3):
        print('Equilatero')
    elif (lado1 != lado2 != lado3):
        print('Escaleno')
    else:
        print('Isosceles')

else:
    print('Os valores informados não formam um triângulo.')