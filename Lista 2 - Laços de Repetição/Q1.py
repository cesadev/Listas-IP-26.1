#Primeiro eu Seto as variaveis vazias fora do while para poder ir fazendo a contagem e a adição das musicas.
contagem_musicas = 0 #Aqui eu conto a quantia de musicas adicionadas, pra no output eu mostrar
setlist = '' #Aqui eu concateno todas as musicas em uma string
musica_proibida = 'Voa, Voa Brabuleta' #Musica proibida em uma variavel pra ficar muito mais facil.

continuar = True
while continuar: 
    musica_escolhida = input() #o usuario escolhe uma musica

    if musica_escolhida.lower() == musica_proibida.lower(): #Se a musica escolhida em minusculo for igual a musica proibida em minusculo
        continuar = False #O booleano de continuar o while interrompe o codigo
    else: #Se não, adicionará a musica e continuará adicionando outras mais.
        if contagem_musicas ==0:
            setlist = musica_escolhida
        else:
            setlist += ' - ' + musica_escolhida
        contagem_musicas += 1

print('Bom dia, dona Maria! Aqui vão as músicas mais pedidas de hoje!')
print(f'A quantidade de músicas selecionadas foi {contagem_musicas}')
print(f'Setlist de músicas: {setlist}')
