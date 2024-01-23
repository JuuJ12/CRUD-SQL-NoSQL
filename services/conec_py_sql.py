import mysql.connector

conexao= mysql.connector.connect(
    host ='insira seu host',
    user='insira seu usuário',
    database='O Banco de Dados que você vai Utilizar',
    password='A senha do Seu SQL'
)
cursor = conexao.cursor()

