import streamlit as st
import pandas as pd
import numpy as np

np.random.seed(0)

df = pd.DataFrame(np.random.randn(4,3),columns=('Column 1','Column 2','Column 3'))

st.subheader('Original dataframe')

st.write(df)

df = df[df['Column 1']> 1]

df= df[['Column 1','Column 2']]
df = df.sort_values(by='Column 2',ascending=False)
st.subheader('Mutated dataframe')
st.write(df)

df = df.assign(Column_4= lambda x: df['Column 1']*2)
st.subheader('Mutated2 dataframe')
st.write(df)
