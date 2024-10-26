nomes = ['Alberto' , 'António', 'Armando', 'Arnaldo']
print(nomes[0], nomes[len(nomes) -1], nomes[-len(nomes)], nomes[-1])
print(nomes[-1:])
print('António' in nomes)
print(nomes[1:])
nomes[0] = 'Alberta'
print(nomes)
nomes[1:3] = ['Antónia', 'Armanda']
print(nomes)
nomes[-1] = "Arnalda"
print(nomes[-1:])
nomes[-1:] = [nomes[-1], 'Andreia']
print(nomes)
nomes2 = nomes + ['Anabela', 'Arlete']
nomes2 += ['Ana']
print(nomes, nomes2)
nomes.append("Anabela")
print(nomes)
nomes.extend(["Arlete", "Ana"])
print(nomes)
nomes[1:3] = []
print(nomes)
nomes.pop(1)
print(nomes)
nomes[:] = []
print(nomes)
nums_repetidos = [4.2] * 10
print(nums_repetidos)
txt_repetido = ['A'*3] * 6
print(txt_repetido)
print(type([1, 2, 3]))
print(list("ABC"))

vogais = ('a', 'e', 'i', 'o', 'u')
print(vogais[0])
print(vogais[-1])
print(vogais[1:3])
vogais = 'a', 'e', 'i', 'o', 'u'
print(vogais)
valores = (10, 20, 30)

#string
pessoas = ('Alberto')
#tuple
pessoas = ('Alberto',)
#list
pessoas = ['Alberto']
listas = ([10, 20, 30], [100, 200, 300])
#listas[0] = [1,2,3]
listas[0][0] = 700
print(listas)
portos = {'ftp': 21, 'ssh': 22, 'smtp': 25, 'http': 80}
print(portos)
print(len(portos))
print(portos.get('sssh', -1))
print(portos.get('http'))
print(portos.keys())
print(portos.values())
print(portos.items())
print('ftp' in portos, 25 in portos.values())
portos.update({'ftp': 19, 'https': 443})
print(portos)
portos['ftp']=21
#portos['pop3']
portos['pop3'] = 110
print(portos)
del portos['smtp']
print(portos)
idades1 = dict(alberto=20, armando=27, antónio=19)
idades2 = dict([['alberto', 20], ['armando', 27], ['antónio', 19]])
print(idades1, idades2)
print(idades1 == idades2, idades1 is idades2)
x = 3
print(3 is x)

