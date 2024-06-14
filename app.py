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

#df = pd.read_csv('data/final.csv')
df_editor = st.data_editor(df, height=212, use_container_width=True,num_rows="dynamic")

