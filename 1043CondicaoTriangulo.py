Entrada = input()
Valores = Entrada.rsplit()

A = abs(float(Valores[0]))
B = abs(float(Valores[1]))
C = abs(float(Valores[2]))


if abs(B - C) < A < B + C:
    P = A + B + C
    print("Perimetro = %.1f" % P)


elif abs(A - C) < B < A + C:
    P = A + B + C
    print("Perimetro = %.1f" % P)


elif abs(A - B) < C < A + B:
    P = A + B + C
    print("Perimetro = %.1f" % P)


else:
    A = ((A + B)* C) / 2
    print("Area = %.1f" % A)
