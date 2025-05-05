import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="SELF Inversiones ON",  # Título de la pestaña del navegador
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

/* Asegúrate de que la página esté bien escalada en dispositivos móviles
@media only screen and (max-width: 600px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}  */

/* Agrandar el tamaño de la letra en st.dataframe */
div[data-testid="stDataFrame"] {
    font-size: 50px; */

</style>
""" 
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


df_raw = pd.read_excel('https://raw.githubusercontent.com/SELF-msselve/Web-HTML-CSS/main/InversionesSELF/Inversiones.xlsx', sheet_name='TABLA')

#df_raw = pd.read_excel('inversiones.xlsx', sheet_name='TABLA')

df_raw['FECHA'] = pd.to_datetime(df_raw['FECHA'], format='%d/%m/%Y')

fecha_filtro = '2029-01-01'
df = df_raw[df_raw['FECHA'] < fecha_filtro]

df['MES'] = df['FECHA'].dt.to_period('M')
df['YEAR'] = df['FECHA'].dt.to_period('Y')

df_sum_mes = df.groupby(['MES'])['INTERES'].sum().reset_index()
df_sum_year = df.groupby(['YEAR'])['INTERES'].sum().reset_index()
df_sum_empresa = df.groupby(['MES', 'EMPRESA'])['INTERES'].sum().reset_index()

df_sum_mes['INTERES'] = df_sum_mes['INTERES'].apply(lambda x: f"{x:,.0f}")
df_sum_year['INTERES'] = df_sum_year['INTERES'].apply(lambda x: f"{x:,.0f}")
df_sum_empresa['INTERES'] = df_sum_empresa['INTERES'].apply(lambda x: f"{x:,.0f}")

# Obtener el DataFrame de empresas y capital
df_empresas_capital = df[['EMPRESA', 'CAPEX']].drop_duplicates().reset_index(drop=True)
df_empresas_capital['CAPEX'] = df_empresas_capital['CAPEX'].apply(lambda x: f"{x:,.0f}")

# Calcular el total de CAPEX
total_capex = df_empresas_capital['CAPEX'].apply(lambda x: int(x.replace(',', ''))).sum()

st.title(':violet[SELF] Inversiones ON')

# Menú inicial en el encabezado
menu = st.selectbox('Opciones', ['Intereses Mensuales', 'Intereses Anuales', 'Intereses x Empresa x Mes', 'Intereses mensuales por empresa', 'Capital por empresa'])

if menu == 'Intereses Mensuales':
    st.write('### Intereses Mensuales.')
    #st.markdown(f'<div style="display:flex;justify-content:center;height:400px;overflow:auto;margin-bottom:20px;"><div style="width:90%;">{df_sum_mes.to_html(index=False)}</div></div>', unsafe_allow_html=True)
    #st.markdown(df_sum_mes.to_html(index=False), unsafe_allow_html=True)
    #st.table(df_sum_mes)
    st.dataframe(
        df_sum_mes,
        width=30, height=300, use_container_width=True,
        column_config={
            "INTERES": st.column_config.NumberColumn(
                "Interes ($)",
                help="Intereses ganados en el mes",
                format="$%d",
            )
        })
    
elif menu == 'Intereses Anuales':
    st.write('### Intereses Anuales.')
    #st.markdown(f'<div style="display:flex;justify-content:center;height:400px;overflow:auto;margin-bottom:20px;"><div style="width:90%;">{df_sum_year.to_html(index=False)}</div></div>', unsafe_allow_html=True)
    st.data_editor(df_sum_year)
    #st.dataframe(df_sum_year)
    
elif menu == 'Intereses x Empresa x Mes':
    st.write('### Intereses x Empresa x Mes.')
    #st.markdown(f'<div style="display:flex;justify-content:center;height:400px;overflow:auto;margin-bottom:20px;"><div style="width:90%;">{df_sum_empresa.to_html(index=False)}</div></div>', unsafe_allow_html=True)
    st.dataframe(df_sum_empresa)
    
elif menu == 'Intereses mensuales por empresa':
    # Lista de marcas disponibles
    marcas = df['EMPRESA'].unique()

    # Selección de marca por el usuario
    marca_seleccionada = st.selectbox('Elige una Empresa', marcas)

    # Filtrar el DataFrame por la marca seleccionada
    df_filtrado = df_sum_empresa[df_sum_empresa['EMPRESA'] == marca_seleccionada]

    # Mostrar los valores mensuales de la marca seleccionada sin índice y con scroll
    st.write(f"### Intereses mensuales para la Empresa: {marca_seleccionada}")
    #st.markdown(f'<div style="display:flex;justify-content:center;height:400px;overflow:auto;margin-bottom:20px;"><div style="width:90%;">{df_filtrado.to_html(index=False)}</div></div>', unsafe_allow_html=True)
    st.dataframe(df_filtrado)
elif menu == 'Capital por empresa':
    st.write("### Empresas y Capital Invertido:")
    #st.markdown(f'<div style="display:flex;justify-content:center;height:400px;overflow:auto;margin-bottom:20px;"><div style="width:90%;">{df_empresas_capital.to_html(index=False)}</div></div>', unsafe_allow_html=True)
    st.dataframe(df_empresas_capital)
    
    # Mostrar el total de CAPEX formateado con separadores de miles
    st.write(f"### Total CAPEX: {total_capex:,.0f}")
