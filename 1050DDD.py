DDD = int(input())
Verif = False
a = 0

mapa = {61 : "Brasilia",
        71 : "Salvador",
        11 : "Sao Paulo",
        21 : "Rio de Janeiro",
        32 : "Juiz de Fora",
        19 : "Campinas",
        27 : "Vitoria",
        31 : "Belo Horizonte"}

lista = [61,71,11,21,32,19,27,31]

for i in lista:
    if lista[a] == DDD:
        print(mapa[DDD])
        break

    elif a <= len(lista):
        a = a + 1

    if a == len(lista):
        print("DDD nao cadastrado")


        
