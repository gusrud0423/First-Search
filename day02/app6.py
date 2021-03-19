import streamlit as st

from eda_app import run_eda_app

from  ml_app  import  run_ml_app

def main() :
    st.title('파일 분리 앱')

    menu = ['Home', 'EDA', 'ML', 'About']  # EDA는 차트 같은,ML 은 머신러닝
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home' :
        st.subheader( '홈 화면 입니다' )
    
    elif choice == 'EDA' :

        #st.subheader( 'EDA 화면 입니다' )
        run_eda_app()  # 라인 3에서 run_eda_app를 불러왔는데 
                       #이건 eda_app 에있는 자료를 불러올수 잇게 한것이다

    elif choice == 'ML' :
        #st.subheader( 'ML 화면 입니다' ) 
        run_ml_app() 
    
    elif choice == 'About' :
        st.subheader( 'About 화면 입니다' )    
    else :
        st.subheader( '프로젝트 소개 화면 입니다' )                      


################### 여기 오류 나 


if __name__ == "__main__" :
    main()