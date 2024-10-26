import decimal
menu = 15.00
iva = 0.23
gorgeta = 0.10

nrpessoas = float(input("Quantas pessoas vieram jantar?"))

totalMenu = nrpessoas * menu
print("Total S/IVA e S/Gorgeta: ", totalMenu)
totalIva = totalMenu * iva
totalGorgeta = totalMenu * gorgeta
total = totalMenu + totalIva + totalGorgeta

print("\nValor do IVA: ", totalIva)
print("\nValor da Gorgeta: ", totalGorgeta)
print("\nValor total: ", total)
input()


