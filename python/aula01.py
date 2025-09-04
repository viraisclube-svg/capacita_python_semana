

def votação(idade):

    if(idade >= 16 & idade < 69):
        
        if(idade <= 18):
            print("voto opcional")

        elif(idade >= 18):
            print("precisa votar")
    
    elif(idade >= 70):
        print("não precisa votar")
    
    else:
        print("não pode votar")
    


usuario = int(input("digite a idade"))
votação(usuario)
