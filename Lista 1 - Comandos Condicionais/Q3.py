print('Ben: Tá na hora de virar herói!')
alien = input()
if alien == 'Chama' or alien == 'XLR8' or alien == 'Diamante' or alien == 'Besta' or alien == 'Ultra-T':
  print(f'Ben: Bora lá, {alien}!')
  print('Gwen: Boa, Ben, agora vamos, temos que encontrar Azmuth.')
  if alien == 'Chama':
    print('Ben: Eu tô pegando fogo!')
  if alien == 'XLR8':
    print('Ben: Vamos encontrar ele bem rápido com o XLR8!')
else:
  print(f'Ben: Droga, Não consigo me transformar no {alien}.')
  print('Gwen: Ben Tennyson! Pare com a Bobeira.')
  if alien == 'Insectoide':
    print('Gwen: Ben, de todos os seus bichos, você tentou escolher esse?')
  if alien == 'Fantasmático':
    print("Ben: Zs'skayr... Ainda bem que o relógio não funcionou.")