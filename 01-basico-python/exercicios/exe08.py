# Promoção de cliente
# Uma loja oferece desconto quando o cliente:
# É membro VIP.
# Ou realiza uma compra acima de R$ 500.
# Crie um programa que receba essas informações e utilize o operador lógico 
# OR 
# .

vip = input('Cliente VIP: (S/N)')
valor = float(input('Valor da compra: '))
participa_promocao = (vip == 'S' or vip == 's') or valor > 500

print('-----------------------------')
print(f'Cliente participa da promocao: {participa_promocao}')