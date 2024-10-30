'''num1=int(input('Digite o primeriro numero: '))
num2=int(input('Digite o segundo numero: '))
if num1 > num2:
    menos = num1 - num2
    print('A difereça entre',num1,'e',num2,'é',menos )
else:
    print('A numero 1 e maior que o numero 2')

num1=float(input('Digite um numero: '))
if num1 > 50:
    metade = num1 / 2
    print('a metade do valor é',metade)
else:
    print('O numero e menor que 50')

num1=int(input('Digite um numero: '))
if num1 > 90 and num1 < 100:
    print('O dobro do numero é',num1 * 2)   
elif num1 < 90:
     print('O numero e menor 90')
else:
    print('O numero é maior que 100')

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

num1=int(input('Digite um numero: '))
if num1 > 0:
    if num1 % 2 == 0:
        print('O numero e par')
    else:
        print('O numero e impar')
else:
    print('O numero e negaivo')'''







maior = media = menor = 0
n1=int(input('Digite o primeriro numero: '))
n2=int(input('Digite o segundo numero: '))
n3=int(input('Digite o terceiro numero: '))
if n1 > n2:
    maior = n1
elif n2 > n3:
    maior = n2
elif n3 > n1:
    maior = n3

if n1 > n2 and n1 < n3:
    media = n1
elif n1 < n2 and n1 > n3:
    media = n1
elif n2 > n3 and n2 < n1:
    media = n2
elif n2 < n3 and n2 > n1:
    media = n2
elif n3 > n1 and n3 < n2:
    media = n3
elif n3 < n1 and n3 > n2:
    media = n3


if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n3 and n2 < n1:
    menor = n2
elif n3 < n1 and n3 < n1:
    menor = n3 

print('O numero ',menor)
print('O numero ',media)
print('O numero ',maior)


