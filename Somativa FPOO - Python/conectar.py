import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='loja',
    user='root',
    password=''
)

cursor = conexao.cursor()
