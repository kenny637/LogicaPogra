from random import randint
import time

turno = 0 # S

escolha_jogador = 0 # S
IA_acao = 0

vida_inimigo = 100 # s
vida_max_i = 100 # s
IA_padrao = []
identificar_padrao = []
jogador_leitura = [0, 0, 0, 0, 0, 0] 
IA_estilo = randint(1, 4) # 1 defensivo, 2 mago, 3 ofensivo, 4 neutro

def jogador_escolha():
    global escolha_jogador
    print("Escolha uma ação:")
    print("1. Atacar")
    print("2. Defender")
    print("3. Esquivar")
    print("4. Usar magia")
    print("5. Curar")
    print("6. Recuperar mana")
    
    while True:
        try:
            escolha_jogador = int(input("Digite o número da ação desejada: "))
            if escolha_jogador in [1, 2, 3, 4, 5, 6]:
                break
            else:
                print("Opção inválida. Por favor, escolha um número entre 1 e 6.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def IA_inimigo():
    global escolha_jogador, vida_inimigo, vida_max_i, identificar_padrao, IA_padrao, IA_acao, jogador_leitura, IA_estilo

    identificar_padrao.append(escolha_jogador)
    IA_padrao.append(IA_acao)
    if len(IA_padrao) > 3:
        IA_padrao.pop(0)
    if len(identificar_padrao) > 10:
        identificar_padrao.pop(0)

    if IA_estilo == 0:
        ataque = 20
        defesa = 20 
        esquiva = 20
        magia = 20  
        cura = 10
        mana = 10

    
    if IA_estilo == 1: # estilo defensivo
        ataque = 20
        defesa = 30
        esquiva = 25
        magia = 15
        cura = 5
        mana = 5
    elif IA_estilo == 2: # estilo mago
        ataque = 15
        defesa = 10
        esquiva = 10
        magia = 30
        cura = 25
        mana = 10
    elif IA_estilo == 3: # estilo ofensivo
        ataque = 35
        defesa = 15
        esquiva = 10
        magia = 30
        cura = 5
        mana = 5    
    elif IA_estilo == 4: # estilo neutro
        ataque = 25
        defesa = 20
        esquiva = 15
        magia = 20
        cura = 10
        mana = 10 

    def IA_estados(ataque, defesa, esquiva,magia, cura, mana):
        if IA_padrao[-2:] != [5, 5]: # se o inimigo curou
            if vida_inimigo <= vida_max_i * 0.2: # estado crítico
                ataque = 40
                magia = 30
                defesa = 0
                esquiva = 0
                cura = 30
                mana = 0    
                return ataque, defesa, esquiva, magia, cura, mana
            elif vida_inimigo <= vida_max_i * 0.5: # estado de perigo
                ataque = 35
                magia = 30
                defesa = 10
                esquiva = 5
                cura = 20
                mana = 0
            elif vida_inimigo <= vida_max_i * 0.7: # estado de alerta
                ataque = 30
                magia = 25
                defesa = 15
                esquiva = 10
                cura = 15
                mana = 5
            
        # ler padrao de escolha do jogador
        if identificar_padrao[-1] == 1: #ataque e defesa
            jogador_leitura[0] += 1
        elif identificar_padrao[-1] == 2: # ataque e cura
            jogador_leitura[1] += 1
        elif identificar_padrao[-1] == 3:  # magia e mana 
            jogador_leitura[2] += 1
        elif identificar_padrao[-1] == 4: # ataque e ataque ou defesa e defesa
            jogador_leitura[3] += 1
        elif identificar_padrao[-1] == 5: # defesa e cura
            jogador_leitura[4] += 1
        elif identificar_padrao[-1] == 6: # esquiva e mana
            jogador_leitura[5] += 1
        
        probabilidade = [0,0,0,0,0,0]
        soma = sum(jogador_leitura) # sempre o numero do jogador vem antes entao nao causa erro de indice
        if soma == 0:
            return ataque,defesa, esquiva, magia, cura, mana 

        divisao = 100 / soma
        for i in range(6):
            if jogador_leitura[i] > 0:
                probabilidade[i] = int(jogador_leitura[i] * divisao) 
        print(jogador_leitura)
        print(soma)
        print(probabilidade)

        if probabilidade[0] > 30: # ataque
            esquiva = min(50, esquiva + 10)
            defesa = min(50, defesa + 10)
            ataque = max(0, ataque - 10)
            magia = max(0, magia - 10)
            if probabilidade[0] > 70:
                esquiva = max(0, esquiva - 30)
                defesa = max(0, defesa - 30)
                ataque = min(50, ataque + 40)
                magia = min(50, magia + 40)
                cura = max(0, cura - 5)
                mana = max(0, mana - 5)
        elif probabilidade[3] > 30: # magia
            esquiva =  min(50, esquiva + 10)
            defesa =  min(50, defesa + 10)
            ataque = max(0, ataque - 10)
            magia = max(0, magia - 10)
        if probabilidade[1] > 30: # defesa
            magia = min(50, magia + 10)
            ataque =  min(50, ataque + 10)
            cura =  min(50, cura + 10)
            defesa = max(0, defesa - 10)
            esquiva = max(0, esquiva - 10)
            mana = max(0, mana - 10)
        elif probabilidade[2] > 30: # esquiva
            magia =  min(50, magia + 10)
            ataque =  min(50, ataque + 10)
            defesa = max(0, defesa - 20)
        if probabilidade[4] > 30: # cura
            ataque =  min(50, ataque + 10)
            magia =  min(50, magia + 10)
            esquiva = max(0, esquiva - 10)
            defesa = max(0, defesa - 10)
        elif probabilidade[5] > 30:
            ataque =  min(50, ataque + 10)
            magia =  min(50, magia + 10)
            cura =  min(50, cura + 10)
            defesa = max(0, defesa - 15)
            mana = max(0, mana - 5)
            esquiva = max(0, esquiva - 5)
        print(ataque, defesa, esquiva, magia, cura, mana)
        return ataque, defesa, esquiva, magia, cura, mana


    ataque, defesa, esquiva, magia, cura, mana = IA_estados(ataque, defesa, esquiva, magia, cura, mana)
    print( ataque, defesa, esquiva, magia, cura, mana)

    soma = ataque + defesa + esquiva + magia + cura + mana
    pensamento = randint(1, soma)
    
    if pensamento:
        if pensamento <= ataque:
            IA_acao = 1
            print("O inimigo atacou!")
            return IA_acao
        elif pensamento <= ataque + defesa:
            IA_acao = 2
            print("O inimigo se defendeu!")
            return IA_acao
        elif pensamento <= ataque + defesa + esquiva:
            IA_acao = 3
            print("O inimigo tentou esquivar!")
            return IA_acao
        elif pensamento <= ataque + defesa + esquiva + magia:  
            IA_acao = 4
            print("O inimigo usou magia!")
            return IA_acao
        elif pensamento <= ataque + defesa + esquiva + magia + cura:
            IA_acao = 5
            print("O inimigo se curou!")
            return IA_acao
        else:
            IA_acao = 6
            print("O inimigo recuperou mana!")
            return IA_acao
    
while True:
    jogador_escolha()
    IA_inimigo()    
    turno += 1
    print(f"\nTurno {turno}")
    time.sleep(0.5)