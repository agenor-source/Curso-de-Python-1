saldo = 1000.00

# defino a função de menu
def mostrar_menu():
    print("===== BANCO PYTHON ===== \n")

    print("1 - consultar saldo")
    print("2 - depositar")
    print("3 - sacar")
    print("4 - sair")

    #defino a função de consulta
    def consultar_saldo(saldo):
        return f'Saldo atual: {saldo}'

#defino a função de de pósito
def depositar(saldo):
    deposito = float(input("Quanto deseja depositar? "))
    print("depósito realizado com sucesso! ")
    return deposito + saldo 

#defino a função de saque
def sacar(saldo):
    saque = float(input(" quanto deseja sacar? "))

    if saque > saldo > saldo:
    print("saldo Insuficiente ")
    return saldo

print("saque realizado com sucesso ")
saldo = saldo - saque
retirn saldo

#while
while True
    mostrar_menu()

    opçao = int(input("digite uma opção acima "))

    if opçao == 1:
        print(consultar_saldo(saldo))
    elif opcao == 2:
        saldo = depositar(saldo)

