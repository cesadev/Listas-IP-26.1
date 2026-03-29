def is_balanced(bracket):
    stack = ''
    for c in bracket:
        if c in '({[':
            stack = c + stack  # push
        else:
            if not stack:
                return False
            # get top
            top = None
            for ch in stack:
                top = ch
                break
            # check
            if (c == ')' and top != '(') or (c == '}' and top != '{') or (c == ']' and top != '['):
                return False
            # pop
            stack = stack[1:]
    return stack == ''

qtd_cidades = int(input())
print("Pega a sua trouxa, moleque. O ônibus pro sertão já vai sair.")
print(f"Se ajeita nesse banco, menino, que o chacoalho vai ser grande. A gente tem {qtd_cidades} cidade(s) de poeira pela frente até achar o tal do teu pai. Presta atenção no que o povo fala...")

found = False
for city in range(1, qtd_cidades + 1):
    print(f"Atenção, {city}ª cidade! Carta de graça! A gente só quer informação da minha família em troca!")
    bracket = ''
    has_identity = False
    has_address = False
    has_memory = False
    open_jesus = False
    open_isaias = False
    open_moises = False
    open_sertao = False
    open_bom_jesus = False
    open_memory = False
    infos = []
    while True:
        info = input().strip()
        if info == 'FIM':
            break
        infos.append(info)
        # find word
        word = None
        if 'bom jesus' in info:
            word = 'bom jesus'
        elif 'sertao' in info:
            word = 'sertao'
        elif 'jesus' in info:
            word = 'jesus'
        elif 'isaias' in info:
            word = 'isaias'
        elif 'moises' in info:
            word = 'moises'
        else:
            word = 'memory'
        if word in ['jesus', 'isaias', 'moises']:
            has_identity = True
            if word == 'jesus':
                if not open_jesus:
                    bracket += '('
                    open_jesus = True
                else:
                    bracket += ')'
                    open_jesus = False
            elif word == 'isaias':
                if not open_isaias:
                    bracket += '('
                    open_isaias = True
                else:
                    bracket += ')'
                    open_isaias = False
            elif word == 'moises':
                if not open_moises:
                    bracket += '('
                    open_moises = True
                else:
                    bracket += ')'
                    open_moises = False
        elif word in ['sertao', 'bom jesus']:
            has_address = True
            if word == 'sertao':
                if not open_sertao:
                    bracket += '{'
                    open_sertao = True
                else:
                    bracket += '}'
                    open_sertao = False
            elif word == 'bom jesus':
                if not open_bom_jesus:
                    bracket += '{'
                    open_bom_jesus = True
                else:
                    bracket += '}'
                    open_bom_jesus = False
        else:
            has_memory = True
            if open_memory:
                bracket += ']'
                open_memory = False
            else:
                bracket += '['
                open_memory = True
    if not infos:
        print("Ô cidadezinha morta, Josué. Ninguém abriu a boca pra dar um pio do teu pai. Dobra essa mesa que aqui a gente só gastou saliva à toa.")
        continue
    if is_balanced(bracket) and has_identity and has_address and has_memory:
        print("A história bateu, Josué. O povo falou a mesma coisa. Pega tuas coisas que a gente achou o caminho do teu pai.")
        found = True
        break
    else:
        if city != qtd_cidades:
            print("Essa conversa tá toda torta, um fala uma coisa, outro fala outra. Vamos embora, menino, a busca continua.")
if found:
    print("------------------------------------------------------------")
    print("✅ Pistas confirmadas. Josué encontrou os irmãos e uma carta de seu pai.")
    print("A missão de Dora terminou. Pela janela do ônibus, ela escreve para o menino que deixou para trás:")
    print("✉️ Dora: 'Você tem razão. Seu pai ainda vai aparecer e, com certeza, ele é tudo aquilo que você diz que ele é.'")
    print("✉️ Dora: 'Quando você estiver cruzando as estradas no seu caminhão enorme, espero que você lembre que fui eu a primeira pessoa a te fazer botar a mão no volante.'")
    print("✉️ Dora: 'No dia que você quiser lembrar de mim, dá uma olhada no retratinho que a gente tirou junto... Tenho medo que um dia você também me esqueça. Tenho saudade de tudo.'")
else:
    print("Não achamos eles nessas cidades, Dona Dora... Mas amanhã a gente bota a mesinha de novo, né? O Brasil é grande, uma hora a gente encontra.")
                pilha += abre
                infos += chave + "|"

            else:
                pilha += fecha


        else: #Se for "FIM", verifica se pilha ta certinho e vai pra prox cidade
            if cidade < qtd_cidades and teve_info == False:
                print('Ô cidadezinha morta, Josué. Ninguém abriu a boca pra dar um pio do teu pai. Dobra essa mesa que aqui a gente só gastou saliva à toa.')

            #funçao de verificar se a pilha ta certa
            elif teve_info == True:
                mudou = True
                while mudou:
                    ultimo = ''
                    nova_pilha = ''
                    mudou = False

                    for i in pilha:
                        if (ultimo == '(' and i == ')') or (ultimo == '{' and i == '}') or (ultimo == '[' and i == ']'):

                            ultimo = ''
                            mudou = True
                        else:
                            if ultimo:
                                nova_pilha += ultimo
                            ultimo = i

                    if ultimo:
                        nova_pilha += ultimo

                    pilha = nova_pilha

                    #pilha vai ser a nova pilha entao se len(pilha) == 0 é valido

                if len(pilha) == 0 and "identidade" in infos and "endereco" in infos and "lembranca" in infos:    
                    print("A história bateu, Josué. O povo falou a mesma coisa. Pega tuas coisas que a gente achou o caminho do teu pai.")
                    encontrou = True

                elif len(pilha) == 0 and cidade < qtd_cidades:
                    print("Essa conversa tá toda torta, um fala uma coisa, outro fala outra. Vamos embora, menino, a busca continua.")

                elif len(pilha) != 0 and cidade < qtd_cidades:
                    print("Essa conversa tá toda torta, um fala uma coisa, outro fala outra. Vamos embora, menino, a busca continua.")

            cidade += 1  #aumenta a cidade e vai pra prox
if encontrou == True:
    print("------------------------------------------------------------")
    print("✅ Pistas confirmadas. Josué encontrou os irmãos e uma carta de seu pai.")
    print("A missão de Dora terminou. Pela janela do ônibus, ela escreve para o menino que deixou para trás:")
    print("✉️ Dora: 'Você tem razão. Seu pai ainda vai aparecer e, com certeza, ele é tudo aquilo que você diz que ele é.'")
    print("✉️ Dora: 'Quando você estiver cruzando as estradas no seu caminhão enorme, espero que você lembre que fui eu a primeira pessoa a te fazer botar a mão no volante.'")
    print("✉️ Dora: 'No dia que você quiser lembrar de mim, dá uma olhada no retratinho que a gente tirou junto... Tenho medo que um dia você também me esqueça. Tenho saudade de tudo.'")

else:
    print("Não achamos eles nessas cidades, Dona Dora... Mas amanhã a gente bota a mesinha de novo, né? O Brasil é grande, uma hora a gente encontra.")