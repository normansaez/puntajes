import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.set_page_config(page_title='Puntajes', page_icon='📊')
st.title('📊 Puntajes')

seleccion = st.radio(
    "Selecciona 👉",
    key="visibility",
    options=["Femenino", "Masculino"],
)
# Load data
if seleccion == 'Femenino':
    st.write(seleccion)
    df = pd.read_csv('data/completoF.csv')
elif seleccion == 'Masculino':
    st.write(seleccion)
    df = pd.read_csv('data/completo.csv')
df_editor = st.data_editor(df, height=212, use_container_width=True,num_rows="dynamic")
if seleccion == 'Femenino':
    st.write(seleccion)
    df = pd.read_csv('data/finalF.csv')
elif seleccion == 'Masculino':
    st.write(seleccion)
    df = pd.read_csv('data/final.csv')

df = df.reset_index(drop=True)
column_to_sort_by = st.selectbox('Selecciona la columna por la cual ordenar:', df.columns)
ascending = True
if column_to_sort_by == 'diff':
    ascending = False
df_ordenado = df.sort_values(by=column_to_sort_by, ascending=ascending)
df_ordenado = df_ordenado.reset_index(drop=True)
st.write(f"Ordenado por la columna '{column_to_sort_by}':")
st.write(df_ordenado)
#st.text(df_ordenado.to_string(index=False))

