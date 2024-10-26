i = int(input("Valor de i: "))
match i:
    case 10:
        print("Preparar operação")
    case 5:
        print("Começar operação")
    case 0:
        print("Missão crítica")
    case _:
        print("Operação abortada")


nome = input("Nome? ")
if nome == 'Alberto' or nome == 'Armando':
    print("Bom rapaz")
elif nome == 'Arnaldo' or nome == 'Augusto':
    print("Hente estranha...")
else:
    print("Desconheço...")



nums = (1, 5, 10)
match (len(nums), isinstance(nums, tuple), nums[0]):
    case (3, True, 10):
        print(nums[1] + nums[2])
    case (3, True, 1):
        print(nums[1] * nums[2])
    case (3, True, _):
        print("Conjunto inválido")
    case _:
        print("Conjunto inválido")