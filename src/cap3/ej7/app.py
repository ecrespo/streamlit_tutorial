import streamlit as st
import wget

progress_text = st.empty()
progress_bar = st.progress(0)

def streamlit_progress_bar(current,total,width):
    percent = int((current/total)*100)
    progress_text.subheader('Progress: {}%'.format(percent))
    progress_bar.progress(percent)

file_url = 'https://download.documentfoundation.org/libreoffice/stable/7.5.1/rpm/x86_64/LibreOffice_7.5.1_Linux_x86-64_rpm.tar.gz'

wget.download(file_url, bar=streamlit_progress_bar)