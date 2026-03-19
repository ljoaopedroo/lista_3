usuario = input("Digite seu usuário: ").lower()
senha = (input("Digite sua senha: "))

if usuario == "admin" and senha == "1234":
    print("Acesso liberado")
elif usuario == "convidado" and senha == "":
    print("Acesso restrito")
else:
    print("Bloqueado")