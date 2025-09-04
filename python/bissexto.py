def anoBissexto(ano):
    if(ano % 4 == 0):
        print("É ano bissexto")
    
    elif(ano % 4 != 0):
        print("Não é bissexto")


meuAno = int(input("Digite um ano: "))
anoBissexto(meuAno)