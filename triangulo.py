# 6. [DESAFIO - não é obrigatório] Peça os três lados de uma figura. Primeiro, verifique se esses valores podem formar um triângulo.

# ⚠️Lembre-se: a soma de dois lados deve ser sempre maior que o terceiro.

# Se for possível formar um triângulo, classifique-o:

# Equilátero: todos os lados têm o mesmo tamanho.
# Isósceles: dois lados têm o mesmo tamanho.
# Escaleno: todos os lados são diferentes.

# Além disso, verifique se o triângulo é retângulo:

# ⚠️Um triângulo é retângulo quando o quadrado do maior lado é igual à soma dos quadrados dos outros dois lados.

# Caso os valores não formem um triângulo, informe isso ao usuário.

print("Digite dados para tentar formar um triângulo: ")

l1 = int(input("Digite a medida de um dos lados da figura: "))
l2 = int(input("Digite a medida de um dos lados da figura: "))
l3 = int(input("Digite a medida de um dos lados da figura: "))

lados = sorted([l1, l2, l3])
l1, l2, l3 = lados[2], lados[1], lados[0]

if l1 < l2 + l3: 
    
    if l1 == l2 == l3:
        tipo_lado = "equilátero"
    elif l2 == l3:
        tipo_lado = "isósceles"
    else:
        tipo_lado = "escaleno"
    
    if l1**2 == l2**2 + l3**2:
        tipo_angulo = " e retângulo"
    else:
        tipo_angulo = ""
    print(f"Triângulo {tipo_lado}{tipo_angulo}")
else:
    print("Os dados informados não podem formar um triângulo")