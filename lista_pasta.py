import os


nome_pasta = input("Indique o caminho da pasta: ")
conteudo = os.listdir(nome_pasta)
if conteudo:
    print(conteudo)
else:
    print("A pasta", nome_pasta, "está vazia!")
print("Fim")