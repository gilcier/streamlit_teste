## ANDRE R OLIVEIRA - RA 2302429
## PAULA PELINI RODRIGUES - RA 2302893

# import das bibliotecas 
import sqlalchemy as sqa 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()

# Site Dados de Mercado
navegador.get('https://www.dadosdemercado.com.br/')

# Clique em Ferramentas 
navegador.find_element(By.XPATH,'//*[@id="content"]/div[2]/a[1]/span').click()

lista_cotacao = []
for i in range(1, 101):
	ticket   = navegador.find_element(By.XPATH,'//*[@id="stocks"]/tbody/tr['+str(i)+']/td[1]/strong/a').text
	nome     = navegador.find_element(By.XPATH,'//*[@id="stocks"]/tbody/tr['+str(i)+']/td[2]').text
	negocios = navegador.find_element(By.XPATH,'//*[@id="stocks"]/tbody/tr['+str(i)+']/td[3]').text
	ultima   = navegador.find_element(By.XPATH,'//*[@id="stocks"]/tbody/tr['+str(i)+']/td[4]').text
	variacao = navegador.find_element(By.XPATH,'//*[@id="stocks"]/tbody/tr['+str(i)+']/td[5]').text
	
	lista_cotacao.append([ticket, nome, negocios, ultima, variacao])
	
df_cotacao = pd.DataFrame(lista_cotacao,columns=['Ticket','Nome','Negócios','Última(R$)','Variação'])

# ALTERANDO OS NOMES E FORMATANDO OS NOMES DAS COLUNAS
df_cotacao.rename(columns={'Negócios': 'Negocios', 'Última(R$)': 'Ultima', 'Variação': 'Variacao'}, inplace=True)

# ALTERANDO TIPO DE DADOS EM COLUNAS NUMERICAS

# Remover pontos e vírgulas de separação de milhares e converter para float
df_cotacao['Negocios'] = df_cotacao['Negocios'].str.replace('.', '').astype(float)

# Remover pontos e vírgulas de separação de milhares e converter para float
df_cotacao['Ultima'] = df_cotacao['Ultima'].str.replace(',', '.').astype(float)

# Remover sinal de '+' e '%' , substituir vírgulas por pontos antes de converter para float
df_cotacao['Variacao'] = df_cotacao['Variacao'].str.replace('+', '').str.replace(',', '.').str.replace('%', '').astype(float)

# SALVANDO DADOS EM CSV E JSON
df_cotacao.to_csv('../0_bases_originais/dados_originais.csv', sep=';' ,index=False, encoding='utf-8')
df_cotacao.to_json('../0_bases_originais/dados_originais.json')

# SALVANDO OS DADOS DO DATAFRAME NO BANCO 
engine = sqa.create_engine("sqlite:///df_cotacao.db", echo=True)
conn = engine.connect()

df_cotacao.to_sql('cotacao', con=conn, if_exists='replace', index=False)

navegador.quit()