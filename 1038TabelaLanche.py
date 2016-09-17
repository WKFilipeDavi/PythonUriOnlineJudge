PriceTable = { 1 : 4.00,
               2 : 4.50,
               3 : 5.00,
               4 : 2.00,
               5 : 1.50}

Entrada = input()
Valores = Entrada.rsplit()

Cod = int(Valores[0])
Qnt = int(Valores[1])

Total = float(PriceTable[Cod]*Qnt)

print("Total: R$ %.2f" % Total)
