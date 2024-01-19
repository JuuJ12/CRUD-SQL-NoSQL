import streamlit as st
import controllers.crud_vinhos as isvinhos
import models.vinhos as Mvinhos

def tela_vinho():
    escolha_crud = st.selectbox('Qual Operação do CRUD Você Deseja Fazer', options=['CREATE','READ','UPADATE','DELETE'])

    if escolha_crud == 'CREATE':
        with st.form(key='include_vinhos'):
            input_vinhoId= st.number_input('Digite o ID do Vinho', format='%d', step=1)
            input_nome_vinho= st.text_input('Digite o Nome do Vinho')
            input_tipo_vinho= st.text_input('Digite o Tipo do Vinho')
            input_preco_vinho= st.number_input('Digite o Preço do Vinho')
            input_vinicolaid= st.number_input('Digite o ID da Vinicola', format='%d', step=1)
            input_button_submit_vinhos= st.form_submit_button('Enviar')
        if input_button_submit_vinhos:
            Mvinhos.vinhoID= input_vinhoId
            Mvinhos.nomeVinho= input_nome_vinho
            Mvinhos.tipoVinho= input_tipo_vinho
            Mvinhos.precoVinho= input_preco_vinho
            Mvinhos.vinicolaID= input_vinicolaid

            isvinhos.create_vinhos(Mvinhos)
    if escolha_crud == 'READ':
        isvinhos.read_vinhos()
