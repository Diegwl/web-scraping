from conectar import conexao, cursor


def create_db():
    sql = """CREATE DATABASE loja IF NOT EXISTS;"""
    cursor.execute(sql)


def create_table():
    sql = """CREATE TABLE produtos IF NOT EXISTS (
            id INT(10) NOT NULL,
            produto VARCHAR(255) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
            preco VARCHAR(255) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
            marca VARCHAR(255) NOT NULL COLLATE 'utf8mb4_0900_ai_ci'
            );"""
    cursor.execute(sql)


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
