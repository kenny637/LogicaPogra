num1=int(input('Digite o total de vendas: '))
if num1 < 100:
    print('A comisão aumentou 0%')
elif num1 > 100 and num1 < 350:
    print('A comisão aumentou 6%')
    soma = (num1 / 6)+ num1
    print(soma)
elif num1 > 350:
    print('A comisão aumentou 10%')
    soma = (num1 / 10)+ num1
    print(soma)