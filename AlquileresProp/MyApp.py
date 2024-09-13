import streamlit as st
import pandas as pd

 
df = pd.read_excel('https://raw.githubusercontent.com/SELF-msselve/Web-HTML-CSS/main/AlquileresProp/prop.xlsx')
#df = pd.read_excel('prop.xlsx')
print(df)
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

/* Asegúrate de que la página esté bien escalada en dispositivos móviles */
@media only screen and (max-width: 600px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}

</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Contenido de la aplicación
st.title("SELF Propiedades")
st.sidebar.title("Menú Lateral")
st.write("Esta es una aplicación de ejemplo usando Streamlit.")

df_columns = df.columns
for index, row in df.iterrows():
    my_expander = st.expander(row['Direccion'], expanded=False)
    with my_expander:
        #col1, col2 = st.columns([1,1])
        contador = 0
        for items in row:
            st.write(df_columns[contador], ': ', items)
            contador += 1


# df_columns = df.columns
# #print(df_columns[2])

# for index, row in df.iterrows():
#     contador = 0
#     for datos in row:
#         print(df_columns[contador], ' : ', datos)
#         contador += 1
