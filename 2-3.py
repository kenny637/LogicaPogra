soma2 = 0
soma = 0
for i in range(5):
    num=int(input('digite um numero'))
    soma = soma + num
    media= soma / 5
    if num >= 0:
        soma2 = soma2 + num
print(media)
print(soma2)
