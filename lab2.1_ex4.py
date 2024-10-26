nome = input("Indique o nome (Alberto/Armanda)")
horas = input("Indique a que horas irá decorrer o evento (hh:mm)")
data = input("Indique em que data irá decorrer o evento (dd/mm/AAAA)")
comp = input("Qual o género do seu acompanhante? M/F")

if(nome == 'Alberto'):
    print(" " * 10, "Caro Alberto,")
    print(" " * 4, "Venho por este meio convidá-lo para a cerimónia a realizar pelas", horas, "do dia")
    print(data+". Caro Alberto, o código de vestimento é formal, o que significa que")
    print("deverá usar um fato com gravata.")
    print(" " * 4, "O dia", data, "é uma data muito especial para mim e contamos com a sua presença. O")
    if(comp == 'M' or comp == 'm'):
        print("convite é extensível ao seu companheiro.")
    else:
        print("convite é extensível à sua companheira.")
    print(" " * 4, "Aguardamos a sua confirmação")
    print(" " * 10, "O seu,")
    print(" " * 7, "-" * 20)
    print(" " * 10, "Arnaldo Antunes")
    
else:
    print(" " * 10, "Cara Armanda,")
    print(" " * 4, "Venho por este meio convidá-la para a cerimónia a realizar pelas", horas, "do dia")
    print(data+". Cara Armanda, o código de vestimento é formal, o que significa que")
    print("deverá usar um vestido e saltos altos.")
    print(" " * 4, "O dia", data, "é uma data muito especial para mim e contamos com a sua presença. O")
    if(comp == 'M' or comp == 'm'):
        print("convite é extensível ao seu companheiro.")
    else:
        print("convite é extensível à sua companheira.")
    print(" " * 4, "Aguardamos a sua confirmação")
    print(" " * 10, "O seu,")
    print(" " * 7, "-" * 20)
    print(" " * 10, "Arnaldo Antunes")
input()
