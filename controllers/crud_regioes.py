import services.conectar_com_banco as db
import streamlit as st
import pandas as pd
import mysql.connector


def create_regioes(regiao):
    try:
        comando_create_regioes= (f"""INSERT INTO REGIOES(regiaoID,nomeRegiao,estadoRegiao)
                                        VALUES('{regiao.regiaoID}','{regiao.nomeRegiao}','{regiao.estadoRegiao}')""")
        db.cursor.execute(comando_create_regioes)
        db.conexao.commit()
        st.success('Região Criada Com Sucesso',icon='✅')
    except mysql.connector.IntegrityError as e:
        st.error("Você está violando a restrição de integridade de FK. Por favor, verifique se a sua FK já está cadastrada.")

def read_regioes():
    comando_read_regioes= (f"""SELECT * FROM REGIOES
                                    """)
    db.cursor.execute(comando_read_regioes)
    res = pd.DataFrame(db.cursor.fetchall(), columns =('ID Região','Nome da Região','Estado'))
    st.table(res)

def read_regioes_condicao(escolha,coluna,condicao):
    comando_read_regioes= (f"""SELECT {escolha} FROM REGIOES
                                    WHERE {coluna} = %s
                                    """)
    
    db.cursor.execute(comando_read_regioes,(condicao,))
    res = pd.DataFrame(db.cursor.fetchall(), columns =([escolha]))
    st.table(res)

def update_regioes(coluna,novo_Valor,coluna_cond,condicao):
    comando_read_regioes= (f"""UPDATE REGIOES 
                                SET {coluna} = %s
                                    WHERE {coluna_cond} = %s
                                    """)
    db.cursor.execute(comando_read_regioes,(novo_Valor,condicao))
    db.cursor.fetchall()
    st.success('Atualização Bem Sucedida',icon='✅')


def delete_regioes(coluna,condicao):
    comando_delete_regioes = (f"""DELETE FROM REGIOES
                                        WHERE {coluna} = %s
                                    """)
    db.cursor.execute(comando_delete_regioes,(condicao,))
    db.conexao.commit()
    st.success('Remoção Realizada Com Sucesso',icon='✅')
