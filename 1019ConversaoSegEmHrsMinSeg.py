N = int(input())

Horas = N/3600
Horas = int(Horas)

Minutos = (N - (Horas * 3600)) / 60
Minutos = int(Minutos)

Segundos = (N-(Horas*3600)-(Minutos*60))

Segundos = int(Segundos)

print("%d:%d:%d" % (Horas, Minutos, Segundos))
