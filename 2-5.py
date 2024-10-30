maior = 0
maior2 = 0
maior3 = 0

menor = 0
menor2 = 0
menor3 = 0
for i in range(1, 3):
    idade = int(input('idade: '))
    peso = int(input('peso: '))
    altura = int(input('altura: '))
    
    if i == 1:
        maior = idade
        maior2 = peso
        maior3 = altura
        menor = idade
        menor2 = peso
        menor3 = altura
    else:
        if  idade > maior:
            maior = idade
        if  peso > maior2:
            maior2 = peso
        if  altura > maior3:
            maior3 = altura
        
        if  idade < menor:
            menor = idade
        if  peso < menor2:
            menor2 = peso
        if  altura < menor3:
            menor3 = altura
print('A maior idade lido foi',maior)
print('O maior peso lido foi ',maior2)
print('A maior altura lido foi',maior3) 
print('A menor idade lido foi',menor)
print('O menor peso lido foi ',menor2)
print('A menor altura lido foi',menor3)