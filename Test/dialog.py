import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Visor de archivos Excel")

# Subida del archivo
archivo_excel = st.file_uploader("Selecciona un archivo Excel", type=["xlsx", "xls"])

# Verifica si se ha subido un archivo
if archivo_excel is not None:
    try:
        # Carga el archivo en un DataFrame
        df = pd.read_excel(archivo_excel)

        # Muestra el DataFrame
        st.subheader("Contenido del archivo:")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Ocurrió un error al leer el archivo: {e}")

