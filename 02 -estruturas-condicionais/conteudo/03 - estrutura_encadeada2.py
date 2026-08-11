#Permite várias condições
nota = float(input('Digite sua nota: '))

if nota >= 7:
    print('Aprovado')
elif nota > 5:
    print('Recuperação')
else:
    print('Reprovado')



print("============== EXEMPLO ==========")

idade = int(input('Digite sua idade: '))

# menor que 12 - criança
# # menor que 18 adolescente
# menor que 60 adulto
# melhor idade

if idade < 12:
    print('Criança')
elif idade < 18:
    print('Adolescente')
elif idade < 60:
    print('Adulto')
else:
    print('Melhor idade')

print('======== EXEMPLO ====OPERADOR LÓGICO=====')

ususario = input('Possui cadastro? (S/N): ').upper()
senha = input()
