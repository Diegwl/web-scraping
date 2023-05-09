import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='megasena',
    user='root',
    password=''
)

cursor = conexao.cursor()
