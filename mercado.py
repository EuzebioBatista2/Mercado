#coding: utf-8
from estoque import cadastro1,vender,balanco
opcao=0
nome=""
preco=0
tipo=""
estoque=""
total_caixa=0.0
class economizatec:

    def menuPrincipal(self):
        cadastra = cadastro1()
        venda = vender()
        qtd_vendida = balanco()
        self.listaProdutos = []

        while True:
            print("\n= = = = Bem-vindo(a) ao EconomizaTec= = = =\n")
            print("Digite a opção desejada\n")
            print("1. Cadastrar um Produto")
            print("2. Vender um Produto")
            print("3. Imprimir Balanço")
            print("4. Sair")
            opcao = raw_input("\nOpção: ")

            if opcao == "1":
                self.listaProdutos = cadastra.cadastroP(self.listaProdutos)
            elif opcao=="2":
                self.listaProdutos = vender.vendendo(self.listaProdutos)
            elif opcao=="3":
                self.listaProdutos = qtd_vendida.imprimirBalanco(self.listaProdutos)
            elif opcao == "4":
                print "\nFim de caixa."
                return "sair"

resultado=economizatec()
resultado.menuPrincipal()