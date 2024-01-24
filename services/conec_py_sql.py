import mysql.connector

conexao= mysql.connector.connect(
    host ='o seu host',
    user='seu usuario',
    database='a base de dados',
    password='a senha do seu banco'
)
cursor = conexao.cursor()

