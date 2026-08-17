# Calcule a media das notas e mostre no print.
# nota1 = notas[0] # 5.5
# nota2 = notas[1] # 8
# nota3 = notas[2] # 9.2
# nota4 = notas[3] # 5

# quantidade_total_notas = len(notas)
# media = (nota1 + nota2 + nota3 + nota4) / quantidade_total_notas

# print(f'A média é de {round(media,2)}')

notas = [5.5, 8, 9.2, 5]
soma_notas = 0

for i in notas:
    soma_notas = soma_notas + i

media = soma_notas / len(notas)

if media >= 7:
    print(f'Sua media foi {round(media,2)} - APROVADO')
elif media >= 5 and media <= 6.9:
    print(f'Sua media foi {round(media,2)} - RECUPERACAO')
else:
    print(f'Sua media foi {round(media,2)} - REPROVADO') 