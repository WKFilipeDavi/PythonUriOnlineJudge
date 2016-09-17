import math

valores1 = input()
valores2 = input()

p1 = valores1.split()
p2 = valores2.split()

x1 = float(p1[0])
y1 = float(p1[1])
x2 = float(p2[0])
y2 = float(p2[1])

Distancia = math.sqrt( ((x2 - x1)**2) + ((y2 - y1)**2) )

print("%.4f" % Distancia)
