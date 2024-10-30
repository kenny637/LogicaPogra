jose = 0
joao = 0
maria = 0
meunego = 0
nulo = 0
branco = 0
soma = soma2 = 0

print('1)José\n'
          '2)João\n'
          '3)Maria\n'
          '4)Meu nego\n'
          '5)Nulo\n'
          '6)Branco\n')
num = 1
while num > 0:
    num = int(input('digite um numero para votar'))
    if num > 0:
        if num == 1:
            jose += 1
        if num == 2:
            joao += 1
        if num == 3:
            maria += 1
        if num == 4:
            meunego += 1
        if num == 5:
            nulo += 1
        if num == 6:
            branco += 1
        if num > 6:
            print('\033[1;31mINVALIDO\033[m')
soma =  branco / (jose + joao + maria + meunego) * 100
soma2 = nulo / (jose + joao + maria + meunego) * 100
print('José recebeu',jose)
print('João recebeu',joao)
print('Maria recebeu',maria)
print('Meu nego recebeu',meunego)
print('Votos nulo',nulo)
print('Votos branco',branco)
print(f'{soma:.1f}%')
print(f'{soma2:.1f}%')
