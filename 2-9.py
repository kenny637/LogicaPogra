cont = 0
cont2 = 0
cont3 = 0
cont4 = 0
for i in range(5):
    ropa = str(input('Qual e o tamanho da camisa: '))
    if ropa == 'p':
        cont += 1
    elif ropa == 'm':
        cont2 += 1
    elif ropa == 'g':
        cont3 += 1
    elif ropa == 'gg':
        cont4 += 1
print('Roupas P',cont)
print('Roupas M',cont2)
print('Roupas G',cont3)
print('Roupas GG',cont4)