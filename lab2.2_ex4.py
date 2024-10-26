
#a)
p = 2.3
print("{:f}".format(p))
print(p*2, '\n')
print("{0}{1}".format(p*2, "\n"[0]))

#b)
v1 = [0]*4
i = 0

v1[i] = 7; i += 1; v1[i] = 14; v1[len(v1) - 1] = 15
print(v1[i]*v1[i+1] + v1[1])

#v1 = [7, 14, 0, 15]

#c)
x=3,5/2
print(x)

#d)
codigo = {'A':19, 'B':20}
print(list(codigo))

#e)
codigo = {'A':19, 'B':20}
print(codigo['B'], codigo.get('C'), codigo.get('C',21))

#f)
codigo = {'A':19, 'B':20}
d = dict(a=list(codigo.values())[0], b=list(codigo.values())[-1])
print(d)

#g)
processos = {'ls':192, 'grep':321, 'init':1}
print('ls' in processos, 321 in processos)
print((192 in processos)*2)
processos.update(ls=292, mkfs=19)
print(list(processos.items()))

#h)
txt = ''
nums = [10, 11]
if nums:
    print("Um")
    if not txt:
        print("Dois")
        txt = 'abc'
        nums = []
    else:
        print("Três")
        txt = 'xey'
        nums[-1:] = [12]
txt = txt.replace('a', '').replace('e', '')
print("Quatro" if len(nums) else "Cinco")
print(txt if len(nums) == 0 else nums)