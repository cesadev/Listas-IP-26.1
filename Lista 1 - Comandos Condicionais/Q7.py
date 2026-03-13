#inputs
maquina1 = input('')
pecas1 = int(input(''))
reacao1 = input('')

maquina2 = input('')
pecas2 = int(input(''))
reacao2 = input('')

maquina3 = input('')
pecas3 = int(input(''))
reacao3 = input('')

maquina4 = input('')
pecas4 = int(input(''))
reacao4 = input('')

#calculos 1
pontuacao_inicial1 = len(maquina1) + pecas1
if "i" in maquina1 and "n" in maquina1 and "a" in maquina1 and "t" in maquina1 and "o" in maquina1 and "r" in maquina1:
    pontuacao_inicial1 -= 50
if "P" in maquina1 and "e" in maquina1 and "r" in maquina1 and "y" in maquina1:
    pontuacao_inicial1 += 20
if maquina1 == "MáquinaDeBanhoForçado":
    pontuacao_inicial1 -= 20
#calculos-reacoes 1 
if reacao1 == "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!":
    pontuacao_inicial1 += 30
elif reacao1 == "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!":
    pontuacao_inicial1 += 20
elif reacao1 == "OK... ISSO É BEM ESTRANHO.":
    pontuacao_inicial1 += 10
elif reacao1 == "AH, NEM É TÃO IMPRESSIONANTE ASSIM.":
    pontuacao_inicial1 = pontuacao_inicial1
elif reacao1 == "SÉRIO? SÓ ISSO?":
    pontuacao_inicial1 -= 5
elif reacao1 == "MÃE! A MÁQUINA SUMIU DE NOVO!":
    pontuacao_inicial1 -= 10
elif reacao1 == "AH, ESQUECE…":
    pontuacao_inicial1 -= 15
#calculo-final 1
pontuacao_final1 = pontuacao_inicial1
if maquina1 == "HidromassagemAutomáticaDoPerry":
    pontuacao_final1 *= 2

#calculos 2
pontuacao_inicial2 = len(maquina2) + pecas2
if "i" in maquina2 and "n" in maquina2 and "a" in maquina2 and "t" in maquina2 and "o" in maquina2 and "r" in maquina2:
    pontuacao_inicial2 -= 50
if "P" in maquina2 and "e" in maquina2 and "r" in maquina2 and "y" in maquina2:
    pontuacao_inicial2 += 20
if maquina2 == "MáquinaDeBanhoForçado":
    pontuacao_inicial2 -= 20
#calculos-reacoes 2 
if reacao2 == "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!":
    pontuacao_inicial2 += 30
elif reacao2 == "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!":
    pontuacao_inicial2 += 20
elif reacao2 == "OK... ISSO É BEM ESTRANHO.":
    pontuacao_inicial2 += 10
elif reacao2 == "AH, NEM É TÃO IMPRESSIONANTE ASSIM.":
    pontuacao_inicial2 = pontuacao_inicial2
elif reacao2 == "SÉRIO? SÓ ISSO?":
    pontuacao_inicial2 -= 5
elif reacao2 == "MÃE! A MÁQUINA SUMIU DE NOVO!":
    pontuacao_inicial2 -= 10
elif reacao2 == "AH, ESQUECE…":
    pontuacao_inicial2 -= 15
#calculo-final 2
pontuacao_final2 = pontuacao_inicial2
if maquina2 == "HidromassagemAutomáticaDoPerry":
    pontuacao_final2 *= 2

#calculos 3
pontuacao_inicial3 = len(maquina3) + pecas3
if "i" in maquina3 and "n" in maquina3 and "a" in maquina3 and "t" in maquina3 and "o" in maquina3 and "r" in maquina3:
    pontuacao_inicial3 -= 50
if "P" in maquina3 and "e" in maquina3 and "r" in maquina3 and "y" in maquina3:
    pontuacao_inicial3 += 20
if maquina3 == "MáquinaDeBanhoForçado":
    pontuacao_inicial3 -= 20
#calculos-reacoes 13
if reacao3 == "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!":
    pontuacao_inicial3 += 30
elif reacao3 == "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!":
    pontuacao_inicial3 += 20
elif reacao3 == "OK... ISSO É BEM ESTRANHO.":
    pontuacao_inicial3 += 10
elif reacao3 == "AH, NEM É TÃO IMPRESSIONANTE ASSIM.":
    pontuacao_inicial3 = pontuacao_inicial3
elif reacao3 == "SÉRIO? SÓ ISSO?":
    pontuacao_inicial3 -= 5
elif reacao3 == "MÃE! A MÁQUINA SUMIU DE NOVO!":
    pontuacao_inicial3 -= 10
elif reacao3 == "AH, ESQUECE…":
    pontuacao_inicial3 -= 15
#calculo-final 3
pontuacao_final3 = pontuacao_inicial3
if maquina3 == "HidromassagemAutomáticaDoPerry":
    pontuacao_final3 *= 2

#calculos 4
pontuacao_inicial4 = len(maquina4) + pecas4
if "i" in maquina4 and "n" in maquina4 and "a" in maquina4 and "t" in maquina4 and "o" in maquina4 and "r" in maquina4:
    pontuacao_inicial4 -= 50
if "P" in maquina4 and "e" in maquina4 and "r" in maquina4 and "y" in maquina4:
    pontuacao_inicial4 += 20
if maquina4 == "MáquinaDeBanhoForçado":
    pontuacao_inicial4 -= 20
#calculos-reacoes 4 
if reacao4 == "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!":
    pontuacao_inicial4 += 30
elif reacao4 == "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!":
    pontuacao_inicial4 += 20
elif reacao4 == "OK... ISSO É BEM ESTRANHO.":
    pontuacao_inicial4 += 10
elif reacao4 == "AH, NEM É TÃO IMPRESSIONANTE ASSIM.":
    pontuacao_inicial4 = pontuacao_inicial4
elif reacao4 == "SÉRIO? SÓ ISSO?":
    pontuacao_inicial4 -= 5
elif reacao4 == "MÃE! A MÁQUINA SUMIU DE NOVO!":
    pontuacao_inicial4 -= 10
elif reacao4 == "AH, ESQUECE…":
    pontuacao_inicial4 -= 15
#calculo-final 4
pontuacao_final4 = pontuacao_inicial4
if maquina4 == "HidromassagemAutomáticaDoPerry":
    pontuacao_final4 *= 2

#ranking

#1 e 2
if pontuacao_final1<pontuacao_final2:
    maquina1, maquina2 = maquina2, maquina1
    pecas1, pecas2 = pecas2, pecas1
    pontuacao_final1, pontuacao_final2 = pontuacao_final2, pontuacao_final1
elif pontuacao_final1 == pontuacao_final2:
    p1 = 0
    p2 = 0
    if pecas1>25:
        p1 += 1
    if len(maquina1)>15:
        p1 += 1
    if pecas2>25:
        p2 += 1
    if len(maquina2)>15:
        p2 += 1
    if p1<p2:
        maquina1, maquina2 = maquina2, maquina1
        pecas1, pecas2 = pecas2, pecas1
        pontuacao_final1, pontuacao_final2 = pontuacao_final2, pontuacao_final1
    elif p1==p2:
        if pecas1<pecas2:
            maquina1, maquina2 = maquina2, maquina1
            pecas1, pecas2 = pecas2, pecas1
            pontuacao_final1, pontuacao_final2 = pontuacao_final2, pontuacao_final1
        elif pecas1 == pecas2:
            if len(maquina1) < len(maquina2):
                maquina1, maquina2 = maquina2, maquina1
                pecas1, pecas2 = pecas2, pecas1
                pontuacao_final1, pontuacao_final2 = pontuacao_final2, pontuacao_final1
#2 e 3
if pontuacao_final2<pontuacao_final3:
    maquina2, maquina3 = maquina3, maquina2
    pecas2, pecas3 = pecas3, pecas2
    pontuacao_final2, pontuacao_final3 = pontuacao_final3, pontuacao_final2
elif pontuacao_final2 == pontuacao_final3:
    p2 = 0
    p3 = 0
    if pecas2>25:
        p2 += 1
    if len(maquina2)>15:
        p2 += 1
    if pecas3>25:
        p3 += 1
    if len(maquina3)>15:
        p3 += 1
    if p2<p3:
        maquina2, maquina3 = maquina3, maquina2
        pecas2, pecas3 = pecas3, pecas2
        pontuacao_final2, pontuacao_final3 = pontuacao_final3, pontuacao_final2
    elif p2==p3:
        if pecas2<pecas3:
            maquina2, maquina3 = maquina3, maquina2
            pecas2, pecas3 = pecas3, pecas2
            pontuacao_final2, pontuacao_final3 = pontuacao_final3, pontuacao_final2
        elif pecas2 == pecas3:
            if len(maquina2) < len(maquina3):
                maquina2, maquina3 = maquina3, maquina2
                pecas2, pecas3 = pecas3, pecas2
                pontuacao_final2, pontuacao_final3 = pontuacao_final3, pontuacao_final2
#3 e 4
if pontuacao_final3<pontuacao_final4:
    maquina3, maquina4 = maquina4, maquina3
    pecas3, pecas4 = pecas4, pecas3
    pontuacao_final3, pontuacao_final4 = pontuacao_final4, pontuacao_final3
elif pontuacao_final3 == pontuacao_final4:
    p3 = 0
    p4 = 0
    if pecas3>25:
        p3 += 1
    if len(maquina3)>15:
        p3 += 1
    if pecas4>25:
        p4 += 1
    if len(maquina4)>15:
        p4 += 1
    if p3<p4:
        maquina3, maquina4 = maquina4, maquina3
        pecas3, pecas4 = pecas4, pecas3
        pontuacao_final3, pontuacao_final4= pontuacao_final4, pontuacao_final3
    elif p3==p4:
        if pecas3<pecas4:
            maquina3, maquina4 = maquina4, maquina3
            pecas3, pecas4 = pecas4, pecas3
            pontuacao_final3, pontuacao_final4 = pontuacao_final4, pontuacao_final3
        elif pecas3 == pecas4:
            if len(maquina3) < len(maquina4):
                maquina3, maquina4 = maquina4, maquina3
                pecas3, pecas4 = pecas4, pecas3
                pontuacao_final3, pontuacao_final4 = pontuacao_final4, pontuacao_final3
#1 e 2
if pontuacao_final1<pontuacao_final2:
    maquina1, maquina2 = maquina2, maquina1
    pecas1, pecas2 = pecas2, pecas1
    pontuacao_final1, pontuacao_final2 = pontuacao_final2, pontuacao_final1
elif pontuacao_final1 == pontuacao_final2:
    p1 = 0
    p2 = 0
    if pecas1>25:
        p1 += 1
    if len(maquina1)>15:
        p1 += 1
    if pecas2>25:
        p2 += 1
    if len(maquina2)>15:
        p2 += 1
    if p1<p2:
        maquina1, maquina2 = maquina2, maquina1
        pecas1, pecas2 = pecas2, pecas1
        pontuacao_final1, pontuacao_final2 = pontuacao_final2, pontuacao_final1
    elif p1==p2:
        if pecas1<pecas2:
            maquina1, maquina2 = maquina2, maquina1
            pecas1, pecas2 = pecas2, pecas1
            pontuacao_final1, pontuacao_final2 = pontuacao_final2, pontuacao_final1
        elif pecas1 == pecas2:
            if len(maquina1) < len(maquina2):
                maquina1, maquina2 = maquina2, maquina1
                pecas1, pecas2 = pecas2, pecas1
                pontuacao_final1, pontuacao_final2 = pontuacao_final2, pontuacao_final1
#2 e 3
if pontuacao_final2<pontuacao_final3:
    maquina2, maquina3 = maquina3, maquina2
    pecas2, pecas3 = pecas3, pecas2
    pontuacao_final2, pontuacao_final3 = pontuacao_final3, pontuacao_final2
elif pontuacao_final2 == pontuacao_final3:
    p2 = 0
    p3 = 0
    if pecas2>25:
        p2 += 1
    if len(maquina2)>15:
        p2 += 1
    if pecas3>25:
        p3 += 1
    if len(maquina3)>15:
        p3 += 1
    if p2<p3:
        maquina2, maquina3 = maquina3, maquina2
        pecas2, pecas3 = pecas3, pecas2
        pontuacao_final2, pontuacao_final3 = pontuacao_final3, pontuacao_final2
    elif p2==p3:
        if pecas2<pecas3:
            maquina2, maquina3 = maquina3, maquina2
            pecas2, pecas3 = pecas3, pecas2
            pontuacao_final2, pontuacao_final3 = pontuacao_final3, pontuacao_final2
        elif pecas2 == pecas3:
            if len(maquina2) < len(maquina3):
                maquina2, maquina3 = maquina3, maquina2
                pecas2, pecas3 = pecas3, pecas2
                pontuacao_final2, pontuacao_final3 = pontuacao_final3, pontuacao_final2
#1 e 2
if pontuacao_final1<pontuacao_final2:
    maquina1, maquina2 = maquina2, maquina1
    pecas1, pecas2 = pecas2, pecas1
    pontuacao_final1, pontuacao_final2 = pontuacao_final2, pontuacao_final1
elif pontuacao_final1 == pontuacao_final2:
    p1 = 0
    p2 = 0
    if pecas1>25:
        p1 += 1
    if len(maquina1)>15:
        p1 += 1
    if pecas2>25:
        p2 += 1
    if len(maquina2)>15:
        p2 += 1
    if p1<p2:
        maquina1, maquina2 = maquina2, maquina1
        pecas1, pecas2 = pecas2, pecas1
        pontuacao_final1, pontuacao_final2 = pontuacao_final2, pontuacao_final1
    elif p1==p2:
        if pecas1<pecas2:
            maquina1, maquina2 = maquina2, maquina1
            pecas1, pecas2 = pecas2, pecas1
            pontuacao_final1, pontuacao_final2 = pontuacao_final2, pontuacao_final1
        elif pecas1 == pecas2:
            if len(maquina1) < len(maquina2):
                maquina1, maquina2 = maquina2, maquina1
                pecas1, pecas2 = pecas2, pecas1
                pontuacao_final1, pontuacao_final2 = pontuacao_final2, pontuacao_final1
#print final
print(f'1º lugar - {maquina1} : {pontuacao_final1} pontos')
print(f'2º lugar - {maquina2} : {pontuacao_final2} pontos')
print(f'3º lugar - {maquina3} : {pontuacao_final3} pontos')
print(f'4º lugar - {maquina4} : {pontuacao_final4} pontos')