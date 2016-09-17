Salario = float(input())

if 0 <= Salario <= 400.00:
    Reajuste = 15
    SalarioFinal = Salario * (1 + 0.15)
    ReajGanho = SalarioFinal - Salario
    Simbolo = "%"

    print("Novo salario: %.2f" % SalarioFinal)
    print("Reajuste ganho: %.2f" % ReajGanho)
    print("Em percentual: %d %s" % (Reajuste, Simbolo))


elif 400.01 <= Salario <= 800.00:
    Reajuste = 12
    SalarioFinal = Salario * (1 + 0.12)
    ReajGanho = SalarioFinal - Salario
    Simbolo = "%"

    print("Novo salario: %.2f" % SalarioFinal)
    print("Reajuste ganho: %.2f" % ReajGanho)
    print("Em percentual: %d %s" % (Reajuste, Simbolo))


elif 800.01 <= Salario <= 1200.00:
    Reajuste = 10
    SalarioFinal = Salario * (1 + 0.10)
    ReajGanho = SalarioFinal - Salario
    Simbolo = "%"

    print("Novo salario: %.2f" % SalarioFinal)
    print("Reajuste ganho: %.2f" % ReajGanho)
    print("Em percentual: %d %s" % (Reajuste, Simbolo))

elif 1200.01 <= Salario <= 2000.00:
    Reajuste = 7
    SalarioFinal = Salario * (1 + 0.07)
    ReajGanho = SalarioFinal - Salario
    Simbolo = "%"

    print("Novo salario: %.2f" % SalarioFinal)
    print("Reajuste ganho: %.2f" % ReajGanho)
    print("Em percentual: %d %s" % (Reajuste, Simbolo))

elif Salario > 2000.00:
    Reajuste = 4
    SalarioFinal = Salario * (1 + 0.04)
    ReajGanho = SalarioFinal - Salario
    Simbolo = "%"

    print("Novo salario: %.2f" % SalarioFinal)
    print("Reajuste ganho: %.2f" % ReajGanho)
    print("Em percentual: %d %s" % (Reajuste, Simbolo))
    
    
