Entrada = float(input())


if Entrada <= 2000.00:
    print("Isento")

else:
    Resto1 = float(Entrada - 2000.00)

    if Resto1 + 2000.00 <= 3000.00:
        Porc8 = float((Resto1 * 8) / 100)
        print("R$ %.2f" % Porc8)

    elif Resto1 + 2000.00 > 3000.00:
        Porc8 = float((1000 * 8) / 100)
        Resto2 = Resto1 - 1000

        if Resto2 + 3000.00 <= 4500.00:
            Porc18 = (Resto2 * 18) / 100
            Total = float(Porc8 + Porc18)
            print("R$ %.2f" % Total)


        else:
            Porc18 = (1500 * 18) / 100
            Resto3 = Resto2 - 1500
            Porc28 = (Resto3 * 28) / 100
            Total = float(Porc8 + Porc18 + Porc28)
            print("R$ %.2f" % Total)


