import streamlit as st
import pandas as pd
import sqlite3

# Conectar a la base de datos SQLite
conn = sqlite3.connect('example.db')

# Leer la tabla 'people' en un DataFrame
df = pd.read_sql_query("SELECT * FROM people", conn)

# Mostrar el DataFrame en Streamlit
st.write("Base de datos original:")
st.dataframe(df)

# Permitir la edición del DataFrame
edited_df = st.data_editor(df)

# Formulario para agregar nuevas filas
st.write("Agregar nueva fila:")
new_row = {
    'Name': st.text_input('Nombre'),
    'Age': st.number_input('Edad', min_value=0, max_value=120),
    'City': st.text_input('Ciudad')
}

if st.button('Agregar fila'):
    new_row_df = pd.DataFrame([new_row])
    edited_df = pd.concat([edited_df, new_row_df], ignore_index=True)
    st.write("Fila agregada exitosamente.")
    st.dataframe(edited_df)  # Mostrar el DataFrame actualizado

# Seleccionar filas para eliminar
st.write("Eliminar filas:")
rows_to_delete = st.multiselect('Selecciona las filas a eliminar', edited_df.index)

if st.button('Eliminar filas'):
    edited_df = edited_df.drop(rows_to_delete)
    st.write("Filas eliminadas exitosamente.")
    st.dataframe(edited_df)  # Mostrar el DataFrame actualizado

# Guardar el DataFrame editado en la base de datos SQLite
if st.button('Guardar cambios'):
    try:
        # Verificar que el DataFrame editado esté en el formato correcto
        if isinstance(edited_df, pd.DataFrame):
            edited_df.to_sql('people', conn, if_exists='replace', index=False)
            st.write("Cambios guardados exitosamente.")
        else:
            st.write("Error: El DataFrame editado no está en el formato correcto.")
    except Exception as e:
        st.write(f"Error al guardar los cambios: {e}")

# Cerrar la conexión
conn.close()
