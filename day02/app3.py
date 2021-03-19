import streamlit as st

from PIL import Image  # 파이썬에서 이미지 불러올때

img = Image.open('data/image_03.jpg' )
st.set_page_config(page_title =  'machine running', page_icon= img, layout = 'wide', initial_sidebar_state = 'collapsed')  
            #     실행되는 화면의 페이지 이름이 바뀜  # 페이지 아이콘도 바꿔짐  이모지에서 원하는거 카피함
            #    메인함수 안에서 해도되지만 페이지 변경하는거라 굳이 그럴필요 없음 



def main() :
    
    st.title('HELLO ~ 🌟')   # 화면에 출력됨
    st.sidebar.success('Menu')


if __name__ == '__main__' :
    main()

