import streamlit as st
import pandas as pd
df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})
dg=pd.DataFrame({
    'Girls':['mya','hla','oo'],
    'Boys':['Kaung','Min','Thant']
})
df
dg
st.title("Hello!!")