import pandas as pd
import streamlit as st


st.set_page_config(
  page_title="SELF Inversiones ON",
  page_icon=":smiley:",
  layout="centered",
  initial_sidebar_state="collapsed",
)

# CSS para ocultar la barra de navegación y el cartel de "Manage App" y aumentar el tamaño de la letra en st.selectbox
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stApp {
   top: 0px;
   padding-top: 0px;
   margin-top: 0px;
}

/* Asegúrate de que la página esté bien escalada en dispositivos móviles */
@media only screen and (max-width: 600px) {
   .block-container {
      padding-left: 1rem;
      padding-right: 1rem;
   }
}

/* Ocultar barra de navegación en Safari */
::-webkit-scrollbar {
   display: none;
}
</style>
""" 

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#df_raw = pd.read_excel('https://raw.githubusercontent.com/SELF-msselve/Web-HTML-CSS/main/InversionesSELF/Inversiones.xlsx', sheet_name='TABLA')

df_raw = pd.read_excel('inversiones.xlsx', sheet_name='TABLA')

df_raw['FECHA'] = pd.to_datetime(df_raw['FECHA'], format='%d/%m/%Y')

fecha_filtro = '2029-01-01'
df = df_raw[df_raw['FECHA'] < fecha_filtro]

df.loc[:,'MES'] = df['FECHA'].dt.to_period('M')
df.loc[:,'YEAR'] = df['FECHA'].dt.to_period('Y')

df_sum_mes = df.groupby(['MES'])['INTERES'].sum().reset_index()
df_sum_year = df.groupby(['YEAR'])['INTERES'].sum().reset_index()
df_sum_empresa = df.groupby(['MES', 'EMPRESA'])['INTERES'].sum().reset_index()

df_sum_mes['INTERES'] = df_sum_mes['INTERES'].apply(lambda x: f"{x:,.0f}")
df_sum_year['INTERES'] = df_sum_year['INTERES'].apply(lambda x: f"{x:,.0f}")
df_sum_empresa['INTERES'] = df_sum_empresa['INTERES'].apply(lambda x: f"{x:,.0f}")

# Obtener el DataFrame de empresas y capital
df_empresas_capital = df[['EMPRESA', 'CAPEX']].drop_duplicates().reset_index(drop=True)
df_empresas_capital['CAPEX'] = df_empresas_capital['CAPEX'].apply(lambda x: f"{x:,.0f}")

df_detalle = df[['EMPRESA', 'FECHA', 'INTERES', 'PAGO']].sort_values(by='FECHA')
df_detalle['FECHA'] = df_detalle['FECHA'].dt.strftime('%d/%m/%Y')

# Calcular el total de CAPEX
total_capex = df_empresas_capital['CAPEX'].apply(lambda x: int(x.replace(',', ''))).sum()

st.title(':violet[SELF] ON Invest')
st.divider()
##st.header('*Tocar la direccion para desplegar Info*')
st.write('### Intereses Mensuales.')
st.dataframe(df_sum_mes)
st.divider()    
st.write('### Intereses Anuales.')
st.dataframe(df_sum_year)
st.divider()    
st.write('### Intereses x Empresa x Mes.')
st.dataframe(df_sum_empresa)
st.divider()    
marcas = df['EMPRESA'].unique()

# Selección de marca por el usuario
marca_seleccionada = st.selectbox('Elige una Empresa', marcas)

# Filtrar el DataFrame por la marca seleccionada
df_filtrado = df_sum_empresa[df_sum_empresa['EMPRESA'] == marca_seleccionada]

# Mostrar los valores mensuales de la marca seleccionada sin índice y con scroll
st.write(f"### Intereses mensuales para la Empresa: {marca_seleccionada}")
#st.markdown(f'<div style="display:flex;justify-content:center;height:400px;overflow:auto;margin-bottom:20px;"><div style="width:90%;">{df_filtrado.to_html(index=False)}</div></div>', unsafe_allow_html=True)
st.dataframe(df_filtrado)

st.divider()    
st.write("### Empresas y Capital Invertido:")
st.dataframe(df_empresas_capital)
    
# Mostrar el total de CAPEX formateado con separadores de miles
st.write(f"### Total CAPEX: {total_capex:,.0f}")
st.divider()    
st.write("### Fechas de Pago:")
st.dataframe(df_detalle)
