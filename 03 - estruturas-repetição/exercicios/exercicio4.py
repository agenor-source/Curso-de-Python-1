contador = 0

while contador < 10:
    itens = int(input('digite a quantidade de itens :'))

    if contador + itens > 10:
        print('Quantidade excedeu o limite ')
        break

    if itens < 0 or itens == 0: # if itens <= 0:
        print('Quantidade inválida ')
        continue


    contador = contador + itens
    print(f'A quantidade acumulada foi de {contador}')
   