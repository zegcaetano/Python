horas = float(input("Quantas horas passaram?"))
minutos = float(input("Quantos minutos passaram?"))
segundos = float(input("Quantos segundos passaram?"))

minutos *= 60
horas *= 3600

total = minutos + horas + segundos


print("O total de segundos passados é: ", total)
input()