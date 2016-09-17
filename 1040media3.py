Entrada = input()
Valores = Entrada.rsplit()

N1 = float(Valores[0])
N2 = float(Valores[1])
N3 = float(Valores[2])
N4 = float(Valores[3])

Media = float( ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / (2 + 3 + 4 + 1) )

if Media >= 7.0:
    print("Media: %.1f" % Media)
    
    print("Aluno aprovado.")

elif Media < 5.0:
    print("Media: %.1f" % Media)
    
    print("Aluno reprovado.")


else:
    print("Media: %.1f" % Media)

    print("Aluno em exame.")

    NotaExame = float(input())

    print("Nota do exame: %.1f" % NotaExame)

    MediaFinal = (NotaExame + Media) / 2
    if MediaFinal >= 5.0:
        print("Aluno aprovado.")
        print("Media final: %.1f" % MediaFinal)

    else:
        print("Aluno reprovado.")
        print("Media final: %.1f" % MediaFinal)

    
