dinheiro_inicial = int(input())
qtd_compras = 0
custo_total = 0
continuar = True

print(f'A família possui {dinheiro_inicial} ainda, talvez ele fique tranquilo hoje')

while continuar == True:
    compra = input()

    if compra == 'Amauri':
        print('Sabia que vocês estão loucos, hora de encerrar essa loucura!')
        continuar = False

    else:
        custo = int(input())

        if dinheiro_inicial == 0 or custo>dinheiro_inicial:
            print('Enlouqueceram? Vocês estão falidos')
            continuar = False
        else:
            if custo > 500000:
                print(f'Enlouqueceram de vez {custo} reais num(a) {compra}')
            elif custo < 1000:
                print(f'Será que se acalmaram?! {compra} por "somente" {custo} reais')
            else:
                print(f'Gastaram {custo} reais para comprar um(a) {compra}')

            if compra == "carro":
                modelo = input()

                if modelo == 'chevette':
                    print('chevette : Relembrando as origens será?')
                elif modelo == 'jeep':
                    print('jeep : Será que ele tá se preparando para outra aventura que não irá?')
                elif modelo == 'bmw':
                    print('bmw : Já to vendo o facebook dele cheio de foto me marcando 🙁')
                        
            dinheiro_inicial-= custo
            qtd_compras+=1
            custo_total += custo

            if dinheiro_inicial == 0:
                print('Enlouqueceram? Vocês estão falidos')
                continuar = False
                
            
print(f'{qtd_compras} - {custo_total} reais')