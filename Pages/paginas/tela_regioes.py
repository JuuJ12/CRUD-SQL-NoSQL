import streamlit as st
import controllers.crud_regioes as isregiao
import models.regiao as Mregiao

def tela_regiao():
     
        escolha_crud = st.selectbox('Qual Operação do CRUD Você Deseja Fazer', options=['CREATE','READ','UPDATE','DELETE'])
        if escolha_crud == 'CREATE':
                st.title('CREATE')
                with st.form(key='include_regiao'):
                        input_regiaoID= st.text_input('Digite o Id da Sua Região: ')
                        input_nome_regiao= st.text_input('Digite o Nome da Sua Região')
                        input_estado_regiao= st.text_input('Digite o Estado da Sua Vinicola')
                        input_button_submit_regiao=st.form_submit_button('Enviar')

                if input_button_submit_regiao:
                        Mregiao.Regiao.regiaoID=input_regiaoID         #--|
                        Mregiao.Regiao.nomeRegiao=input_nome_regiao    #-- #Moldar A Entidade Regiões
                        Mregiao.Regiao.estadoRegiao=input_estado_regiao#--|
                        
                        isregiao.create_regioes(Mregiao.Regiao)
                     
        elif escolha_crud == 'READ':
                st.title('READ')
                
                isregiao.read_regioes()

                st.title('Consulta  Com Condição')
                input_escolha = st.selectbox('O que Você Deseja Ver', options=['regiaoID','nomeRegiao','estadoRegiao'])
                input_coluna = st.selectbox('Selecione a Coluna Que Atenderá a Sua Condição de Busca', options=['regiaoID','nomeRegiao','estadoRegiao'])
                input_condicao = st.text_input('Digite a Condição de Busca')
                input_confirm_read = st.button('Pesquisar')
                        
                if input_confirm_read:
                                isregiao.read_regioes_condicao(input_escolha, input_coluna, input_condicao)

        elif escolha_crud == 'UPDATE':
                st.title('UPDATE')
                isregiao.read_regioes()
                input_coluna_up= st.selectbox('Coluna que Você Deseja Atualizar ', options=['regiaoID','nomeRegiao','estadoRegiao'])
                novo_Valor= st.text_input('Digite o Novo Valor')
                coluna_condicao= st.selectbox('Qual Coluna Você Vai Usar Como Condição: ', options=['regiaoID','nomeRegiao','estadoRegiao'])
                condicao= st.text_input('Digite a Condição')

                
                input_confirm_update = st.button('Atualizar')
                        
                if input_confirm_update:
                        isregiao.update_regioes(input_coluna_up,novo_Valor,coluna_condicao,condicao)
  
        elif escolha_crud == 'DELETE':
                st.title('DELETE')
                isregiao.read_regioes()
                with st.form(key='deletar_regiao'):
                        input_coluna= st.selectbox('Selecione a Coluna', options=['regiaoID','nomeRegiao','estadoRegiao'])
                        input_condicao= st.text_input('Digite a Condição de Exclusão')
                        input_confirm_exclusao= st.form_submit_button('Excluir')

                if input_confirm_exclusao:
                        isregiao.delete_regioes(input_coluna,input_condicao)
                                        

