import services.conec_py_sql as db
import streamlit as st
import pandas as pd

def create_regioes(regiao):
    comando_create_regioes= (f"""INSERT INTO REGIOES(regiaoID,nomeRegiao,estadoRegiao)
                                    VALUES('{regiao.regiaoID}','{regiao.nomeRegiao}','{regiao.estadoRegiao}')""")
    db.cursor.execute(comando_create_regioes)
    db.conexao.commit()

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
    


def delete_regioes(coluna,condicao):
    comando_delete_regioes = (f"""DELETE FROM REGIOES
                                        WHERE {coluna} = %s
                                    """)
    db.cursor.execute(comando_delete_regioes,(condicao,))
    db.conexao.commit()
