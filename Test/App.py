import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Visor de archivos Excel")

archivo_excel = st.file_uploader("Selecciona un archivo Excel", type=["xlsx", "xls"])

if archivo_excel is not None:
    try:
        # Leer el archivo Excel
        df = pd.read_excel(archivo_excel)

        # Mostrar el contenido
        st.subheader("Contenido del archivo:")
        st.dataframe(df, use_container_width=True)

        # Convertir el DataFrame a un archivo Excel en memoria usando openpyxl
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
        output.seek(0)

        # Botón para descargar el archivo modificado
        st.download_button(
            label="📥 Descargar archivo modificado",
            data=output,
            file_name="archivo_modificado.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"Ocurrió un error al leer el archivo: {e}")
