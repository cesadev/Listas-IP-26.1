###Inicio da Etapa 1
moedas_total = 0
#Print Inicial
print('Ô promessa sem jeito…')

print()

#Loop de coletar moedinhas
for _ in range(1,8):
    print(f'Dia {_}: Quantas moedas João Grilo conseguiu arrecadar hoje?')
    moedas = int(input())
    moedas_total += moedas
    print(f'No dia {_}, o baú já tem R$ {moedas_total}')

#Print
print()

print(f'Total arrecadado após o plano: R$ {moedas_total}')

print()

###Inicio da Etapa 2
if moedas_total == 0: 
    print("João Grilo não conseguiu arrecadar nada... direto para o plano B!!")
    sinal = 'não'

else: #Se arrecadou faz a oraçãozuda
    print("João Grilo começa a despedida da cachorra:")
    print("'Canis Mortus, Dinherus no Bolsus'")
    print("'Caro nostra quae in patina eius est, canis.'")
    
    print()
    #Pede sinal
    print('João Grilo, o padeiro acreditou?')
    sinal = input().lower()
    
    if sinal == 'sim':
        print("O padeiro acreditou! Chicó pode se casar com Rosinha!")
        print("Como o padeiro acreditou?")
    if sinal == 'não':
        print("O padeiro não acreditou... João Grilo parte para o Plano B!")

#def desculpas()
if sinal == 'não':
    print()
    print("Quantas desculpas João Grilo precisa inventar para o Padeiro?")
    print()

    quantia_desculpas = int(input())

    for _ in range(1,quantia_desculpas+1):
        print(f"Digite a {_}ª desculpa:")
        desculpa = input()
        print(f"João Grilo disse: '{desculpa}'... e o padeiro caiu na conversa!")

#final
print("Chicó: 'Não sei, só sei que foi assim!'")