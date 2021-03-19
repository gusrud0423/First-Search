import  streamlit as st

import numpy as np
import pandas as pd

import altair as alt
import plotly.express as px 
# https://plotly.com/python/

# https://altair-viz.github.io   여기 참고!!!!!!!

def main() :
    df1 =  pd.read_csv('data/lang_data.csv')
    st.dataframe(df1)


    # 언어별로 선택하면 차트 만들수 있게 언어 선택창 만들기
    lang_list = df1.columns.tolist() # 컬럼을 리스트로 
    print(lang_list)

    lang_list =  lang_list[ 1: ] # week는 필요없어서 슬라이싱 함
    
    
    selected_lang_list = st.multiselect('언어를 선택하시오', lang_list)
    print(selected_lang_list)

    if len(selected_lang_list) != 0 :
    # 셀렉티드 리스트가 0과 같지 않다면??  ==  비어있지 않으면 
    #   > 0 , !=0 이것도 가능 


        # 유저가 선택한 언어만, 또는 여러개의 언어 차트를 그리려고 한다 
        df_selected = df1[ selected_lang_list ]

        #st.dataframe(df_seleted)

        st.line_chart(df_selected)  # 선으로 보여달라

        st.area_chart(df_selected)   # 영역을 칠해서 보여달라
    

    
    
    
    
    
    
        st.write('새로운 영역')       

        df2 =  pd.read_csv('data/iris.csv')

        st.dataframe(df2.head())

        st.bar_chart(df2[ ['sepal_length', 'petal_length'] ])  

    # Altair 이용하면 , 뭐가 좋냐?
    # x 축 , y 축 설정 + color 또는 size 까지 표현 가능

    #1. 차트를 그릴 변수를 지정~~~
        chart = alt.Chart(df2).mark_circle().encode(
        x = 'petal_length',
        y = 'petal_width',
        color =  'species'
        )
        st.altair_chart(chart, use_container_width= True)
                            # 화면에 맞게 더 크게 보여줌  st ~~ 여기에 다쓸수 있음
  
    
    
    #  위도 경도를 가지고 지도 찍기
        df3 =  pd.read_csv('data/location.csv', index_col = 0)
        st.dataframe(df3)  # zoom 쓰면 땡겨짐

        st.map(data=  df3)


        df4 = pd.read_csv('data/prog_languages_data.csv', index_col= 0)
                                                          # 인덱스 0번에 있던것을 인덱스번호 자체로 
        st.dataframe(df4)

        fig1 =  px.pie( 
            df4,
            values = 'Sum',
            names = 'lang',
            title = 'Pie Chart of Languages'
         )
        st.plotly_chart(fig1)  # 내가 원하는것만 선택해서 볼수 있음 


        fig2 = px.bar( 
            df4,
            x = 'lang',
            y = 'Sum'
         )
        st.plotly_chart(fig2)   # 이거 차트가 나오는데 확대해서 마우스 움직여서 원하는 부분 확대해서 볼수 있음 

    










if __name__ == '__main__' :
    main()

