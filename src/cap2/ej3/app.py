import streamlit as st

col1, col2 = st.columns(2)

with col1:
    number1 = st.number_input("Please enter the first number",value=1,step=1)
with col2:
    number2 = st.number_input("Please enter the second number",value=0,step=1)


try:
    st.info(f'**{number1}/{number2}=**{number1/number2}')
except Exception as e:
    st.error(f'Error: {e}')