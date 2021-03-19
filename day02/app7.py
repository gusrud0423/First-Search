# 차트 그리는 법

import streamlit as st


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  
import matplotlib
matplotlib.use('Agg')  # 서버에서, 화면에 표시하기 위해서 필요
import seaborn as sns

def main() :
    st.title('Plotting with st.pyplot()')

    df =  pd.read_csv('data/iris.csv')
    st.dataframe( df.head() )

    # plt.scatter(data=  df, x= 'sepal_length', y= 'sepal_width')
    # plt.show()  # 이렇게 쓰면 백엔드서버에서 돌고 있는거라 안된다
    fig = plt.figure()  # 차트영역 먼저 가져와라
    plt.scatter(data=df, x= 'sepal_length', y= 'sepal_width')
    plt.xlabel('sepal_length')
    plt.ylabel('sepal_width')
    plt.title('sepal_length vs width')
    
    st.pyplot(fig)  # 스트림릿아 이 차트좀 보여줘라  
    # 우리가 아는것 다쓴거고 변한건 이것 밖에 없어

    
    
    # x 축에 sepal_length 로 히스토그램을 그려주세요
    fig2 = plt.figure()
    plt.hist(data= df, x= 'sepal_length', bins = 30) # 이게 fig2의 영역
    st.pyplot(fig2)

   # 서브플롯! : 차트 여러개 한번에 
   # 위에 차트를 하나는 빈즈가 20, 40 개짜리 1행 2열로 만들기

    fig3 = plt.figure()
    plt.subplot(1,2,1) # 1행 2열의 첫번째 
    plt.hist( data=df, x='sepal_length', bins= 20 )
    plt.subplot(1,2,2)
    plt.hist(data=df, x='sepal_length', bins= 40)
    st.pyplot(fig3)

   # 컬럼 species 의 데이터를 몇개씩 있는지 
    fig4 = plt.figure()
    sns.countplot(data= df, x='species')
    st.pyplot(fig4)          #이거 확인해봐 오류

    fig5 = plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig5)


if __name__ == '__main__' :
    main()    

    
    
    
    
    # 라이브러리 설치 했는지 확인 
    # cls 치고 해오던 디렉토리에서 나가서

    # conda install matplotlib 을 쳐보면 packages already installed. 해봐야함
    # 경로 맨끝에 python 을 치면 파이썬 환경에서 확인할수 있다
    #그래서 거기다가  import matplotlib.pyplot as plt 쳐서 확인해보기

    # 이래도 없으면 껏다 켯다가 그래도 안되면 명령 프롬프트 켜서 
    #pip install mat ~~ 하기