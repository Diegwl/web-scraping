from conectar import conexao, cursor


def inserir_produtos(id, produto, preco, marca):
    produtos = f"""INSERT INTO produtos(id, produto, preco, marca)
    values
    ({int(id)}, '{produto}', '{preco}', '{marca}');"""
    cursor.execute(produtos)
    conexao.commit()


def deletar_produtos():
    sql = """Delete from produtos"""
    cursor.execute(sql)
    conexao.commit()