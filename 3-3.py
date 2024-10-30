rj = 0
bh = 0
sc = 0
cidade = ' '
while cidade not in 'FIM':
    cidade = str(input('digite um numero')).upper()
    if cidade == 'RJ':
        rj += 1
    if cidade == 'BH':
        bh += 1
    if cidade == 'SC':
        sc += 1
print('RJ foi digitado ', rj)
print('BH foi digitado ', bh)
print('SC foi digitado ', sc)