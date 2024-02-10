import streamlit as st
import controllers.crud_vinicolas as isvinicolas
import models.vinicolas as Mvinicolas

def tela_vinicola():
    escolha_crud = st.selectbox('Qual Operação do CRUD Você Deseja Fazer', options=['CREATE','READ','UPDATE','DELETE'])

    if escolha_crud == 'CREATE': #CREATE

        with st.form(key='include_vinicolas'):
            input_vinicolaId= st.number_input(label='Insira o ID da Sua Vinicola', format='%d', step=1)
            input_name_vinicola= st.text_input(label='Insira o Nome da Vinicola')
            input_phone= st.text_input(label='Digite o Número de Contato da Sua Vinicola')
            input_regiao= st.text_input(label='Digite o ID da Região da Sua Vinicola').upper()
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
            st.title('Consulta  Com Condição')
            input_escolha = st.selectbox('O que Você Deseja Ver', options=['vinicolaID','nomeVinicola','foneVinicola','regiaoID'])
            input_coluna = st.selectbox('Selecione a Coluna', options=['vinicolaID','nomeVinicola','foneVinicola','regiaoID'])
            input_condicao = st.text_input('Digite a Condição de Busca')
            input_confirm_read = st.button('Pesquisar')
                            
            if input_confirm_read:
                isvinicolas.read_vinicolas_condicao(input_escolha, input_coluna, input_condicao)
    elif escolha_crud == 'UPDATE':
            st.title('UPDATE')
            isvinicolas.read_vinicolas()
            input_coluna_up= st.selectbox('Coluna que Você Deseja Atualizar ', options=['vinicolaID','nomeVinicola','foneVinicola','regiaoID'])
            novo_Valor= st.text_input('Digite o Novo Valor')
            coluna_condicao= st.selectbox('Qual Coluna Você Vai Usar Como Condição: ', options=['vinicolaID','nomeVinicola','foneVinicola','regiaoID'])
            condicao= st.text_input('Digite a Condição')

                    
            input_confirm_update = st.button('Atualizar')
                            
            if input_confirm_update:
                    isvinicolas.update_vinicolas(input_coluna_up,novo_Valor,coluna_condicao,condicao)

    elif escolha_crud == 'DELETE':
            isvinicolas.read_vinicolas()
            with st.form(key='deletar_vinicolas'):
                input_condicao= st.number_input('Digite o ID Para Realizar a Exclusão', step=1)
                input_confirm_exclusao= st.form_submit_button('Excluir')

            if input_confirm_exclusao:
                isvinicolas.delete_vinicolas(input_condicao)
