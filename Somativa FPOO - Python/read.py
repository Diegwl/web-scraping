from conectar import conexao, cursor

def listar_marcas():
    sql = "SELECT marca from produtos"
    cursor.execute(sql)
    marcas = []
    linhas = cursor.fetchall()
    for linha in linhas:
        if linha not in marcas:
            marcas.append(linha)
    return marcas


def listar_produtos():
    sql = 'SELECT * from produtos'
    cursor.execute(sql)
    linhas = cursor.fetchall()
    return linhas


def search_products(marca):
    sql = f'SELECT * from produtos where marca = "{marca}"'
    cursor.execute(sql)
    linhas = cursor.fetchall()
    print(linhas)
    return linhas