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
def delete_vinicolas(ID):
    comando_delete_vinicolas = (f"""DELETE FROM vinicolas
                                        WHERE vinicolaID = %s
                                    """)
    db.cursor.execute(comando_delete_vinicolas,(ID,))
    db.conexao.commit()