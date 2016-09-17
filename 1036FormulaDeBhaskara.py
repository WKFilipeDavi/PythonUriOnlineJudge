import math
Entrada = input()
Valores = Entrada.rsplit()

A = float(Valores[0])
B = float(Valores[1])
C = float(Valores[2])

Delta = float(((B**2) - (4*A*C)))

if Delta <= 0:
    print("Impossivel calcular")


elif A == 0:
    print("Impossivel calcular")

else:
    R1 = float(( -B + (math.sqrt(Delta)) ) / (2*A))
    R2 = float(( -B - (math.sqrt(Delta)) ) / (2*A))

    print("R1 = %.5f" % R1)

    print("R2 = %.5f" % R2)

