print("1 - Pesquisar ocorrência")
print("2 - Adicionar ocorrência")
print("3 - Actualizar BD de ocorrências")
print("0 - Terminar")
opcao = input("Opção: ");
"""
if opcao == '1':
    print("Introduza os dados para pesquisa...")
elif opcao == '2':
    print("Introduza os dados do novo registo...")
elif opcao == '3':
    print("Vamos agora actualizar a BD...")
elif opcao == '0':
    print("Programa vai terminar")
else:
    print("ERRO: Opção {opcao} inválida")"""



match opcao:
    case '1':
        print("Introduza os dados para pesquisa...")
    case '2':
        print("Introduza os dados do novo registo...")
    case '3':
        print("Vamos agora actualizar a BD...")
    case '0':
        print("Programa vai terminar")
    case _:
        print("ERRO: Opção {opcao} inválida")