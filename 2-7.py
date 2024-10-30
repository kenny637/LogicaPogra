for i in range(5):
    cliente = str(input('O nome do cliente: '))
    endereco = str(input('O endereço do cliente: '))
    valor = int(input('O valor da compra: '))
    if valor > 50000:
        s = (valor * 15)+valor
    if valor <= 50000:
        s = (valor * 10)+valor
    print('valor teve um aulmento de',s)
