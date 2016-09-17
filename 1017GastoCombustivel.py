LitPkm = 12
TempoViagem = int(input())
VelMedia = int(input())

LitrosGastos = ((VelMedia * TempoViagem) / LitPkm)

print("%.3f" % LitrosGastos)
