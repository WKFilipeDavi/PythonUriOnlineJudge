Entrada = input()
Numeros = Entrada.split()
A = int(Numeros[0])
B = int(Numeros[1])
C = int(Numeros[2])
MaiorAB = ((A+B)+abs(A-B))/2
Maior = ((MaiorAB + C)+ abs(MaiorAB - C))/2

print("%d eh o maior" % Maior)
