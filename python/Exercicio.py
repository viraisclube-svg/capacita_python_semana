def tipoDeTriangulo(angulo1, angulo2, angulo3):
    if( angulo1 + angulo2 + angulo3 == 180):

        if(angulo1 == angulo2 and angulo1 == angulo3 and angulo2 == angulo3):
            print("Triangulo Equilatero")
    
        elif(angulo1 == angulo2 or angulo1 == angulo3 or angulo2 == angulo3):
            print("Triangulo Isoceles")
    
        else:
            print("Triangulo Escaleno")
    
    else:
        print("não é um triangulo")




tipoDeTriangulo(60, 60, 60)