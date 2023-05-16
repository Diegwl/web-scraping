import tkinter.messagebox
from tkinter import ttk
from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from conectar import conexao, cursor
from read import listar_marcas, listar_produtos, search_products
from tkinter.messagebox import showinfo
import matplotlib.pyplot as plt

janela = Tk()


class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.inserts()
        self.lista()
        self.grafico()
        janela.mainloop()

    def tela(self):
        self.janela.title("MAGAZU")
        self.janela.configure(background="cyan")
        self.janela.geometry("700x800")
        self.janela.resizable(True, True)
        self.janela.minsize(width=700, height=700)

    def frames(self):
        self.frame0 = Frame(self.janela, bg="blue")
        self.frame0.place(relheight=0.07, relwidth=0.94, relx=0.03, rely=0.03)
        self.frame1 = Frame(self.janela, bg="blue")
        self.frame1.place(relheight=0.07, relwidth=0.94, relx=0.03, rely=0.115)
        self.frame2 = Frame(self.janela, bg="blue")
        self.frame2.place(relheight=0.25, relwidth=0.94, relx=0.03, rely=0.21)
        self.frame3 = Frame(self.janela, bg="blue")
        self.frame3.place(relheight=0.45, relwidth=0.94, relx=0.03, rely=0.475)

    def botoes(self):
        self.btBuscarAll = Button(self.frame0, text='Ler', bg="cyan", command=self.ler_produtos)
        self.btBuscarAll.place(relx=0.58, rely=0.15, relwidth=0.1, relheight=0.70)

        self.btBuscar = Button(self.frame0, text='Buscar', bg="cyan", command=self.procurar_produtos)
        self.btBuscar.place(relx=0.69, rely=0.15, relwidth=0.1, relheight=0.70)

        self.btClear = Button(self.frame0, text='Limpar', bg="cyan", command=self.limpar)
        self.btClear.place(relx=0.80, rely=0.15, relwidth=0.1, relheight=0.70)

        self.btExportar = Button(self.frame1, text='Exportar', bg="cyan", command=self.limpar)
        self.btExportar.place(relx=0.80, rely=0.15, relwidth=0.1, relheight=0.70)

        self.btWeb = Button(self.frame1, text='Web Scraping', bg="cyan", command=self.WebScraping)
        self.btWeb.place(relx=0.80, rely=0.15, relwidth=0.1, relheight=0.70)

    def labels(self):
        self.lbMarca = Label(self.frame0, text="Marcas:", background="cyan")
        self.lbMarca.place(relx=0.05, rely=0.03, relwidth=0.4, relheight=0.20)

        self.lbFormato = Label(self.frame1, text="Formato de Arquivo:", bg="cyan")
        self.lbFormato.place(relx=0.05, rely=0.03, relwidth=0.4, relheight=0.20)

    def inserts(self):
        self.marcas = ["Macbooks", "Notebook Acer", "Notebook Dell", "Notebook Lenovo", "Notebook Samsung"]

        self.clicked = StringVar()

        self.clicked.set("")

        self.drop_marcas = OptionMenu(self.frame0, self.clicked, *self.marcas)
        self.drop_marcas.pack()
        self.drop_marcas.place(relx=0.05, rely=0.30, relwidth=0.4, relheight=0.60)

        self.formatos = [".xlsx", ".csv"]

        self.clicked2 = StringVar()

        self.clicked2.set("")

        self.drop_formatos = OptionMenu(self.frame1, self.clicked2, *self.formatos)
        self.drop_formatos.pack()
        self.drop_formatos.place(relx=0.05, rely=0.30, relwidth=0.4, relheight=0.60)




    def lista(self):
        self.listaCli = ttk.Treeview(self.frame2, height=3, columns=("col1", "col2", "col3", "col4"))

        self.listaCli.heading('#0', text='ID')
        self.listaCli.heading('#1', text='Modelo')
        self.listaCli.heading('#2', text='Preço')
        self.listaCli.heading('#3', text='Marca')

        self.listaCli.column('#0', width=50)
        self.listaCli.column('#1', width=200)
        self.listaCli.column('#2', width=70)
        self.listaCli.column('#3', width=70)

        self.listaCli.place(relx=0.025, rely=0.075, relwidth=0.925, relheight=0.85)

        self.scrollLista = Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.949, rely=0.079, relwidth=0.02, relheight=0.84)
        self.scrollLista.config(command=self.listaCli.yview)

    def delete_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())

    def procurar_produtos(self):
        self.delete_lista()
        linhas = search_products(self.clicked.get())
        for i in range(len(linhas)):
            self.listaCli.insert(index=i, values=[linhas[i][1], linhas[i][2], linhas[i][3]], parent="", text=linhas[i][0])

    def ler_produtos(self):
        self.delete_lista()
        linhas = listar_produtos()
        for i in range(len(linhas)):
            self.listaCli.insert(index=i, values=[linhas[i][1], linhas[i][2], linhas[i][3]], parent="", text=linhas[i][0])

    def limpar(self):
        self.delete_lista()

    def grafico(self):
        pass
        """
        fig = plt.Figure(figsize=(12, 6), dpi=50)
        ax = fig.add_subplot(111)

        numeros = [n for n in range(1, 61)]

        counts = []

        sql = f"SELECT * from jogos"
        cursor.execute(sql)
        linhas = cursor.fetchall()
        for i in range(1, 61):
            cont = 0
            for linha in linhas:
                for j in range(1, 7):
                    if linha[j] == i:
                        cont += 1
            counts.append(cont)

        ax.bar(numeros, counts)

        ax.set_ylabel('Vezes que foi sorteado')
        ax.set_title('Número de vezes que cada número foi sorteado')

        canva = FigureCanvasTkAgg(fig, self.janela)
        canva.get_tk_widget().place(relx=0.05, rely=0.50)
        """

