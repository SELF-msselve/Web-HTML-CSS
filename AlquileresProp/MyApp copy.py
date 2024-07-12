import streamlit as st
import pandas as pd

st.set_page_config(
     page_title='Streamlit cheat sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)

st.write("""
# My first app
Hello *world!*
""")

st.title('Hello GeekFolks')
 
df = pd.read_csv('https://raw.githubusercontent.com/SELF-msselve/Web-HTML-CSS/main/AlquileresProp/prop.csv')
#st.line_chart(df)
df2 = df.loc[:,['Direccion','Lugar']]
st.write(df2.style.hide())

# Text Input
 
# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input('', "Type Here ...")
 
# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
    result = name.title()
    st.success(result)
    df.loc[0:0,'Direccion'] = result
    df.to_csv('https://raw.githubusercontent.com/SELF-msselve/Web-HTML-CSS/main/AlquileresProp/prop_2.csv')

# Selection box
 
# first argument takes the titleof the selectionbox
# second argument takes options
hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])
 
# print the selected hobby
st.write("Your hobby is: ", hobby)

# cols = st.columns(4)

# for index, row in df.iterrows():
#     cols = st.columns(4)
#     cols[0].success(row.Direccion)
#     cols[1].success(row.UF)

# import streamlit as st
# import pandas as pd

# def display_dataframe(df):
#     """
#     Muestra las columnas y filas de un dataframe utilizando Streamlit.
#     Args:
#         df (pd.DataFrame): El dataframe de entrada.
#     """
#     st.write("## Vista previa del DataFrame")
#     st.write(f"Número de filas: {df.shape[0]}")
#     st.write(f"Número de columnas: {df.shape[1]}")

#     # Muestra las columnas
#     st.write("### Columnas:")
#     st.write(df.columns.tolist())

#     # Muestra las primeras filas del dataframe
#     st.write("### Datos de ejemplo:")
#     st.write(df.head())

# def main():
#     st.title("Visor de DataFrame")

#     # Carga tu dataframe aquí (reemplaza con tus propios datos)
#     # Ejemplo: df = pd.read_csv("tu_archivo.csv")
#     df = pd.DataFrame({
#         "Columna1": [1, 2, 3],
#         "Columna2": ["A", "B", "C"],
#         "Columna3": [10.5, 20.3, 15.7],
#         "Columna4": [45, 12, 56],
#     })

#     display_dataframe(df)

# if __name__ == "__main__":
#     main()