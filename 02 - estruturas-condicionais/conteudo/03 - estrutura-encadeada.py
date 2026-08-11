# # Permite varias condicoes 
# nota = float(input('Digite sua nota: '))

# if nota >= 7:
#     print('Aprovado')
# elif nota >= 5:
#     print('Recuperacao')
# else:
#     print('Reprovado')

# print('========= EXEMPLO =========')

# # menor que 12 - crianca 
# # menor que 18 adolescente 
# # menor que 60 adulto 
# # melhor idade 
# idade = int( input('Digite sua idade: '))

# if idade < 12:
#     print('Criança')
# elif idade < 18:
#     print('Adolescente')
# elif idade < 60:
#     print('Adulto')
# else:
#     print('Melhor idade')

print('========= EXEMPLO - operador logico =========')

usuario = input('Possui cadastro? (S/N): ').upper()
senha = input('Senha correta? (S/N): ').upper()

if usuario == 'S' and senha == 'S':
    print('Acesso liberado')
else: 
    print('Acesso negado')