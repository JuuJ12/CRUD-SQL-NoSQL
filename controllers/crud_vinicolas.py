import services.conec_py_sql as db
import streamlit as st
def create_vinicolas(vinicolas):
    comando_create_vinicolas= (f"""INSERT INTO vinicolas(vinicolaID,nomeVinicola,foneVinicola,regiaoID)
                                    VALUES({vinicolas.vinicolaID},'{vinicolas.nomeVinicola}',{vinicolas.foneVinicola},'{vinicolas.regiaoID}')""")
    db.cursor.execute(comando_create_vinicolas)
    db.conexao.commit()
def read_vinicolas():
    comando_read_vinicolas= (f"""SELECT * FROM vinicolas
                                    """)
    db.cursor.execute(comando_read_vinicolas)
    res = db.cursor.fetchall()
    st.table(res)