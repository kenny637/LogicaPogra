
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end='')
cont = 3
while True:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
    if t3 >= 500:
        break
print('→ fim')
