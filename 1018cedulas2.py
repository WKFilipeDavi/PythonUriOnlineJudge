N = int(input())
aux = 0

print(N)

print("%d nota(s) de R$ 100,00" % (N/100))
aux = N%100

print("%d nota(s) de R$ 50,00" % (aux/50))
aux = aux%50

print("%d nota(s) de R$ 20,00" % (aux/20))
aux = aux%20

print("%d nota(s) de R$ 10,00" % (aux/10))
aux = aux%10

print("%d nota(s) de R$ 5,00" % (aux/5))
aux = aux%5

print("%d nota(s) de R$ 2,00" % (aux/2))
aux = aux%2

print("%d nota(s) de R$ 1,00" % (aux/1))
