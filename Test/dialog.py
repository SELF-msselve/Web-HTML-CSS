
import streamlit as st
import pandas as pd

# Configura el diseño de la página para que sea más ancho
st.set_page_config(layout="wide")

# Divide la pantalla en dos columnas con proporciones 1:3
col1, col2 = st.columns([1, 3], vertical_alignment="bottom")

with col1:
    st.title("Visor de archivos Excel")
    archivo_excel = st.file_uploader("Selecciona un archivo Excel", type=["xlsx", "xls"])

with col2:
    if archivo_excel is not None:
        try:
            df = pd.read_excel(archivo_excel)
            st.subheader("Contenido del archivo:")
            st.dataframe(df, use_container_width=True)
        except Exception as e:
            st.error(f"Ocurrió un error al leer el archivo: {e}")



