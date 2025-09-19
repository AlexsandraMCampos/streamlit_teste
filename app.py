# importar o streamlit como o comando: pip intall streamlit
#  python  -m streamlit run app.py
import streamlit as st

# tab= abas
tab1, tab2 = st.tabs(['Elementos de texto', 'Outros Elementos'])

with tab1:
    st.write('Olá Mundo')
    st.title('Título')
    st.header('Header')
    st.subheader('Subheader')
    st.markdown('# Título 1')
    st.markdown('## Título 2')
    st.markdown('### Título 3')
    st.markdown('#### Título 4')
    st.markdown('##### Título 5')
    st.markdown('---')
    st.markdown('**negrito** sem negrito')
    st.markdown("""
    Lista:
    - Item 1
    - Item 2
    """)

    st.markdown("""
    Código cru:
                
    ```bash
                print(Ola Mundo)
    ```
                """)
    codigo = 'print(Olá mundo)'

    st.code(codigo)
   
with tab2:
    animais = ['gato','cachorro','coelho']
    animal =st.selectbox('Escolha o animal', animais) # selectbox tem o papel de input
    st.write(f'O animal esolhido foi {animal}.')
    st.image(f'{animal}.jpg', width=300)
    if animal == 'gato':
        st.video('https://www.youtube.com/shorts/MqppCgaND68')
    elif animal == "cachorro":
        st.video('https://www.youtube.com/shorts/jXWElQaC-RA')
    elif animal == 'coelho':
        st.video('https://www.youtube.com/shorts/9NQYHWO7K2E')

    