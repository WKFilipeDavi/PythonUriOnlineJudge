Entrada = input()
Valores = Entrada.rsplit()

x = float(Valores[0])
y = float(Valores[1])


if x == y == 0:

    print("Origem")

if x == 0 != y:

    print("Eixo X")

elif x != 0 == y:

    print("Eixo Y")

if x > 0 < y:

    print("Q1")

if x < 0 < y:

    print("Q2")

if x < 0 > y:

    print("Q3")

if x > 0 > y:

    print("Q4")
