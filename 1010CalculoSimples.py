valores1 = str(input())
valores2 = str(input())
pecas1 = valores1.rsplit()
pecas2 = valores2.rsplit()
p1cod = int(pecas1[0])
p1qnt = int(pecas1[1])
p1preco = float(pecas1[2])
p2cod = int(pecas2[0])
p2qnt = int(pecas2[1])
p2preco = float(pecas2[2])

Valor = (p1qnt * p1preco) + (p2qnt * p2preco)

print("VALOR A PAGAR: R$ %.2f" % Valor)
