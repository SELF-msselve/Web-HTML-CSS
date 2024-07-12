import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Datos de ejemplo
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie', 'David'],
    'Edad': [24, 27, 22, 32],
    'Ciudad': ['Nueva York', 'Los Ángeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# # Configura tus credenciales de la base de datos
# host = 'mysql-eduardofarina-self-01.a.aivencloud.com:27648'
# usuario = 'avnadmin'
# contraseña = 'AVNS_EFCz8BR33pf0DTARSKL'
# base_de_datos = 'self-properties'

# # Crea una cadena de conexión SQLAlchemy
# cadena_conexion = f"mysql+mysqlconnector://{usuario}:{contraseña}@{host}/{base_de_datos}"

# # Crea una conexión a la base de datos
# engine = create_engine(cadena_conexion)

# # Consulta SQL para obtener los datos (reemplaza con tu consulta)
# nombre_tabla = 'propiedades'
# consulta_sql = f"SELECT * FROM {nombre_tabla}"

# # Carga los datos en un DataFrame de pandas
# df_global = pd.read_sql(consulta_sql, engine)
# df_global.Pagos=df_global.Pagos.astype(int)
# df_global.Pagos=df_global.Pagos.astype(bool)


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
    

def my_widget(key):
    st.subheader('Hello there!')
    return st.button("Click me " + key)

# This works in the main area
clicked = my_widget("first")

# And within an expander
my_expander = st.expander("Expand", expanded=True)
with my_expander:
    clicked = my_widget("second")

for index, row in df.iterrows():
    my_expander = st.expander(row['Nombre'], expanded=False)
    with my_expander:
        for items in row:
            st.write(items)

        # st.write(row['Nombre'])
        # st.write(row['Edad'])
        # st.write(row['Ciudad'])
        
    

# AND in st.sidebar!
# with st.sidebar:
#     clicked = my_widget("third")

