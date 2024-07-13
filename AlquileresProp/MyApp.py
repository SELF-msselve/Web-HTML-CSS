import streamlit as st
import pandas as pd

 
df = pd.read_excel('https://raw.githubusercontent.com/SELF-msselve/Web-HTML-CSS/main/AlquileresProp/prop.xlsx')
#df = pd.read_excel('prop.xlsx')

# Configurar la página
st.set_page_config(
    page_title="SELF Propiedades",  # Título de la pestaña del navegador
    page_icon=":smiley:",  # Icono de la pestaña del navegador (puede ser un emoji o una ruta a una imagen)
    layout="centered",  # Otras opciones son 'centered'
)
#     initial_sidebar_state="expanded",  # Estado inicial de la barra lateral ('collapsed' o 'expanded')
# )

# CSS para ocultar los menús y el pie de página de Streamlit
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stApp {
    top: 0px;
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Contenido de la aplicación
st.title("Bienvenido a SELF Propiedades")
# st.sidebar.title("Menú Lateral")
# st.write("Esta es una aplicación de ejemplo usando Streamlit.")

df_columns = df.columns
for index, row in df.iterrows():
    my_expander = st.expander(row['Direccion'], expanded=False)
    with my_expander:
        col1, col2 = st.columns([1,2])
        contador = 0
        for items in row:
            with col1:
                st.write(df_columns[contador], ' : ')
            with col2:    
                st.write(items)
            contador += 1


# df_columns = df.columns
# #print(df_columns[2])

# for index, row in df.iterrows():
#     contador = 0
#     for datos in row:
#         print(df_columns[contador], ' : ', datos)
#         contador += 1
