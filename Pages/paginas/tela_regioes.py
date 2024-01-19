import streamlit as st
import controllers.crud_regioes as isregiao
import models.regiao as Mregiao

def tela_regiao():
    escolha_crud = st.selectbox('Qual Operação do CRUD Você Deseja Fazer', options=['CREATE','READ','UPADATE','DELETE'])
    if escolha_crud == 'CREATE':
            
            with st.form(key='include_regiao'):
                    input_regiaoID= st.text_input('Digite o Id da Sua Região')
                    input_nome_regiao= st.text_input('Digite o Nome da Sua Região')
                    input_estado_regiao= st.text_input('Digite o Estado da Sua Vinicola')
                    input_button_submit_regiao=st.form_submit_button('Enviar')

            if input_button_submit_regiao:
                    Mregiao.regiaoID=input_regiaoID         #--|
                    Mregiao.nomeRegiao=input_nome_regiao    #-- #Moldar A Entidade Regiões
                    Mregiao.estadoRegiao=input_estado_regiao#--|
                    
                    isregiao.create_regioes(Mregiao)
    if escolha_crud == 'READ':
           isregiao.read_regioes()
    if escolha_crud == 'UPADATE':
            st.title('funcionou')
    if escolha_crud == 'DELETE':
        
            st.title('funcionou')