qtd_cidades = int(input())
print("Pega a sua trouxa, moleque. O ônibus pro sertão já vai sair.")
print(f"Se ajeita nesse banco, menino, que o chacoalho vai ser grande. A gente tem {qtd_cidades} cidade(s) de poeira pela frente até achar o tal do teu pai. Presta atenção no que o povo fala...")

#Passei muitas horas aprendendo essa bomba.
#Fiz, Refiz, refiz denovo, apaguei os comentarios, fiz com funçoes, fiz com indexaçao, fiz com listas pra só dps conseguir descer o nivel pra o da lista 2
#Ta bagunçado mas sinceramente tá rodando, nas proximas listas vou começar a fazer comentários mais precisos sobre cada parte do meu codigo
#Mas esse aqui foi tao denso pra chegar na lógica que derreti

encontrou = False
cidade = 1
while cidade <= qtd_cidades and not encontrou:
    print(f"Atenção, {cidade}ª cidade! Carta de graça! A gente só quer informação da minha família em troca!")
    simbolos = ''
    teve_identidade = False
    teve_endereco = False
    teve_lembranca = False
    aberto_jesus = False
    aberto_isaias = False
    aberto_moises = False
    aberto_sertao = False
    aberto_bom_jesus = False
    aberto_lembranca = False
    num_informacoes = 0
    continuar_coleta = True
    while continuar_coleta:
        info = input()
        if info == 'FIM':
            continuar_coleta = False
        else:
            num_informacoes += 1
            #encontrar palavra
            palavra = None
            if 'bom jesus' in info:
                palavra = 'bom jesus'
            elif 'sertao' in info:
                palavra = 'sertao'
            elif 'jesus' in info:
                palavra = 'jesus'
            elif 'isaias' in info:
                palavra = 'isaias'
            elif 'moises' in info:
                palavra = 'moises'
            else:
                palavra = 'lembranca'
            if palavra == 'jesus' or palavra == 'isaias' or palavra == 'moises':
                teve_identidade = True
                if palavra == 'jesus':
                    if not aberto_jesus:
                        simbolos += '('
                        aberto_jesus = True
                    else:
                        simbolos += ')'
                        aberto_jesus = False
                elif palavra == 'isaias':
                    if not aberto_isaias:
                        simbolos += '('
                        aberto_isaias = True
                    else:
                        simbolos += ')'
                        aberto_isaias = False
                elif palavra == 'moises':
                    if not aberto_moises:
                        simbolos += '('
                        aberto_moises = True
                    else:
                        simbolos += ')'
                        aberto_moises = False
            elif palavra == 'sertao' or palavra == 'bom jesus':
                teve_endereco = True
                if palavra == 'sertao':
                    if not aberto_sertao:
                        simbolos += '{'
                        aberto_sertao = True
                    else:
                        simbolos += '}'
                        aberto_sertao = False
                elif palavra == 'bom jesus':
                    if not aberto_bom_jesus:
                        simbolos += '{'
                        aberto_bom_jesus = True
                    else:
                        simbolos += '}'
                        aberto_bom_jesus = False
            else:
                teve_lembranca = True
                if aberto_lembranca:
                    simbolos += ']'
                    aberto_lembranca = False
                else:
                    simbolos += '['
                    aberto_lembranca = True
    if num_informacoes == 0:
        print("Ô cidadezinha morta, Josué. Ninguém abriu a boca pra dar um pio do teu pai. Dobra essa mesa que aqui a gente só gastou saliva à toa.")
    else:
        # verificar se ta balanceado
        pilha = ''
        balanceado = True
        processar_simbolos = True
        for simbolo in simbolos:
            if processar_simbolos:
                if simbolo in '({[':
                    pilha += simbolo  # empilhar
                else:
                    if not pilha:
                        balanceado = False
                        processar_simbolos = False
                    else:
                        # pegandor a parte de cima da pilha
                        topo = None
                        for ch in pilha:
                            topo = ch
                        # verificand
                        if (simbolo == ')' and topo != '(') or (simbolo == '}' and topo != '{') or (simbolo == ']' and topo != '['):
                            balanceado = False
                            processar_simbolos = False
                        else:
                            # desempilha
                            nova_pilha = ''
                            cont = 0
                            for char in pilha:
                                if cont < len(pilha) - 1:
                                    nova_pilha += char
                                cont += 1
                            pilha = nova_pilha
        if pilha != '':
            balanceado = False
        if balanceado and teve_identidade and teve_endereco and teve_lembranca:
            print("A história bateu, Josué. O povo falou a mesma coisa. Pega tuas coisas que a gente achou o caminho do teu pai.")
            encontrou = True
        else:
            if cidade != qtd_cidades:
                print("Essa conversa tá toda torta, um fala uma coisa, outro fala outra. Vamos embora, menino, a busca continua.")
    cidade += 1
if encontrou:
    print("------------------------------------------------------------")
    print("✅ Pistas confirmadas. Josué encontrou os irmãos e uma carta de seu pai.")
    print("A missão de Dora terminou. Pela janela do ônibus, ela escreve para o menino que deixou para trás:")
    print("✉️ Dora: 'Você tem razão. Seu pai ainda vai aparecer e, com certeza, ele é tudo aquilo que você diz que ele é.'")
    print("✉️ Dora: 'Quando você estiver cruzando as estradas no seu caminhão enorme, espero que você lembre que fui eu a primeira pessoa a te fazer botar a mão no volante.'")
    print("✉️ Dora: 'No dia que você quiser lembrar de mim, dá uma olhada no retratinho que a gente tirou junto... Tenho medo que um dia você também me esqueça. Tenho saudade de tudo.'")
else:
    print("Não achamos eles nessas cidades, Dona Dora... Mas amanhã a gente bota a mesinha de novo, né? O Brasil é grande, uma hora a gente encontra.")
