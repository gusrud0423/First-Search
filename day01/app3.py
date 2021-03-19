import streamlit as st
import pandas as pd

def main() :
    
    
    
    # name ='Han'  # 이런 조건은 위에 있어야 해
    # if st.button('이름 확인') :
    #     #st.write('당신의 이름은 {}입니다'.format(name)) 
    #     st.write( name.upper() ) # 영어이름 일때 대문자로
    
    # if st.button('이름 확인', key= 'btn2') : # 버튼2 생성해서 버튼을 키로 구별한다
    #     #st.write('안녕하세요')
    #     st.write(name.lower())  # 영어이름 일때 소문자로 
    
    df = pd.read_csv('data/iris.csv')  # 데이터 프레임 가져올땐 미리 읽고 시작해야한다
    
    status = st.radio('정렬을 선택하세요', ['오름차순', '내림차순'])   # 버튼 누르면 오름차순 문자열이 입력, 내림차순 버튼을 누르면 내림차순 문자열이 입력
    if status == '오름차순' :
        st.dataframe( df.sort_values( by= 'sepal_length') )  # df의 sepal_length 기준으로 전부 오름차순으로 정렬
        #st.write('오름차순 눌렀어요')  
    elif status == '내림차순' :
        #st.write('내림차순 눌렀어요') 
        st.dataframe( df.sort_values( by= 'sepal_length', ascending=  False) )   

    if st.checkbox('show/hide') :
        st.text('뭔가 하겠다')  # 체크 했을 때의 액션을 써주면 됨

    
    
    lang = ['python', 'java', 'c', 'go']
    selected_lang =st.selectbox('언어 선택하세요', lang)  # 어떤 언어를 사용할지 선택할수 있음

    #st.write(selected_lang) # 언어 선택했을 때 액션을 씀
    st.write('당신이 선택한 언어는 {}입니다'.format(selected_lang) )

    lang_list = st.multiselect('언어를 선택하세요', lang)  # 여러개를 선택할수 있음
    print(lang_list)  # 프린트는 개발자가 디버깅용으로 터미널 이용해서 볼수 있게 한다   
                      # 스트림릿페이지 에서 여러개 선택 했던것을 뭐 선택했는지 리스트로 보여준다 ['go', 'java', 'c] 이런식

    age =  st.slider('나이', 1,100) 
    print(age)
    st.write('당신이 선택한 나이는 {}입니다'.format(age))                         

if __name__ == '__main__' :
    main()

    #오류