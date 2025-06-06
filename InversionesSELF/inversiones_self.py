import pandas as pd
import streamlit as st

st.title('SELF Inversiones ON')

df_raw = pd.read_excel('inversiones.xlsx', sheet_name='TABLA')

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

# Menú inicial
menu = st.sidebar.selectbox('Opciones', ['Intereses Mensuales', 'Intereses Anuales', 'Intereses x Empresa x Mes', 'Intereses mensuales por empresa', 'Capital por empresa'])

if menu == 'Intereses Mensuales':
    st.write('### Intereses Mensuales.')
    st.markdown(f'<div style="display:flex;justify-content:center;height:400px;overflow:auto;margin-bottom:20px;"><div style="width:80%;">{df_sum_mes.to_html(index=False)}</div></div>', unsafe_allow_html=True)
   
elif menu == 'Intereses Anuales':
    st.write('### Intereses Anuales.')
    st.markdown(f'<div style="display:flex;justify-content:center;height:400px;overflow:auto;margin-bottom:20px;"><div style="width:80%;">{df_sum_year.to_html(index=False)}</div></div>', unsafe_allow_html=True)

elif menu == 'Intereses x Empresa x Mes':
    st.write('### Intereses x Empresa x Mes.')
    st.markdown(f'<div style="display:flex;justify-content:center;height:400px;overflow:auto;margin-bottom:20px;"><div style="width:80%;">{df_sum_empresa.to_html(index=False)}</div></div>', unsafe_allow_html=True)

elif menu == 'Intereses mensuales por empresa':
    # Lista de marcas disponibles
    marcas = df['EMPRESA'].unique()

    # Selección de marca por el usuario
    marca_seleccionada = st.selectbox('Elige una Empresa', marcas)

    # Filtrar el DataFrame por la marca seleccionada
    df_filtrado = df_sum_empresa[df_sum_empresa['EMPRESA'] == marca_seleccionada]

    # Mostrar los valores mensuales de la marca seleccionada sin índice y con scroll
    st.write(f"### Intereses mensuales para la Empresa: {marca_seleccionada}")
    st.markdown(f'<div style="display:flex;justify-content:center;height:400px;overflow:auto;margin-bottom:20px;"><div style="width:80%;">{df_filtrado.to_html(index=False)}</div></div>', unsafe_allow_html=True)

elif menu == 'Capital por empresa':
    st.write("### Empresas y Capital Invertido:")
    st.markdown(f'<div style="display:flex;justify-content:center;height:400px;overflow:auto;margin-bottom:20px;"><div style="width:80%;">{df_empresas_capital.to_html(index=False)}</div></div>', unsafe_allow_html=True)
    
    # Mostrar el total de CAPEX formateado con separadores de miles
    st.write(f"### Total CAPEX: {total_capex:,.0f}")



