print('CInFantasma - Defesa Sobrenatural do CIn!')
energia_danny = input()
tipo_fantasma = input()
energia_fantasma = input()
nome_fantasma = input()
portal_instavel = input()

if not energia_danny.isdigit() or not energia_fantasma.isdigit():
  print('Erro no Scanner Fenton: nível de energia inválido!')
else:
  energia_danny = int(energia_danny)
  energia_fantasma = int(energia_fantasma)
  if "king" in nome_fantasma.lower() or "lord" in nome_fantasma.lower():
    print('O Scanner detectou um possível fantasma de elite!')
  if len(nome_fantasma)>12:
    print('O nome do fantasma é assustadoramente longo...')
  if portal_instavel == "sim":
    print('O portal da Zona Fantasma continua instável!')
  else:
    print('O portal parece estar temporariamente estável.')
  if tipo_fantasma not in ['comum','raro','chefe'] and energia_fantasma>=70:
    print('Um fantasma misterioso apareceu no CIn!')
  if tipo_fantasma == 'chefe' and energia_fantasma>=80 and energia_danny>=energia_fantasma:
    print('Danny ativou o Modo Fantasma Total!')
  elif tipo_fantasma == 'raro' and energia_fantasma>=50 and energia_danny>=energia_fantasma:
    print('Danny capturou o fantasma com o Fenton Thermos!')
  elif energia_fantasma<20:
    print('Danny decidiu apenas observar o fantasma.')
  elif energia_fantasma>energia_danny:
    print('Danny percebeu que o fantasma é forte demais e decidiu recuar!')
  else:
    print('Danny enfrentou o fantasma normalmente!')