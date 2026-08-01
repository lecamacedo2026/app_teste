import streamlit as st
import pandas as pd


st.title('Minha web page')

st.image('image.png')

dados = pd.read_csv('dados.csv')
df = pd.DataFrame(dados)
st.write(dados)



# graficos

st.bar_chart(df, x = 'vendedor', y =  'vendas')

st.map()


