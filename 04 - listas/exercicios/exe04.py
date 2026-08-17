# # peca ao usuario para cadastrar numeros em uma lista 
# # conte quantos impares e pares tem nessa lista 
# lista = []
# impares = 0
# pares = 0

for i in range(6):
    numero = int(input('Digite um numero: '))
    lista.append(numero)

    if i % 2 == 0:
        pares = pares + 1
    else: 
        impares += 1

# print(f'Na lista eu tenho {impares} impares')
# print(f'Na lista eu tenho {pares} pares')
