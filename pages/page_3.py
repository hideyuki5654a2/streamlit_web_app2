import streamlit as st
import pandas as pd

#データ分析関連
df=pd.read_csv('./data/weather.csv',index_col='年月日',encoding='shift_jis')
st.dataframe(df)
#st.table(df)
st.line_chart(df)
st.bar_chart(df)