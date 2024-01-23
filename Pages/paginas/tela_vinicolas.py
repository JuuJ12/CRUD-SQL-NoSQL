import streamlit as st
import controllers.crud_vinicolas as isvinicolas
import models.vinicolas as Mvinicolas

def tela_vinicola():
    escolha_crud = st.selectbox('Qual Operação do CRUD Você Deseja Fazer', options=['CREATE','READ','UPADATE','DELETE'])

    if escolha_crud == 'CREATE': #CREATE

        with st.form(key='include_vinicolas'):
            input_vinicolaId= st.number_input(label='Insira o ID da Sua Vinicola', format='%d', step=1)
            input_name_vinicola= st.text_input(label='Insira o Nome da Vinicola')
            input_phone= st.text_input(label='Digite o Número de Contato da Sua Vinicola')
            input_regiao= st.text_input(label='Digite a Região da Sua Vinicola').upper()
            input_button_submit_vinicola= st.form_submit_button('Enviar')

        if input_button_submit_vinicola:
            Mvinicolas.vinicolaID=input_vinicolaId      #---
            Mvinicolas.nomeVinicola=input_name_vinicola #   |--
                                                            #Moldar A Entidade Vinicolas
            Mvinicolas.foneVinicola=input_phone         #   |--
            Mvinicolas.regiaoID=input_regiao            #---

            isvinicolas.create_vinicolas(Mvinicolas)
    elif escolha_crud == 'READ':
            isvinicolas.read_vinicolas()
    #if escolha_crud == 'UPADATE':

    elif escolha_crud == 'DELETE':
            isvinicolas.read_vinicolas()
            with st.form(key='deletar_vinicolas'):
                input_condicao= st.number_input('Digite o ID Para Realizar a Exclusão', step=1)
                input_confirm_exclusao= st.form_submit_button('Excluir')

            if input_confirm_exclusao:
                st.write('funcionou')
                st.write(input_condicao)
                isvinicolas.delete_vinicolas(input_condicao)
