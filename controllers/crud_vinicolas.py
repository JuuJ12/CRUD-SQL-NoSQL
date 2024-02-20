import services.conectar_com_banco as db
import streamlit as st
import pandas as pd
import mysql.connector

def create_vinicolas(vinicolas):
    try:
        comando_create_vinicolas= (f"""INSERT INTO vinicolas(vinicolaID,nomeVinicola,foneVinicola,regiaoID)
                                        VALUES({vinicolas.vinicolaID},'{vinicolas.nomeVinicola}',{vinicolas.foneVinicola},'{vinicolas.regiaoID}')""")
        db.cursor.execute(comando_create_vinicolas)
        db.conexao.commit()
        st.success('Vinicola Criada Com Sucesso', icon='✅')
    except mysql.connector.IntegrityError as e:
         st.error("Você Está Violando a Restrição de Integridade Referencial de FK. Por Favor, Verifique Se a sua FK Já Está Cadastrada.")

def read_vinicolas():
    comando_read_vinicolas= (f"""SELECT * FROM vinicolas
                                    """)
    db.cursor.execute(comando_read_vinicolas)
    res = pd.DataFrame(db.cursor.fetchall(), columns=('ID da Vinicola','Nome da Vinicola','Contato','Região'))
    st.table(res)

def read_vinicolas_condicao(escolha,coluna,condicao):
    comando_read_vinicolas= (f"""SELECT {escolha} FROM vinicolas
                                    WHERE {coluna} = %s
                                    """)
    db.cursor.execute(comando_read_vinicolas,(condicao,))
    res = pd.DataFrame(db.cursor.fetchall(), columns =([escolha]))
    st.table(res)

def update_vinicolas(coluna,novo_Valor,coluna_cond,condicao):
    comando_read_vinicolas= (f"""UPDATE vinicolas 
                                SET {coluna} = %s
                                    WHERE {coluna_cond} = %s
                                    """)
    db.cursor.execute(comando_read_vinicolas,(novo_Valor,condicao))
    db.cursor.fetchall()
    st.success('Atualização Realizada Com Sucesso',icon='✅')
def delete_vinicolas(coluna,condicao):
    comando_delete_vinicolas = (f"""DELETE FROM vinicolas
                                        WHERE {coluna} = %s
                                    """)
    db.cursor.execute(comando_delete_vinicolas,(condicao,))
    db.conexao.commit()
    st.success('Remoção Realizada Com Sucesso', icon='✅')