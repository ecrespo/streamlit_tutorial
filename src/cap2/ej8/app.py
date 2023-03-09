import streamlit as st
import pandas as pd
import matplotlib.pyplot as fig


df = pd.DataFrame(data={
    'Exam': ['First','Second','Third'],
    'Jessica': [77,56,89],
    'John': [88,78,90],
    'Alex': [90,80,95]
})

df.set_index('Exam').plot(kind='line',xlabel='Exam',ylabel='Score',subplots=True,title='Scores')

st.pyplot(fig)
