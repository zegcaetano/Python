import sys
import shutil

if len(sys.argv) != 2:
    print("Utilização: python3", __file__, "caminho")
else:
    total, usado, livre = shutil.disk_usage(sys.argv[1])
    utilizacao = 100 * (usado/total)

    if utilizacao >= 80:
        print("Cheio")
    elif utilizacao >= 40:
        print("Ok")
    else:
        print("Vazio")

print("Fim")