import services.conec_py_sql as db
import streamlit as st
import pandas as pd
def create_vinhos(vinhos):
    comando_create_vinhos= (f"""INSERT INTO vinhos(vinhoID,nomeVinho,tipoVinho,precoVinho,vinicolaID)
                                    VALUES({vinhos.vinhoID},'{vinhos.nomeVinho}','{vinhos.tipoVinho}',{vinhos.precoVinho},{vinhos.vinicolaID})""")
    db.cursor.execute(comando_create_vinhos)
    db.conexao.commit()

def read_vinhos():
    comando_read_vinhos= (f"""SELECT * FROM vinhos
                                    """)
    db.cursor.execute(comando_read_vinhos)
    res = pd.DataFrame(db.cursor.fetchall(), columns=('ID Do Vinho','Nome do Vinho','Tipo do Vinho','Valor','Vinicola'))
    st.table(res)

def delete_vinhos(ID):
    comando_delete_vinhos = (f"""DELETE FROM vinhos
                                        WHERE vinhoID = %s
                                    """)
    db.cursor.execute(comando_delete_vinhos,(ID,))
    db.conexao.commit()
