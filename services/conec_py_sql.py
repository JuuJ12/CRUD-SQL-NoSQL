import mysql.connector

conexao= mysql.connector.connect(
    host ='localhost',
    user='root',
    database='vinicolas_copy',
    password='0000'
)
cursor = conexao.cursor()

