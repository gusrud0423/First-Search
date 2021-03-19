import streamlit as st


def main( ) :
   st.title( "hello streamlit project!" )
   name =  '김나나'
   st.text("안녕하세요 저는 {}입니다.".format(name))
   
   st.header("안녕하세요")
   st.header('안녕하세요')  # 큰따옴표, 작은 따옴표 상관 없이 결과는 같음

   st.markdown("# 큰글자")    # 글자 굵게
   st.markdown("## 중간글자")   # 일반
   #st 더 작은 글자??

   st.success('성공했을때~')
   st.warning('경고를 하고 싶을때')
   st.info('인포를 주고 싶을때')
   st.error('에러가 발생했음을 알리고 싶을때')
   st.exception('예외 상황이 발생했을때')

if __name__ == '__main__' :
   main()

# 스트림릿을 실행 시키는데 라이브러리 불러오고 실행한 파이썬의 파일명이 __main__ 이 되는거고  
# 메인 함수를 def가 받아서 스트림릿이 그내용들 실행시킨다
# 이제 순서대로 hello~~, ~~~~~~~쭉 실행되면서 찍힌다 
# 다 실행 되면 다시 if 문에서 함수호출한 부분으로 와서 끝난다 


