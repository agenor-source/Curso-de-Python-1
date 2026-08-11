#  Cadastro de produto
# Uma loja precisa cadastrar produtos no sistema.
# Crie um programa que solicite as informações de um produto

nome_produto = input('Digite o nome do produto: ')
preco_produto = float(input('Digite o preco: '))
quantidade_disponivel_produto = int(input('Digite a quantidade disponível: '))
categoria_produto = input('Digite a categoria: ')
promocao_produto = input('O produto esta em promoção? (S/N)')
esta_em_promocao = promocao_produto == 'S' or promocao_produto == 's'

print('--- Produto Cadastrado ---')

print(f'Produto: {nome_produto}')
print(f'Preço: R$ {preco_produto}')
print(f'Quantidade: {quantidade_disponivel_produto} unidades')
print(f'Categoria: {categoria_produto}')
print(f'Promoção: {esta_em_promocao}')