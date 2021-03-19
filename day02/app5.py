import streamlit as st

from PIL import Image

import pandas as pd

import os

# 디렉토리와 파일을 주면, 해당 디렉토리에 이 파일을 저장하는 함수

def save_uploaded_file(directory, file) :
    # 1 . 디렉토리가 있는지 확인하여 , 없으면 만든다.
    if not os.path.exists(directory) :      
        os.makedirs(directory)
    # 2 . 이제는 디렉토리가 있으니까 , 파일을 저장 
    with open(os.path.join(directory, file.name),  'wb') as f : 
        f.write(file.getbuffer())
    return st.success('Saved file : {} in {}'.format(file.name, directory))        


def load_image(image_file) :
    img = Image.open(image_file)
    return img
                     # 항상 이미지 파일 오픈한 결과를 볼수 있게 한 함수



def main() :
    st.title('여러 파일들 하는 앱')

    # 사이드바용 메뉴
    menu = ['Home', 'Dataset', 'About']
    choice =  st.sidebar.selectbox('메뉴', menu) # UI 작성할땐 항상 중간에 잘 나오는지 확인 해야함 
    print(choice)

    if choice == 'Home' : # 초이스가 홈이랑 같으면 
        uploade_files = st.file_uploader('이미지 파일 업로드', type = ['png', 'jpeg', 'jpg'],  # 이런타입만 받아라
                                                          accept_multiple_files = True )  # 여러개의 파일 받을수 있다 
        if uploade_files is not None :  # 변수가 Null 인지 확인을 해야하는 경우 ??
            st.write(uploade_files)    # 이미지 파일을 write 하면 이미지가 직접 표시되는것은 아님

            for img_file in uploade_files :
                save_uploaded_file('temp_files', img_file)  # 첫번째 , 두번째, 세번째 이미지를 한개씩 반복문 돌면서 템프 파일즈라는 파일에 들어간다 

                img - load_image(img_file)
                st.image(img, width = 150)      
    
  ################### CSV 파일을 여러개 올리면 , 모두 저장하는 코드 작성 ####################
    
    # 유저가 Dataset 메뉴 클릭하면 여기서 처리
    elif choice == 'Dataset' :
        # 파일 업로드 생성 
        uploade_files = st.file_uploader('CSV파일 여러개 업로드', type = ['csv'], accept_multiple_files = True ) 
        # 만약 파일이 정상이면, 파일 저장
        if uploade_files is not None :  # 변수가 Null 인지 확인을 해야하는 경우 ??

            file_name_list = [ ]  # 빈 리스트를 만들어 파일이름을 저장할수 있게 만들어준다 

            st.write(uploade_files)    # 이미지 파일을 write 하면 이미지가 직접 표시되는것은 아님

            for csv_file in uploade_files :
                save_uploaded_file('temp_files', data_file)  # 첫번째 , 두번째, 세번째 이미지를 한개씩 반복문 돌면서 템프 파일즈라는 파일에 들어간다 
                
                file_name_list.append( csv_file.name ) 
                #  위에 포문이 다끝나고 포문 돌릴때 가져온 csv파일에서 csv파일의 이름을 가져와서 파일네임 리스트에 추가해라  
                #  밑에 작업이 실행될려면 유저가 올린것들이 다 추가를 해야함

    # 파일 저장이 모두 끝나면 , 화면에 셀렉트박스 보여주고 
    # 린 csv 파일을 선택 하면 데이터 프레임이 나오도록 코드 작성
    
            selected_file =  st.selectbox('파일을 선택하세요', file_name_list)
            # print(selected_file_name) 디버깅용이었음

            df = pd.read_csv('temp_files/'+selected_file)

            st.dataframe(df)

    

if __name__ == "__main__" :
    main()

     # 여기 오류