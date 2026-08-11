# Comparação de preços
# Uma loja deseja comparar o preço de dois produtos.
# Crie um programa que receba dois valores e faça comparações

preco_produto1 = float(input('Digite o preço do primeiro produto: '))
preco_produto2 = float(input('Digite o preco do segundo produto: '))

produto1_menor_produto2 = preco_produto1 < preco_produto2
produto2_maior_produto1 = preco_produto2 > preco_produto1
mesmo_preco = preco_produto1 == preco_produto2

print('---------------------------------------')

print(f'O primeiro produto é menor que o segundo: {produto1_menor_produto2}')
print(f'O segundo produto é maior que o primeiro: {produto2_maior_produto1}')
print(f'Os produtos possuem o mesmo preço: {mesmo_preco}')