#!/usr/bin/env python

import streamlit as st

with st.form('feedback_form'):
    st.header('Feedback form')

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input('Please enter your name')
        rating = st.slider('Please rating this app',0,10,5)

    with col2:
        dob = st.date_input('Please enter your date birth')
        recommend = st.radio('Would you recommend this app to others?',('Yes','No'))

    submited = st.form_submit_button('Submit')

    if submited:
        st.write('**Name**', name, '**Date of birth**',dob,'**Rating**:',rating,'**Would recommend?:**',recommend)
