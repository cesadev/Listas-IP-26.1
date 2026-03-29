#Quais palavras aparecem na fofoca e quantas vezes elas surgem
#A safada da Sueli poe palavras proibida pra confundir os curiosos
#Terá N Rodadas

numero_rodadas = int(input())

print('Radar de Fofocas de Copacabana iniciado!')

for rodada_atual in range(1, numero_rodadas+1): #Loop das rodadas
    numero_fofocas = int(input())
    pontuacao = 15

    print(f"Rodada {rodada_atual}/{numero_rodadas}")
    print(f"Fofocas registradas: {numero_fofocas}")
    print("Pontuação inicial: 15")
    
    fofoca_total = ''
    for i in range(1, numero_fofocas+1): #Loop das N-fofocas
        fofoca = input()
        fofoca_total += fofoca + ' '

    palavra_proibida = input() #A safada da Sueli começa a agir
    
    continuar = True
    tentativa_total = '_'

    while continuar:
        tentativa = input()

        if tentativa.lower() == 'fim':
            print(f"Rodada encerrada! Pontuação final: {pontuacao}")
            continuar = False
            
        elif f"_{tentativa}_" in tentativa_total:
            print(f"Você já investigou '{tentativa}'. Tente outra.")
        
        else:
            tentativa_total += f"_{tentativa}_"

            if tentativa == palavra_proibida:
                print(f"Armadilha da Sueli! '{tentativa}' era proibida! -5 pontos")
                pontuacao -= 5
                print(f"Pontuação atual: {pontuacao}")

            else:
                ocorrencias = 0
                palavra_checagem = ''

                for letra in fofoca_total:
                    if letra != " ":
                        palavra_checagem += letra
                    else:
                        if palavra_checagem == tentativa:
                            ocorrencias += 1
                        palavra_checagem = ""
                
                if ocorrencias > 0 :
                    print(f"Investigação bem sucedida! '{tentativa}' apareceu {ocorrencias} vez(es).")
                    pontuacao += ocorrencias*2
                    print(f"Pontuação atual: {pontuacao}")

                else:
                    print(f"Nada encontrado sobre '{tentativa}'. -1 ponto")
                    pontuacao -= 1
                    print(f"Pontuação atual: {pontuacao}")
            
            if pontuacao <= 0:
                continuar = False
                print("Você ficou sem pontos! Sueli venceu essa rodada")

