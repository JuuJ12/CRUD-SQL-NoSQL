import services.conec_py_sql as db
import streamlit as st
import pandas as pd
def create_vinicolas(vinicolas):
    comando_create_vinicolas= (f"""INSERT INTO vinicolas(vinicolaID,nomeVinicola,foneVinicola,regiaoID)
                                    VALUES({vinicolas.vinicolaID},'{vinicolas.nomeVinicola}',{vinicolas.foneVinicola},'{vinicolas.regiaoID}')""")
    db.cursor.execute(comando_create_vinicolas)
    db.conexao.commit()
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

def delete_vinicolas(ID):
    comando_delete_vinicolas = (f"""DELETE FROM vinicolas
                                        WHERE vinicolaID = %s
                                    """)
    db.cursor.execute(comando_delete_vinicolas,(ID,))
    db.conexao.commit()