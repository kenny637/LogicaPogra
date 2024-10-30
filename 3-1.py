num = 1
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
while num > 0:
    num = int(input('Digite um numero'))
    if num > 0:
        if num >= 0 and num <= 25:
            cont1 += 1
        if num >= 26 and num <= 50:
            cont2 += 1
        if num >= 51 and num <= 75:
            cont3 += 1
        if num >= 76 and num <= 100:
            cont4 += 1
print('Numeros entre [0-25]',cont1)
print('Numeros entre [26-50]',cont2)
print('Numeros entre [51-75]',cont3)
print('Numeros entre [76-100]',cont4)

