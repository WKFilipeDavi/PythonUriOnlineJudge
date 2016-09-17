Entrada = input()
Valores = Entrada.rsplit()

H1 = int(Valores[0])
M1 = int(Valores[1])

H2 = int(Valores[2])
M2 = int(Valores[3])


if M1 < M2:
    Minutos = M2 - M1

    if H1 < H2:
      Horas = H2 - H1

      
    elif H1 > H2:
       Horas = abs(H2 - (H1 + 24))

    else:
       Horas = 24


    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (Horas,Minutos))
    

elif M1 > M2:
    Minutos = abs(M1 - (M2 + 60))
    H2 = H2 - 1

    if H1 < H2:
      Horas = H2 - H1

      
    elif H1 > H2:
       Horas = abs(H2 - (H1 + 24))

    else:
       Horas = 0

    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (Horas,Minutos))


else:
    Minutos = 0

    if H1 < H2:
      Horas = H2 - H1

      
    elif H1 > H2:
       Horas = abs(H2 - (H1 + 24))

    else:
       Horas = 24

    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (Horas,Minutos))

    

