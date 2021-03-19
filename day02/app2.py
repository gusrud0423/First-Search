import streamlit as st


def main() :
    
    fname = st.text_input('이름을 입력하세요')
    st.title(fname)

    fname2 = st.text_input('이름을 입력하세요', max_chars = 5)   # 유저한테 입력 받을 껀데 5글자까지만 나오게해라
    st.title(fname2)
       #text 해도됨 day01에서 했음 

    message =  st.text_area('메세지를 입력하세요',height = 3)  # 문자를 3줄 까지 입력가능
    st.write(message)

    number =  st.number_input('숫자 입력', 1,100 )   # 1부터 100까지 정수로 입력받을수 있음
    st.write(number)

    number2 = st.number_input('숫자입력', 0.0, 20.0)  # 0.0 부터 20.0 까지  # 아무것도 안쓰면 실수로 자동
    st.write(number2)


    my_date =  st.date_input('약속 날짜')  # 날짜 선택 가능
    st.write(my_date)

    my_time =  st.time_input('시간 선택')   # 시간 선택 가능 
    st.write(my_time) 


    password =  st.text_input('비밀번호 입력', type= 'password', max_chars=12) # 타입 파라미터 뭐있는지 확인해 
    st.write(password)                               # 비밀번호 입력할수있게 함  12 글자 까지만  
    
    color =  st.color_picker('색을 선택하세요')  # 색깔 선택하기
    st.write(color)

    



if __name__ == '__main__' :
    main()