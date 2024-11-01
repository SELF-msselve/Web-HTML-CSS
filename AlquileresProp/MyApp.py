import streamlit as st
import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

st.set_page_config(
    page_title="SELF Propiedades",  # Título de la pestaña del navegador
    page_icon=":smiley:",  # Icono de la pestaña del navegador (puede ser un emoji o una ruta a una imagen)
    layout="centered",  # Otras opciones son 'centered'
    initial_sidebar_state="collapsed", # Estado inicial de la barra lateral ('collapsed' o 'expanded'))
)

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
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#df = pd.read_excel('https://raw.githubusercontent.com/SELF-msselve/Web-HTML-CSS/main/AlquileresProp/prop2.xlsx')
df = pd.read_excel('prop2.xlsx')
encabezados = list(df.columns)
vence_un_mes = []
vence_dos_meses = []

one_month = date.today() + relativedelta(months=+1)
two_month = date.today() + relativedelta(months=+2)

menu = ['Alquileres', 'Actualizaciones']

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

for index, row in df.iterrows():
    for items in row:
        if is_date(items):
            if items.year == one_month.year and items.month == one_month.month:
                vence_un_mes.append(row[1])
            if items.year == two_month.year and items.month == two_month.month:
                vence_dos_meses.append(row[1])                

df_un_mes = pd.DataFrame(vence_un_mes)
df_dos_meses = pd.DataFrame(vence_dos_meses)

def pagina_1():
    # Contenido de la aplicación
    st.title(':violet[SELF] Propiedades')
    #st.sidebar.title("Menú Lateral")
    st.write('*Tocar la direccion para desplegar Info*')
    #st.write("***Hello***, *World!* :sunglasses:")

    df_columns = df.columns
    for index, row in df.iterrows():
        my_expander = st.expander(row['Direccion'], expanded=False)
        with my_expander:
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
    # Contenido de la aplicación
    st.title(':violet[SELF] Propiedades')
    st.write('*Tocar la direccion para desplegar Info*')
    
    st.title('Vence en 1 mes')
    st.write(df_un_mes.to_html(index=False, header=False), unsafe_allow_html=True)
    
    st.title('Vence en 2 meses')
    st.write(df_dos_meses.to_html(index=False, header=False), unsafe_allow_html=True)
    
st.sidebar.title('Menú Lateral')
# Configurar la barra lateral
page = st.sidebar.selectbox('Elige una página', menu)

# Mostrar contenido basado en la página seleccionada
if page == menu[0]:
    pagina_1()
elif page == menu[1]:
    pagina_2()


