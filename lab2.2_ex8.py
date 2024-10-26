bissexto = False
ano = int(input(print("Será que o ano é bissexto? Introduza um ano: ")))

if ano % 4 == 0:
    bissexto = True
if ano % 4 == 0 and ano % 100 == 0:
    if ano % 400 == 0:
        bissexto = True
    else:
        bissexto = False


if bissexto == True:
    print("O ano é bissexto!")
else:
    print("O ano não é bissexto")