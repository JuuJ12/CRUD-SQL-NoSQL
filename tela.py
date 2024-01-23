import streamlit as st
import Pages.paginas.tela_regioes as pagereg
import Pages.paginas.tela_vinicolas as pagevini
import Pages.paginas.tela_vinhos as pagevinho
st.title('CRUD TESTE')
escolha =st.selectbox('Selecione o DataFrame de Sua escolha',options=['Regiões','Vinicolas','Vinhos'])

#regioes
if escolha == 'Regiões':
  pagereg.tela_regiao()
 

    
#vinicolas
if escolha == 'Vinicolas':
    pagevini.tela_vinicola()
    


#Vinhos
if escolha == 'Vinhos':
    pagevinho.tela_vinho()