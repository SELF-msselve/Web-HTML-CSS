import streamlit as st
import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
 
df = pd.read_excel('https://raw.githubusercontent.com/SELF-msselve/Web-HTML-CSS/main/AlquileresProp/prop2.xlsx')
#df = pd.read_excel('prop2.xlsx')
#print(df)
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


st.markdown(hide_streamlit_style, unsafe_allow_html=True)

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


