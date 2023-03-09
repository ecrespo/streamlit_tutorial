#!/usr/bin/env python

import streamlit as st
import pandas as pd

df1 = pd.DataFrame(data={
    'Name': ['Jessica','John','Alex'],
    'Score 1': [77,56,89]
})

df2 = pd.DataFrame(data={
    'Name': ['Jessica','John','Alex'],
    'Score 2': [76,97,82]
})

st.subheader('Original dataframe')
st.write(df1)
st.write(df2)

df1 = df1.merge(df2,how='inner',on='Name')
st.subheader('Mutated dataframe')
st.write(df1)
