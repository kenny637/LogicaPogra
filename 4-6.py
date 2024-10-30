cont = 0
maior = 0
menor = 999
while True:
    cont += 1
    altura = int(input(f'Digite a altura do aluno {cont}: '))
    sn = str(input('Quer continuar')).upper()
    if maior < altura:
        maior = altura
    if menor > altura:
        menor = altura
    if sn == 'N':
        break
print(maior)
print(menor)