import pandas as pd
import openpyxl


class Exportar:
    def __init__(self, produto, preco, marca):
        self.produto = produto
        self.preco = preco
        self.marca = marca

    def del_xlsx(self):
        dados = pd.read_excel("Produtos.xlsx")
        df = pd.DataFrame(dados)
        df.drop()

    def criar_xlsx(self):
        d = {"Produto": [''], "Preço": [''], "Marca": ['']}
        dados = pd.DataFrame(data=d)
        dados.to_excel("Produtos.xlsx", index=False)

    def enviar_dados_xlsx(self):
        df = pd.read_excel("Produtos.xlsx")
        insert = [[self.produto, self.preco, self.marca]]
        novo = pd.DataFrame(data=insert, columns=['Produto', 'Preço', 'Marca'])

        final = pd.concat([df, novo], ignore_index=True)

        final.to_csv("Produtos.xlsx")

    def del_csv(self):
        dados = pd.read_csv("Produtos.csv")
        df = pd.DataFrame(dados)
        df.drop()

    def criar_csv(self):
        d = {"Produto": [''], "Preço": [''], "Marca": ['']}
        dados = pd.DataFrame(data=d)
        dados.to_csv("Produtos.csv", index=False)

    def enviar_dados_csv(self):
        df = pd.read_csv("Produtos.csv")
        insert = [[self.produto, self.preco, self.marca]]
        novo = pd.DataFrame(data=insert, columns=['Produto', 'Preço', 'Marca'])

        final = pd.concat([df, novo], ignore_index=True)

        final.to_csv("Produtos.xlsx")
