N = float(input())
N = str(N)
Total = N.rsplit('.')

Real = int(Total[0])
auxR = 0
Moedas = int(Total[1])
auxM = 0

print("NOTAS:")

print("%d nota(s) de R$ 100.00" % (Real/100))
auxR = Real%100

print("%d nota(s) de R$ 50.00" % (auxR/50))
auxR = auxR%50

print("%d nota(s) de R$ 20.00" % (auxR/20))
auxR = auxR%20

print("%d nota(s) de R$ 10.00" % (auxR/10))
auxR = auxR%10

print("%d nota(s) de R$ 5.00" % (auxR/5))
auxR = auxR%5

print("%d nota(s) de R$ 2.00" % (auxR/2))
auxR = auxR%2

print("MOEDAS:")

print("%d moeda(s) de R$ 1.00" % (auxR/1))
auxR = auxR%1

print("%d moeda(s) de R$ 0.50" % (Moedas/50))
auxM = Moedas%50

print("%d moeda(s) de R$ 0.25" % (auxM/25))
auxM = auxM%25

print("%d moeda(s) de R$ 0.10" % (auxM/10))
auxM = auxM%10

print("%d moeda(s) de R$ 0.05" % (auxM/5))
auxM = auxM%5

print("%d moeda(s) de R$ 0.01" % (auxM/1))
auxM = auxM%1
