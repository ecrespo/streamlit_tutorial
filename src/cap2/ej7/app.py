import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(data={
    'Name': ['Jessica','John','Alex'],
    'Score 1': [77,56,89],
    'Score 2': [88,78,90]
})

df.set_index('Name').plot(kind='bar',stacked=False,xlabel='Name',ylabel='Score',title='Scores')

st.pyplot(plt)

