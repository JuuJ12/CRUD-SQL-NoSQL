import services.conec_py_sql as db
import streamlit as st
def create_regioes(regiao):
    comando_create_regioes= (f"""INSERT INTO REGIOES(regiaoID,nomeRegiao,estadoRegiao)
                                    VALUES({regiao.regiaoID},'{regiao.nomeRegiao}','{regiao.estadoRegiao}')""")
    db.cursor.execute(comando_create_regioes)
    db.conexao.commit()

def read_regioes():
    comando_read_regioes= (f"""SELECT * FROM REGIOES
                                    """)
    db.cursor.execute(comando_read_regioes)
    res = db.cursor.fetchall()
    st.table(res)