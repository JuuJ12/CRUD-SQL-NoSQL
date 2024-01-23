import services.conec_py_sql as db
import streamlit as st
import pandas as pd
@st.cache
def create_regioes(regiao):
    comando_create_regioes= (f"""INSERT INTO REGIOES(regiaoID,nomeRegiao,estadoRegiao)
                                    VALUES({regiao.regiaoID},'{regiao.nomeRegiao}','{regiao.estadoRegiao}')""")
    db.cursor.execute(comando_create_regioes)
    db.conexao.commit()

def read_regioes():
    comando_read_regioes= (f"""SELECT * FROM REGIOES
                                    """)
    db.cursor.execute(comando_read_regioes)
    res = pd.DataFrame(db.cursor.fetchall(), columns =('ID Região','Nome da Região','Estado'))
    st.table(res)
def delete_regioes(ID):
    comando_delete_regioes = (f"""DELETE FROM REGIOES
                                        WHERE regiaoID = %s
                                    """)
    db.cursor.execute(comando_delete_regioes,(ID,))
    db.conexao.commit()
