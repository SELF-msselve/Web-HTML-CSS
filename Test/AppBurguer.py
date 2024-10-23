import streamlit as st

st.set_page_config(
    page_title='My App',
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={'Get Help': 'https://dbdmg.polito.it/',
                'Report a bug': 'https://dbdmg.polito.it/',
                'About': '# *Introduction to Database* Course'}
)

st.title('Streamlit :red[Tutorial]')
st.header(':blue[Introduction to Data Bases]')
st.subheader('Web Application')
st.text('My Second Web Apllication')

db_list=['Oracle', 'MySQL', 'PostgresSQL', 'MongoDB', 'InfluxDB']


    
if st.checkbox('Accept the conditions'):
    st.write('Thanks for accepting me!')
else:
    st.write('Please, accept me.')


widget = st.radio('Which widget you prefere', ['Button', 'Checkbox'])

st.write('Here is your Widget')

if widget == 'Button':
    if st.button('Show', type='primary'):
        st.write(db_list)
else:
    if st.checkbox('Show'):
        pass
    
option=st.selectbox('Choose a Data Base to connect', db_list)

st.write(option)