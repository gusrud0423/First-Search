import streamlit as st

import pandas as pd

def main() :
    df = pd.read_csv('data/iris.csv')

    #st.dataframe( df )  # 스크롤 있음

    #st.dataframe( df.style.highlight_max(axis = 0) )  # 각 컬럼의 맥스 값에 하이라이트를 준다(노란색으로 표시)

    # st.table(df)      # 스크롤이 없음 판으로 보여짐 

    # st.table( df.head() )  # 이렇게 하면 상위 5개만 보임

    # st.write( df.head() )  # 컬럼들도 클릭 가능 


if __name__ == '__main__' :
   main()    


