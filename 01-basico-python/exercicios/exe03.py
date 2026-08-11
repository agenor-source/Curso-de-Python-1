# Calculadora de compra
# Uma pessoa foi ao mercado e comprou dois tipos de produtos.
# Crie um programa que calcule o valor total da compra e a quantidade total de produtos

quantidade_produto1 = int(input('Quantidade do primeiro produto: '))
valor_produto1 = float(input('Valor do primeiro produto: '))

quantidade_produto2 = int(input('Quantidade do segundo produto: '))
valor_produto2 = float(input('Valor do segundo produto: '))

quantidade_produto = quantidade_produto1 + quantidade_produto2
valor_total_compra = (quantidade_produto1 * valor_produto1) + (quantidade_produto2 * valor_produto2)

print('--- Resumo da Compra ---')
print(f'Quantidade total de produtos: {quantidade_produto}')
print(f'Valor total da compra: R$ {valor_total_compra}')
print('Ola mundo')