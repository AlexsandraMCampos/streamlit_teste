import streamlit as st

# ---------------------------------SIDEBAR
st.sidebar.title('Calculadora de IMC')

nome = st.sidebar.text_input('Nome: ')
peso = st.sidebar.text_input('Peso: ')
altura= st.sidebar.text_input('Altura: ')








#--------------------------------------BODY
st.title('Calculadora de IMC')

if st.sidebar.button('Calcular'): # após o botão ser clicado, fazemos as conversoes das strings para float e fazermos o calculo
    peso= float(peso)
    altura= float(altura)
    imc= peso/(altura**2)
    st.write(f'Seu IMC é: {imc:.2f}')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('Nome', nome)
    with col2:
        st.metric('Peso', peso)
    with col3:
        st.metric('Altura', altura)
    if imc <= 18.5:
        st.error(f'Seu IMC é {imc:.2f}! Você está abaixo do peso.')
    elif imc <= 24.9:
        st.title(f'Seu imc é {imc:.2f}. Você está no peso ideal.')
    elif imc <= 29.9:
        st.warning(f'Seu IMC é {imc:.2f}. Você está acima do peso!')
    elif imc <= 34.9:
        st.warning(f'Seu IMC é {imc:.2f}! VocÊ está em Obsidade grau I')
    elif imc <= 39.9:
        st.error(f'Seu IMC é {imc:.2f}! VocÊ está em Obsidade grau II')
    else:
        st.warning(f'Seu IMC é {imc:.2f}! VocÊ está em Obsidade grau III (Morbida)')