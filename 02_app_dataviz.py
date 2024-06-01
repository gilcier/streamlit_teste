## ANDRE R OLIVEIRA - RA 2302429
## PAULA PELINI RODRIGUES - RA 2302893

import sqlalchemy as sqa 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos dados 

df_cotacao = pd.read_csv('../0_bases_originais/dados_originais.csv', sep=';')

# Titulo do App
st.title('Dados das Ações')

# Imagem do App 
cotacao_sidebar = st.sidebar.image('https://img.freepik.com/vetores-premium/bolsa-de-valores-com-design-de-ilustracao-de-modelo-de-logotipo-de-seta-eps-10_822766-7510.jpg')

# Selectbox para exibir os dados do ticket 
selected_ticket = st.sidebar.selectbox('Selecione um Ticket', df_cotacao['Ticket'])

# Filtrando os dados com base no ticket selecionado a partir do Selectbox acima
selected_data = df_cotacao[df_cotacao['Ticket'] == selected_ticket]

# Exibindo os detalhes do ticket selecionado
st.header(f'Detalhes do Ticket: {selected_ticket}')
st.write(selected_data)

# Exibindo gráficos
st.header('Gráficos')

# Gráfico de Negócios por Ticket
st.subheader('Negócios por Ticket')
st.bar_chart(df_cotacao.set_index('Ticket')['Negocios'])

# Gráfico de Última Cotação por Ticket
st.subheader('Última Cotação por Ticket')
st.line_chart(df_cotacao.set_index('Ticket')['Ultima'])

# Gráfico de Variação por Ticket
st.subheader('Variação por Ticket')
st.bar_chart(df_cotacao.set_index('Ticket')['Variacao'])

# Exibindo os dados em uma tabela
st.header('Tabela de Dados Gerais')
st.dataframe(df_cotacao, width=1500, height=500, hide_index=True)

# Gráfico de Pizza para os top 10 negócios,

df_top10 = df_cotacao.nlargest(10, 'Negocios') 

st.subheader('Top 10 Empresas x Ações negociadas')
fig, ax = plt.subplots()
ax.pie(df_top10['Negocios'], labels=df_top10['Nome'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)

# Informações adicionais
st.header('Informações Adicionais')
st.write('Este aplicativo exibe dados sobre diferentes ações, incluindo o número de negócios, última cotação e variação.')