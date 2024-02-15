import services.conectar_com_banco as db
import streamlit as st
import pandas as pd
import mysql.connector
def create_vinhos(vinhos):
    try:
        comando_create_vinhos= (f"""INSERT INTO vinhos(vinhoID,nomeVinho,tipoVinho,precoVinho,vinicolaID)
                                        VALUES({vinhos.vinhoID},'{vinhos.nomeVinho}','{vinhos.tipoVinho}',{vinhos.precoVinho},{vinhos.vinicolaID})""")
        db.cursor.execute(comando_create_vinhos)
        db.conexao.commit()
    except mysql.connector.IntegrityError as e:
        st.error("Você Está Violando a Restrição de Integridade Referencial de FK. Por Favor, Verifique Se a sua FK Já Está Cadastrada.")

def read_vinhos():
    comando_read_vinhos= (f"""SELECT * FROM vinhos
                                    """)
    db.cursor.execute(comando_read_vinhos)
    res = pd.DataFrame(db.cursor.fetchall(), columns=('ID Do Vinho','Nome do Vinho','Tipo do Vinho','Valor','Vinicola'))
    st.table(res)

def update_vinhos(coluna,novo_Valor,coluna_cond,condicao):
    comando_read_vinhos= (f"""UPDATE vinhos 
                                SET {coluna} = %s
                                    WHERE {coluna_cond} = %s
                                    """)
    db.cursor.execute(comando_read_vinhos,(novo_Valor,condicao))
    db.cursor.fetchall()

def read_vinhos_condicao(escolha,coluna,condicao):
    comando_read_vinhos= (f"""SELECT {escolha} FROM vinhos
                                    WHERE {coluna} = %s
                                    """)
    db.cursor.execute(comando_read_vinhos,(condicao,))
    res = pd.DataFrame(db.cursor.fetchall(), columns =([escolha]))
    st.table(res)

def delete_vinhos(ID):
    comando_delete_vinhos = (f"""DELETE FROM vinhos
                                        WHERE vinhoID = %s
                                    """)
    db.cursor.execute(comando_delete_vinhos,(ID,))
    db.conexao.commit()
