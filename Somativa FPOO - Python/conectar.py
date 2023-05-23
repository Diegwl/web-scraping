import mysql.connector


try:
    conexao = mysql.connector.connect(
        host='localhost',
        database='loja',
        user='root',
        password=''
    )

    cursor = conexao.cursor()
except:
    sql = """CREATE DATABASE loja IF NOT EXISTS;"""
    cursor.execute(sql)
