print('=-'*17)
print('Vamos caucular A MEDIA ARITMEDICA')
print('=-'*17)
num1=float(input('Digite o primeriro numero: '))
num2=float(input('Digite o segundo numero: '))
num3=float(input('Digite o terceiro numero: '))
divisao=(num1+num2+num3)/3
print('A sua media é',divisao)
if divisao >= 7:
    print('Você foi provado')
else:
    print('Você nao foi aprovado')
print('A sua media é',divisao)



mes=int(input('Digite o um numero entre, 1 e 12: '))
if mes == 1:
    print('O mês Janeiro')
elif mes == 2:
    print('O mês Fevereiro')
elif mes == 3:
    print('O mês Março')
elif mes == 4:
    print('O mês Abril')
elif mes == 5:
    print('O mês Maio')
elif mes == 6:
    print('O mês Junho')
elif mes == 7:
    print('O mês Julho')
elif mes == 8:
    print('O mês Agosto')
elif mes == 9:
    print('O mês Setembro')
elif mes == 10:
    print('O mês Outubro')
elif mes == 11:
    print('O mês Novembro')
elif mes == 12:
    print('O mês Desembro')
else:
    print('O numero foi digitado icorretamente,\n Tente novamente ')



cod=int(input('Digite o Codigo de verificação entre, 1 e 11: '))
if cod == 1:
    print('O Pacote é de origem Sul')
elif cod == 2:
    print('O Pacote é de origem norte')
elif cod == 3:
    print('O Pacote é de origem Leste')
elif cod == 4:
    print('O Pacote é de origem Oeste')
elif cod == 5 or cod == 6:
    print('O Pacote é de origem Nordeste')
elif cod == 7 or cod == 8 or cod == 9:
    print('O Pacote é de origem Sudeste')
elif cod == 10:
    print('O Pacote é de origem Centro-Oeste')
elif cod == 11:
    print('O Pacote é de origem Noroeste')
else:
    print('O codigo esta incorreto')



dia=int(input('Quantos anos você tem: '))
ano = 360 * dia 
print('Você viveu',ano,'dias ')



num1=int(input('Digite o primeriro numero: '))
cubo = num1 * num1 * num1
quad = num1 * num1 
print('Cubo',cubo)
print('Quadrado',quad)



num1=int(input('Digite o primeriro numero: '))
num2=int(input('Digite o segundo numero: '))
soma=num1+num2
print('a Soma dos valor é',soma)