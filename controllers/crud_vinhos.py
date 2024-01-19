import services.conec_py_sql as db
import streamlit as st
def create_vinhos(vinhos):
    comando_create_vinhos= (f"""INSERT INTO vinhos(vinhoID,nomeVinho,tipoVinho,precoVinho,vinicolaID)
                                    VALUES({vinhos.vinhoID},'{vinhos.nomeVinho}','{vinhos.tipoVinho}',{vinhos.precoVinho},{vinhos.vinicolaID})""")
    db.cursor.execute(comando_create_vinhos)
    db.conexao.commit()

def read_vinhos():
    comando_read_vinhos= (f"""SELECT * FROM vinhos
                                    """)
    db.cursor.execute(comando_read_vinhos)
    res = db.cursor.fetchall()
    st.table(res)