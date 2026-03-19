caminho = input("Você deseja ir para a esquerda ou para a direita ? ").lower()
if caminho == "esquerda":
    print("Você encontrou um rio")
    caminho_rio = input("Você deseja atravessar o rio ou voltar ? ").lower()
    if caminho_rio == "atravessar":
        print("Você chegou a uma vila segura")
    else:
        print("Você permanece perdido na floresta")
else:
    print("Você encontrou uma montanha")
    caminho_montanha = input("Você deseja subir ou voltar ? ").lower()
    if caminho_montanha == "subir":
        print("Você encontrou um tesouro no topo")
    else:
        print("Você permanece perdido na floresta")