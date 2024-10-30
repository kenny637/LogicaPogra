primo = int(input('Digite um numero: '))
if primo > 1:
    for i in range(2, primo):
        if primo % i == 0:
            print('O numero e primo')
        else:
            print('E um numero primo')
else:
    print('O numero nao e primo')
    print('O numero nao e primo')