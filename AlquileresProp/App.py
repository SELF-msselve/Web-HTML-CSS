import streamlit as st
import pandas as pd

# Datos de ejemplo
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie', 'David'],
    'Edad': [24, 27, 22, 32],
    'Ciudad': ['Nueva York', 'Los Ángeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# Función para mostrar la tabla con checkboxes
def display_table_with_checkboxes(df):
    st.write("Selecciona las filas:")
    selected_rows = []
    
    for index, row in df.iterrows():
        checkbox = st.checkbox(f"{row['Nombre']}, {row['Edad']}, {row['Ciudad']}", key=index)
        if checkbox:
            selected_rows.append(row)
    
    return selected_rows

# Título de la aplicación
st.title("Tabla con selección de filas")

# Mostrar tabla con checkboxes
selected_rows = display_table_with_checkboxes(df)

# Mostrar las filas seleccionadas
if selected_rows:
    st.write("Filas seleccionadas:")
    selected_df = pd.DataFrame(selected_rows)
    st.dataframe(selected_df)
else:
    st.write("No se han seleccionado filas.")

