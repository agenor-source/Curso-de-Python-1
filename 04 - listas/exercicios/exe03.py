quadrados = []
soma_quadrados = 0

for i in range(5):
    numero = int(input('Digite um numero: '))
    quadrado = numero ** 2
    quadrados.append(quadrado)

for i in quadrados:
    print(i)
    soma_quadrados = soma_quadrados + i

print(f'A soma dos quadrados é: {soma_quadrados}')

