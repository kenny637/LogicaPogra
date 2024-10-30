i = 0
cont = 0
while (i < 5):
    i += 1
    idade=int(input('Informe o Idade: '))
    peso=int(input('Informe o Peso : '))
    altura=float(input('Informe o Altura: '))
    if idade > 50:
        cont += 1
print(f'Tem {cont} pessoa com mais de 50 anos')
