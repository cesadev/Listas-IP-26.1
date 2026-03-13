velocidade_IJ = int(input(''))
velocidade_LR = int(input(''))
dificuldade_inimigos = int(input(''))
pontuacao_final = (velocidade_IJ*velocidade_LR)/dificuldade_inimigos
if pontuacao_final <= 65000:
  print("BRUTAL! Ninguém jamais conseguiu alcançar as pontuações fantásticas do Jorel.")
elif 65000<pontuacao_final<=99000:
  print('INCRÍVEL! A dupla conseguiu alcançar o top 10 nas pontuações do jogo.')
elif 99000<pontuacao_final<=153000:
  print('SENSACIONAL!! Os jogadores conseguiram alcançar o pódio do jogo ao lado das outras pontuações do Jorel.')
else:
  print('IMPOSSÍVEL!!! A DUPLA IMPLACÁVEL FOI CAPAZ DE QUEBRAR O RECORDE INALCANÇÁVEL DO JOREL!')