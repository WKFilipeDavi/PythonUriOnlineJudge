Entrada = input()
Numeros = Entrada.rsplit()


A = int(Numeros[0])
B = int(Numeros[1])
C = int(Numeros[2])
D = int(Numeros[3])

if B > C and D > A and C + D > A + B and C > 0 and D > 0 and A%2 == 0:
    print("Valores aceitos")

else:
    print("Valores nao aceitos")
