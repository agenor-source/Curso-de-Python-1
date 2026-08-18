# carrinho_compras = [150, 260, 100, 50, 60]
# lista = [1, 2, 3, 4, 5]
# somaLista = 0
# somaCarrinhoCompra = 0

# for item in carrinho_compras:
#     somaCarrinhoCompra = somaCarrinhoCompra + item

# for item in lista:
#     somaLista = somaLista + item

# print(somaLista)
# print(somaCarrinhoCompra)


carrinho_compras = [150, 260, 100, 50, 60]
def soma_lista(lista):
    soma = 0
    for i in lista:
        soma += i

    return soma

soma_carrinho = soma_lista(carrinho_compras)
print(f'A soma do carrinho de compras foi de: {soma_carrinho}')