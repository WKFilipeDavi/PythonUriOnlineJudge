Num = input()
Valores = Num.split()
A = float(Valores[0])
B = float(Valores[1])
C = float(Valores[2])
pi = 3.14159
TRIANGULO = (A*C)/2
CIRCULO = pi * (C**2)
TRAPEZIO = ((A + B)* C)/2
QUADRADO = B * B
RETANGULO = A*B

print("TRIANGULO: %.3f" % TRIANGULO)
print("CIRCULO: %.3f" % CIRCULO)
print("TRAPEZIO: %.3f" % TRAPEZIO)
print("QUADRADO: %.3f" % QUADRADO)
print("RETANGULO: %.3f" % RETANGULO)
