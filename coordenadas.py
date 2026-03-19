x = int(input("Digite uma coordenada para o eixo X: "))
y = int(input("Digite uma coordenada para o eixo Y: "))

if x >= 0 and x <= 10 and y >= 0 and y <= 10:
    if x == 0 or x == 10 or y == 0 or y == 10:
        print ("Na fronteira")
    else:
        print("Dentro do quadrado")
else:
    print("Fora dos limites")