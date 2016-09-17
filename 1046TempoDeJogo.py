Entrada = input()
Valores = Entrada.rsplit()

A = int(Valores[0])
B = int(Valores[1])

if A > B:
    Tempo = abs(A - (B + 24))
    print("O JOGO DUROU %d HORA(S)" % Tempo)

elif A < B:
    Tempo = abs(A - B)
    print("O JOGO DUROU %d HORA(S)" % Tempo)

else:
    Tempo = 24
    print("O JOGO DUROU %d HORA(S)" % Tempo)
