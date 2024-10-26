ss = 0.115
irs = 0.25
sind = 0.05

salarioB = float(input("Qual o seu salário bruto? "))

ss *= salarioB
irs *= salarioB
sind *= salarioB

print("Valor da Segurança Social: ", ss)
print("Valor do IRS: ", irs)
print("Valor sindicato: ", sind)
salarioL = salarioB - (ss + irs + sind)
print("Salário líquido: ", salarioL)
input()