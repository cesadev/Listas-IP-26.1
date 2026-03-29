quantia_pendrives = int(input())
pendrives_abertos = 0

print("Avenida Brasil: A Vingança de Nina!")
for pendrive_atual in range(1,quantia_pendrives+1):

    quantia_caracteres_senha = 0 #começa em 0 em todo loop

    senha_secreta = input()
    senha_criptografada = ''
    
    #Criação da Senha Criptografada
    for i in senha_secreta:
        if i == " ":
            senha_criptografada += i
        else:
            senha_criptografada += "_"

    #Calculando caracteres da senha sem o espaço
    for i in senha_secreta:
        if i != ' ':
            quantia_caracteres_senha += 1

    quantia_tentativas = quantia_caracteres_senha*2 #Multiplica por 2 a quantia de caracteres


    #Tentativas
    print(f"Descriptografando pendrive {pendrive_atual} de {quantia_pendrives}...")

    continuar = True
    chutes = ''

    while continuar == True:
        tentativa = input()
        quantia_tentativas -= 1 #Retira uma tentativazuda

        if tentativa not in chutes: #Se for inédita
            chutes += tentativa #chutes recebe a tentativa

            if tentativa in senha_secreta: #Se for inédita e estiver na senha
                print("Nina: Boa, Tufão! Menos uma mentira da Carminha.")

            #Fazer Forca
                senha_criptografada = '' #Reseta o estado atual da senha
                
                for letra in senha_secreta: #para cada kletra da senha
                    if letra in chutes: #se a letra estiver nas tentativaas
                        senha_criptografada += letra #Senha criptografada receberá ela

                    elif letra == " ":
                        senha_criptografada += " "

                    else: #Se não, receberá o simbolo criptografado
                        senha_criptografada += '_'

            else: #Se for inédita e não estiver na senha
                print("Carminha: Você é um idiota, Tufão! Isso não faz sentido.")

        else: #Se não for inédita (estando ou não na senha)
            print("Max: Ele já tentou isso, Carminha...")

        print(f"Senha: {senha_criptografada}") #Estado atual da senha

        #Se descobrir, tufao printa algo
        if senha_secreta == senha_criptografada:
            print(f"Tufão: Agora eu sei de toda a verdade! O pendrive {pendrive_atual} está aberto.")
            pendrives_abertos += 1
            continuar = False

        #Encerrar as tentativas
        if quantia_tentativas == 0:
            print(f"Carminha: Consegui! As fotos do pendrive {pendrive_atual} estão a salvo comigo.")
            continuar = False


print(f'Conseguimos abrir {pendrives_abertos} de {quantia_pendrives} pendrives!')

taxa_acertos = (pendrives_abertos * 100)/quantia_pendrives

if taxa_acertos == 0:
    print("Tufão continuará sendo enganado para sempre...")
elif 0<taxa_acertos<=50:
    print("Tufão descobriu algumas coisas, mas Carminha ainda tem poder.")
elif 50<taxa_acertos<100:
    print("A casa caiu para a Carminha! Quase todas as provas foram recuperadas.")
else:
    print("Justiça por Rita! Todas as provas estão nas mãos de Tufão.")


    