import streamlit as st
import pandas as pd

df = pd.read_excel('https://raw.githubusercontent.com/SELF-msselve/Web-HTML-CSS/main/AlquileresProp/prop.xlsx')
#df = pd.read_excel('prop.xlsx')

# Aplicación Streamlit
#st.title('SELF Propiedades')
#st.sidebar.title('Propiedades')
    
# Barra lateral con menú desplegable
selected_value = st.sidebar.selectbox('Selecciona Propiedad:', df['Direccion'])

# Filtra el DataFrame según el valor seleccionado
selected_row = df[df['Direccion'] == selected_value]

# Muestra la fila seleccionada como una tabla
st.write('Propiedad Seleccionada')

for index, row in selected_row.iterrows():
    for texto in row:
        st.text(texto)
    
