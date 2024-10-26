print("1/P - Pesquisar ocorrência")
print("2/N - Adicionar ocorrência")
print("3/A - Actualizar BD de ocorrências")
print("0/T - Terminar")
opcao = input("Opção: ");
"""if opcao == '1' or opcao == 'P':
    print("Introduza os dados para pesquisa...")
elif opcao == '2' or opcao == 'N':
    print("Introduza os dados do novo registo...")
elif opcao == '3' or opcao == 'A':
    print("Vamos agora actualizar a BD...")
elif opcao == '0' or opcao == 'T':
    print("Programa vai terminar")
else:
    print("ERRO: Opção {opcao} inválida")"""

match opcao:
    case '1' | 'P':
        print("Introduza os dados para pesquisa...")
    case '2' | 'N':
        print("Introduza os dados do novo registo...")
    case '3' | 'A':
        print("Vamos agora actualizar a BD...")
    case '0' | 'T':
        print("Programa vai terminar")
    case _:
        print("ERRO: Opção {opcao} inválida")