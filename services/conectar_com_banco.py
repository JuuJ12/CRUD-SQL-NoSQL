import mysql.connector

conexao= mysql.connector.connect(
    host ='localhost',
    user='USÁRIO DO BANCO DE DADOS',
    database='NOME DO DATABASE QUE SEJA UTILIZADO',
    password='SENHA DO SEU BANCO'
)
cursor = conexao.cursor()

