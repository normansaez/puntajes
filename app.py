import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.set_page_config(page_title='Puntajes', page_icon='📊')
st.title('📊 Puntajes')


# Load data
df = pd.read_csv('data/completo.csv')
df_editor = st.data_editor(df, height=212, use_container_width=True,num_rows="dynamic")

df = pd.read_csv('data/final.csv')
column_to_sort_by = st.selectbox('Selecciona la columna por la cual ordenar:', df.columns)
if column_to_sort_by == 'diff':
    ascending = False
else:
    ascending = True
df_ordenado = df.sort_values(by=column_to_sort_by, ascending)
st.write("DataFrame original:")
st.write(df)
st.write(f"DataFrame ordenado por la columna '{column_to_sort_by}':")
st.write(df_ordenado)
df_editor = st.data_editor(df, height=212, use_container_width=True,num_rows="dynamic")

