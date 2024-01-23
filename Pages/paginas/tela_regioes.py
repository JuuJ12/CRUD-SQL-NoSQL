import streamlit as st
import controllers.crud_regioes as isregiao
import models.regiao as Mregiao
import time
def tela_regiao():
     
        escolha_crud = st.selectbox('Qual Operação do CRUD Você Deseja Fazer', options=['CREATE','READ','UPADATE','DELETE'])
        if escolha_crud == 'CREATE':
            
                with st.form(key='include_regiao'):
                        input_regiaoID= st.text_input('Digite o Id da Sua Região')
                        input_nome_regiao= st.text_input('Digite o Nome da Sua Região')
                        input_estado_regiao= st.text_input('Digite o Estado da Sua Vinicola')
                        input_button_submit_regiao=st.form_submit_button('Enviar')

                if input_button_submit_regiao:
                        Mregiao.Regiao.regiaoID=input_regiaoID         #--|
                        Mregiao.Regiao.nomeRegiao=input_nome_regiao    #-- #Moldar A Entidade Regiões
                        Mregiao.Regiao.estadoRegiao=input_estado_regiao#--|
                        
                        isregiao.create_regioes(Mregiao.Regiao)
                     
        elif escolha_crud == 'READ':
                isregiao.read_regioes()
  
        elif escolha_crud == 'DELETE':
                isregiao.read_regioes()
                with st.form(key='deletar_regiao'):
                        input_coluna= st.selectbox('Selecione a Coluna', options=['regiaoID','nomeRegiao','estadoRegiao'])
                        input_condicao= st.text_input('Digite a Condição de Exclusão')
                        input_confirm_exclusao= st.form_submit_button('Excluir')

                if input_confirm_exclusao:
                        st.write('funcionou')
                        st.write(input_condicao)
                        isregiao.delete_regioes(input_condicao)
                                        

