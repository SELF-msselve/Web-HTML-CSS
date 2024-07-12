import streamlit as st
import pandas as pd

 
#df = pd.read_csv('https://raw.githubusercontent.com/SELF-msselve/Web-HTML-CSS/main/AlquileresProp/prop.csv')
df = pd.read_csv('prop.csv')
for index, row in df.iterrows():
    my_expander = st.expander(row['Direccion'], expanded=False)
    with my_expander:
        for items in row:
            st.write(items)
