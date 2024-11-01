import streamlit as st
import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
 
df = pd.read_excel('prop2.xlsx')

def is_date(variable):
    if isinstance(variable, datetime):
        return True
    elif isinstance(variable, str):
        try:
            datetime.strptime(variable, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    else:
        return False



# Definir las funciones para cada página
def pagina_1():
    # Contenido de la aplicación
    st.title(':violet[SELF] Propiedades')
    #st.sidebar.title("Menú Lateral")
    st.write('*Tocar la direccion para desplegar Info*')
    #st.write("***Hello***, *World!* :sunglasses:")

    one_month = date.today() + relativedelta(months=+1)
    two_month = date.today() + relativedelta(months=+2)

    df_columns = df.columns
    for index, row in df.iterrows():
        my_expander = st.expander(row['Direccion'], expanded=False)
        with my_expander:
            #col1, col2 = st.columns([1,1])
            contador = 0
            for items in row:
                if is_date(items):
                    if items.year == one_month.year and items.month == one_month.month:
                        st.write(':red[**Vence el mes que viene**] :sunglasses:')
                    if items.year == two_month.year and items.month == two_month.month:
                        st.write(':orange[**Vence en dos meses**]')                
                    st.write(df_columns[contador], ': ', items.strftime('%m/%Y'))
                else:
                    st.write(df_columns[contador], ': ', items)
                contador += 1

def pagina_2():
    st.title("Página 2")
    st.write("Bienvenido a la Página 2")
    st.write("Este es un texto de ejemplo en la Página 2")

def pagina_3():
    st.title("Página 3")
    st.write("Bienvenido a la Página 3")
    if st.button('Presiona este botón'):
        st.write('¡Botón presionado!')

# Configurar la barra lateral para seleccionar la página
page = st.sidebar.selectbox("Elige una página", ["Página 1", "Página 2", "Página 3"])

# Mostrar el contenido basado en la página seleccionada
if page == "Página 1":
    pagina_1()
elif page == "Página 2":
    pagina_2()
elif page == "Página 3":
    pagina_3()
