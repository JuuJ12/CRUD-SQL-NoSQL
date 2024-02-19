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

def delete_vinhos(coluna,condicao):
    comando_delete_vinhos = (f"""DELETE FROM vinhos
                                        WHERE {coluna} = %s
                                    """)
    db.cursor.execute(comando_delete_vinhos,(condicao,))
    db.conexao.commit()

def ponto_extra():
    comando_min_max= (f"""SELECT tipoVinho,
       max(precoVinho) AS MaisCaro,
       min(precoVinho) AS MaisBarato,
       (SELECT nomeVinho FROM vinhos WHERE tipoVinho = v.tipoVinho AND precoVinho = max(v.precoVinho)) AS VinhoMaisCaro,
       (SELECT nomeVinho FROM vinhos WHERE tipoVinho = v.tipoVinho AND precoVinho = min(v.precoVinho)) AS VinhoMaisBarato
        FROM vinhos v
        GROUP BY tipoVinho""")
    db.cursor.execute(comando_min_max)
    res = pd.DataFrame(db.cursor.fetchall(), columns=('Tipo do Vinho','Maior Valor','Menor Valor','Vinho Mais Caro','Vinho Mais Barato'))
    st.table(res)

def verificar_trigger_existente():
    try:
        # Verifica se o trigger já existe no banco de dados
        db.cursor.execute("""SELECT *
                            FROM INFORMATION_SCHEMA.TRIGGERS
                            WHERE TRIGGER_NAME = 'valor_max'""")
        trigger_existente = db.cursor.fetchone()
        
        # Se o trigger já existir, retorna True
        if trigger_existente:
            return True
        else:
            return False
    except mysql.connector.Error as e:
        st.error(f"Erro ao verificar se o trigger existe: {e}")
        return False



# Função para criar o trigger
def criar_trigger():
    try:
        comando_criar_trigger = f"""CREATE TRIGGER valor_max
                                        BEFORE INSERT ON vinhos
                                        FOR EACH ROW
                                        BEGIN
                                            IF NEW.precoVinho > 1000.00 THEN
                                                SET NEW.precoVinho = 950.00;
                                            END IF;
                                        END;
                                    """
        db.cursor.execute(comando_criar_trigger)
        db.conexao.commit()
        st.success('Trigger criado com sucesso!')
    except mysql.connector.Error as e:
        st.error(f"Erro ao criar o trigger: {e}")
