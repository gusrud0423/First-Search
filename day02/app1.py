import streamlit as st

from PIL import Image


def main() :

    img = Image.open('data/image_03.jpg')
    st.image(img, use_column_width= True)  # 이미지를 페이지 화면에 맞게 폭을 늘려서 출력함
                                        
                                            # 인터넷에 있는 이미지도 가능 
    # st.image('')  여기안에 url 주소 가져오면 됨 

   
   
    video_file = open('data/secret_of_success.mp4', 'rb' ).read()  # 비디오 파일 불러오기
    st.video(video_file)  # 비디오파일 불러온것을 실행해라  

    
    
    audio_file =  open('data/song.mp3', 'rb').read()  # 오디오 파일 불러오기 
    st.audio( audio_file )             # 오디오 실행 


if __name__ == '__main__' :
    main()
        


#경로 바꾸는 법   파일을 새로 만들어서 그 안에 파일을 만들어도 경로를 설정해줘야 한다 
# 
# 1. 스트림릿>cd day02  치고 엔터 치면 커런트워킹 디렉토리 바뀜   
# 
# 
# 했던거 초기화 할려면 cls 쳐서 엔터치기 
# 
# *****  데이 02 에서 스트림릿으로 다시 커런트 워킹 디렉토리 바꾸고 싶으면 cd .. 이렇게 치고 cd day02치면 바뀜 
# 
#   저기 이미지 오픈함수에 경로를 day02/data/로 바꿔야 한다 
# 스트림릿>스트림릿 런 데이 02/app.py   치면 실행됨 
# 
# 커런트 워킹 디렉토리는 내가 지금 어디서 작업하고 있는지를 나타냄 
# 
#      



