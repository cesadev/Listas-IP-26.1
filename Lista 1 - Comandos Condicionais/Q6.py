robin = input()
estelar = input()
ciborgue = input()
ravena = input()
mutano = input()
quantidade = 0
if robin == 'S':
    quantidade += 1
if estelar == 'S':
    quantidade += 1
if ciborgue == 'S':
    quantidade += 1
if ravena == 'S':
    quantidade += 1
if mutano == 'S':
    quantidade += 1
selecionado = ''
especial = ''
if quantidade == 0:
  print('Parece que ninguém quer participar da Liga da Justiça, o Batman vai ter que ouvir um Super-Esculacho do Super-Homem por não ter conseguido ninguém super forte!')
elif quantidade == 5:
  print('Em toda a vida do Batman, ele nunca viu um lugar tão caótico quanto a torre dos titãns depois da notícia, nem mesmo Gotham, com isso ele percebe que não seria ali o local ideal para encontrar o novo salvador da terra!')
elif quantidade == 1:
  print('Através de um processo seletivo rigoroso, o mais novo integrante da Liga da Justiça foi escolhido!')
  if robin == "S":
    selecionado ='Robin'
  elif ravena == "S":
    selecionado = 'Ravena'
  elif estelar == "S":
    selecionado = 'Estelar'
  elif ciborgue == "S":
    selecionado = 'Ciborgue'
  else:
    selecionado = 'Mutano'
elif 2<=quantidade<=4:
  if quantidade == 2:
    if robin == 'S' and estelar =='S':
      selecionado = 'Estelar'
      especial = 'amor'
    elif mutano == 'S' and ravena == 'S':
      selecionado = 'Ravena'
      especial = 'amor'
    elif mutano == 'S' and ciborgue == 'S':
      quantidade_mutano = int(input())
      quantidade_ciborgue = int(input())
      if quantidade_mutano > quantidade_ciborgue:
        selecionado = 'Mutano'
      elif quantidade_ciborgue >quantidade_mutano:
        selecionado = 'Ciborgue'
      else:
        selecionado = input()
      especial = 'tofu'
    else:
      if robin =="S":
        selecionado = 'Robin'
      elif ravena =="S":
        selecionado = 'Ravena'
      elif estelar =="S":
        selecionado = 'Estelar'
      elif ciborgue =="S":
        selecionado = 'Ciborgue'
      elif mutano =="S":
        selecionado = 'Mutano'
  elif quantidade == 3 or quantidade == 4:
    if robin == "S":
      selecionado = 'Robin'
    else:
      selecionado = 'Ravena'
      if ravena != 'S':
        especial = 'Ravena'
  print(f'Mesmo com {quantidade} candidatos, o(a) {selecionado} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {selecionado}!')
if selecionado == 'Robin':
  print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!')
elif selecionado == 'Ravena':
  print('Não tinha como a filha de Trigon não ser a escolhida, a mais forte dos Titãns vai botar os inimigos da Liga para correr!')
elif selecionado == 'Mutano':
  print('O herói mais versátil da torre está pronto para mostrar que tamanho não é documento, especialmente se ele virar um tiranossauro!')
elif selecionado == 'Ciborgue':
  print('BOOYAH! A tecnologia de ponta do Ciborgue agora faz parte do arsenal da Liga. Até parece que já foi antes...')
elif selecionado == 'Estelar':
  print('Com a fúria de Tamaran e o brilho das suas rajadas, a Estelar vai iluminar o caminho da Liga da Justiça!')
elif selecionado != 'Robin' and selecionado != 'Ravena' and selecionado != 'Mutano' and selecionado != 'Cigorgue' and selecionado != 'Estelar':
  print('Poxa, mas que pena, os Titãns vão ter que esperar mais um pouco antes de darem mais um passo na carreira, se continuar assim, vão assinar a CLT.')
  
if especial == 'amor':
  print('Parece que o cavalherismo ainda não morreu não é mesmo?')
elif especial == 'tofu':
  print('Nem uma competição árdua assim pode abalar a amizade desses caras!')
elif especial == 'Ravena':
  print('O Batman não iria perder a chance de ter um dos seres mais poderosos do Universo DC no time, o preparo dele não permite isso!')
elif especial == '':
  print('Que bom que tudo deu certo, sem dificuldades!')