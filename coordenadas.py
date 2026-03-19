x = int(input("Digite uma coordenada para o eixo X: "))
y = int(input("Digite uma coordenada para o eixo Y: "))

if (x and y) >= 0 and (x and y) <= 10:
    if (x or y ) == 0 or (x or y) == 10:
        print ("Na fronteira")
    else:
        print("Dentro do quadrado")
else:
    print("Fora dos limites")