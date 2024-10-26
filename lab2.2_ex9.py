from datetime import datetime

data_actual = datetime.now()
dia_actual = data_actual.day
mes_actual = data_actual.month
ano_actual = data_actual.year

dia_nasc = int(input("Insira o seu dia de nascimento: "))
mes_nasc = int(input("Insira o seu mês de nascimento: "))
ano_nasc = int(input("Insira o seu ano de nascimento: "))

idade = ano_actual - ano_nasc

if (mes_actual < mes_nasc) or (mes_actual == mes_nasc and dia_actual < dia_nasc):
    idade -= 1

print(f"Você tem {idade} anos!")