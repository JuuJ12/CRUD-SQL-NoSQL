import streamlit as st
import controllers.crud_vinhos as isvinhos
import models.vinhos as Mvinhos

def tela_vinho():
    escolha_crud = st.selectbox('Qual Operação do CRUD Você Deseja Fazer', options=['CREATE','READ','UPDATE','DELETE'])

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
    elif escolha_crud == 'READ':
        isvinhos.read_vinhos()
        st.title('Consulta  Com Condição')
        input_escolha = st.selectbox('O que Você Deseja Ver', options=['vinhoID','nomeVinho','tipoVinho','precoVinho','vinicolaID'])
        input_coluna = st.selectbox('Selecione a Coluna Que Atenderá a Sua Condição de Busca', options=['vinhoID','nomeVinho','tipoVinho','precoVinho','vinicolaID'])
        input_condicao = st.text_input('Digite a Condição de Busca')
        input_confirm_read = st.button('Pesquisar')
                            
        if input_confirm_read:
                isvinhos.read_vinhos_condicao(input_escolha, input_coluna, input_condicao)
        input_precos =st.button('Mais Caros e Mais Baratos')
        if input_precos:
                isvinhos.ponto_extra()
    elif escolha_crud == 'UPDATE':
            st.title('UPDATE')
            isvinhos.read_vinhos()
            input_coluna_up= st.selectbox('Coluna que Você Deseja Atualizar ', options=['vinhoID','nomeVinho','tipoVinho','precoVinho','vinicolaID'])
            novo_Valor= st.text_input('Digite o Novo Valor')
            coluna_condicao= st.selectbox('Qual Coluna Você Vai Usar Como Condição: ', options=['vinhoID','nomeVinho','tipoVinho','precoVinho','vinicolaID'])
            condicao= st.text_input('Digite a Condição')

                    
            input_confirm_update = st.button('Atualizar')
                            
            if input_confirm_update:
                    isvinhos.update_vinhos(input_coluna_up,novo_Valor,coluna_condicao,condicao)
    
    elif escolha_crud == 'DELETE':
                isvinhos.read_vinhos()
                input_excluir = st.selectbox('O que Você Deseja Excluir', options=['vinhoID','nomeVinho','tipoVinho','precoVinho','vinicolaID'])
                input_condicao = st.text_input('Digite a Condição de Exclusão')
                input_confirm_exclusao= st.button('Excluir')

                if input_confirm_exclusao:
                        isvinhos.delete_vinhos(input_excluir,input_condicao)
