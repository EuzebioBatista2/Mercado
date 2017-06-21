#coding: utf-8
from produto import produto1
class cadastro1:

    def cadastroP(self,listacadas):

        print("\n= = = = Cadastro de Produtos= = = =")
        while True:
            nome=raw_input("\nDigite o nome do produto: ")
            preco= float(raw_input("Digite o preço unitário do produto: "))
            tipo= raw_input("Digite o tipo do produto: ")
            estoque= int(raw_input("Digite a quantidade no estoque: "))
            prod = produto(nome,preco,tipo,estoque)
            listaProdutos.append(prod)

            print "\n%d %s(s) cadastrado(s) com sucesso.\n"%(estoque,nome.title())

            sair= raw_input("Deseja cadastrar outro produto? ")
            if sair.upper()=="NAO":
                break
            while sair.upper() not in ("NAO", "SIM"):
                print "\nValor inválido!"
                sair=raw_input("\nDigite 'nao' para sair e 'sim' para continuar: ")
class vender:
    def __init__(self):
        pass
    def vendendo(self,listavend):
        global total_caixa
        print("\n= = = = Venda de Produtos= = = =")
        existe= False
        while True:
            nome= raw_input("\nDigite o nome do Produto: ")
            for i in range(len(listaProdutos)):
                if listaProdutos[i].getNome()== nome:
                    existe= True
                    print "==> %s (%s). R$ %.2f" % (listaProdutos[i].getNome().title(), listaProdutos[i].getTipo().title(), listaProdutos[i].getPreco())
                    qtd_produto = int(raw_input("Digite a quantidade que deseja vender: "))
                    if qtd_produto < listaProdutos[i].getEstoque():
                        listaProdutos[i].setEstoque(listaProdutos[i].getEstoque()-qtd_produto)
                        total_caixa += qtd_produto * listaProdutos[i].getPreco()
                        print "==> Total arrecadado: R$ %.2f"%(qtd_produto*listaProdutos[i].getPreco())
                        break
                    else:
                        print "Não é possível vender pois não há %s suficiente."%listaProdutos[i].getNome()
                if existe==False and i+1== len(listaProdutos):
                    print "%s nao cadastrado no sistema"%nome.title()
                    break

            sair = raw_input("\nDeseja vender outro produto? ")
            if sair.upper() == "NAO":
                break
            while sair.upper() not in ("NAO", "SIM"):
                print "\nValor inválido!"
                sair = raw_input("\nDigite 'nao' para sair e 'sim' para continuar: ")

class balanco:
    def __init__(self):
        pass
    def imprimirBalanco(self,listabala):
        total_previsto=0.0
        print ("\n= = = = Impressão de Balanço = = = =\n")
        print "Produtos cadastrados:\n"
        for i in range(len(listaProdutos)):
            print "%d) %s(%s). R$ %.2f"%(i+1,listaProdutos[i].getNome().title(), listaProdutos[i].getTipo().title(),listaProdutos[i].getPreco())
            print("\tRestante: %d\n")%listaProdutos[i].getEstoque()
            total_previsto+= listaProdutos[i].getPreco() * listaProdutos[i].getEstoque()
        print "Total arrecardado em vendas: R$ %.2f"%total_caixa
        print "\nTotal que pode ser arrecardado: R$ %.2f"%total_previsto