import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# Configurar la página
st.set_page_config(page_title="Mi Aplicación", layout="wide")

# Crear el menú en el header
with st.sidebar:
    selected = option_menu(
        menu_title="Menú Principal",  # required
        options=["Pantalla 1", "Pantalla 2"],  # required
        icons=["house", "gear"],  # Opcional
        menu_icon="cast",  # Opcional
        default_index=0,  # Opcional
    )

# Contenido para Pantalla 1
if selected == "Pantalla 1":
    st.title("Pantalla 1")
    st.write("Este es el contenido de la Pantalla 1.")
    # Aquí puedes agregar más contenido para la Pantalla 1
    data = {
        'Nombre': ['Alice', 'Bob', 'Charlie', 'David'],
        'Edad': [24, 27, 22, 32],
        'Ciudad': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)
    st.dataframe(df)

# Contenido para Pantalla 2
elif selected == "Pantalla 2":
    st.title("Pantalla 2")
    st.write("Este es el contenido de la Pantalla 2.")
    # Aquí puedes agregar más contenido para la Pantalla 2
    st.write("Aquí puedes poner gráficos, tablas o cualquier otro contenido.")
