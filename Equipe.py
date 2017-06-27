from Alunoo import aluno
#coding: utf-8
class aluno:
    def __init__(self):
        pass

    def menuPrincipal(self):
        listaA = []
        listaB = []
        while True:
            op = raw_input("Opcao do aluno: 1 Adicionar / 2 Remover / 3 Mostrar Lista :")
            if op == "1":
                Nome = raw_input("Informe seu Nome: ")
                Cpf = raw_input("Informe seu CPF: ")
                listaA.append(Nome)
                listaB.append(Cpf)
                print(listaA)
                continue
            elif op == "2":
                Remove = raw_input("Informe o Nome do aluno que deseja remover: ")
                for x in listaA:
                    if x == Remove:
                        listaA.remove(x)
                Remove1 = raw_input("Informe o CPF que deseja remover: ")
                for y in listaA:
                    if y == Remove1:
                        listaB.remove(y)

            elif op == "3":
                print(listaA)
                print(listaB)
            else:
                print("Opcao invalida.")
                continue

resultado=aluno()
resultado.menuPrincipal()


