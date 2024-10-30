cont = 2
cont2 = 1
for i in range(5):
    num = int(input('digite um numero'))
    if  num <= 20 or num >= 10:
        cont = cont + 1
    elif num < 10 or num > 20:
        cont2 += 1
print(cont)
print(cont2)
