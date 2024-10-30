cont = 0
for i in range(5):
    num = int(input('digite um numero'))
    if num < 0:
        cont += 1
print('São negativos',cont,'Numeros')
