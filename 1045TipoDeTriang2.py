Entrada = input()
Valores = Entrada.rsplit()


A = float(Valores[0])
B = float(Valores[1])
C = float(Valores[2])

if A < B:
    D = A
    A = B
    B = D

if A < C:
    D = A
    A = C
    C = D

if B < C:
    D = B
    B = C
    C = D

if A >= B+C:
    print("NAO FORMA TRIANGULO")


elif A**2 == (B**2) + (C**2):
    print("TRIANGULO RETANGULO")


elif A**2 > (B**2) + (C**2):
    print("TRIANGULO OBTUSANGULO")


elif A**2 < (B**2) + (C**2):
    print("TRIANGULO ACUTANGULO")



if A == B and A == C:
    print("TRIANGULO EQUILATERO")


else:
    if A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")
