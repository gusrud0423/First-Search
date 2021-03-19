import streamlit as st
import pandas as pd


def run_eda_app()  :

    st.subheader( 'EDA 화면 입니다' )   # app6 에서 이걸 가져다가 쓸것이다
    st.write('다른 파일에서 불러온것이다')

    df =  pd.read_csv('data/iris.csv')

    st.dataframe(df)
