import streamlit as st

from PIL import Image

import pandas as pd
from PyPDF2 import PdfFileReader # (pip install PyPDF2)  pdf 파일 쓸 수있게 라이브러리 설치 

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




# pdf 파일 읽어오는 파일   
def read_pdf(pdf_file) :
    pdfReader = PdfFileReader(pdf_file)
    count = pdfReader.numPages  # 페이지 정보 있음 
    text = ''
    for i in range(count) :
        page =  pdfReader.getPage(i)
        text =  text + page.extractText()
    return text    




def load_image(image_file) :
    img = Image.open(image_file)
    return img
                     # 항상 이미지 파일 오픈한 결과를 볼수 있게 한 함수


def main() :
    st.title('파일 업로드 프로젝트')

    menu = ['Image', 'Dataset', 'Documents', 'About']  # 메뉴 카테고리
    choice = st.sidebar.selectbox('메뉴', menu)  # 메뉴를 표시해라
    print(choice)  # 사람이 볼수있게 디버깅함


    if choice == 'Image' :       # 이미지가 초이스랑 같다면 
        st.subheader('이미지파일 업로드')  # 이미지 파일 업로드 라는 헤드를 달아주고 
        image_file = st.file_uploader('Upload Image', type = ['png', 'jpg', 'jpeg'])  # 이미지 다운로드 할수있게 함
                                               # 이미지 파일 업로드 하는데 이 형식들것만 받겠다 
        # 유저가 입력한 파일이 있으면
        if image_file is not None :   # 파일 정보도 알아낼수 있다  # 이미지 가져와서 넣어봐도 됨
            st.write(type(image_file))
            st.write(image_file.name)
            st.write(image_file.size)
            st.write(image_file.type)


            img = load_image(image_file)
            st.image(img, width = 250)    # 파일 넣었을 때 크기를 표시함 ?

            save_uploaded_file('temp_files', image_file) 
             # 이미지파일로 하라 위에 파일 저장함수 씀     옆에 목록에 파일 만들어짐
    
    # 화면에 표시하는건 st 가 하고  이미지파일 로드하는건 PIL 함수가 하는것 

    ##################### dataset 업로드 하기 ###################
    
    elif choice == 'Dataset' :
        st.subheader('CSV 파일 업로드')
        data_file = st.file_uploader('Uploade CSV', type =['csv'])  # csv 파일 업로드 하자
        if data_file is not None:
            st.write(data_file.name)
            st.write(data_file.type)
            st.write(data_file.size)

            # 데이터 프레임을 화면에 표시 
            df = pd.read_csv('data_file')  # 데이터 파일 변수에 데이터프레임 들어있다 그래서 위에서 data_file.name 이렇게 쓸수 있었던것  
            st.dataframe( df )

            save_uploaded_file('temp_files', data_file)  # 다른 파일 이름도 가능 
    ################## Documents  업로드 하기 ########################

    elif choice == 'Documents' :
        st.subheader('문서 파일 업로드')
        doc_file =  st.file_uploader('Upload pdf or txt', type=['pdf', 'txt'])  # pdf나 txt 만 받겠다     
   
        if st.button('Process') :
            #st.write('버튼 클릭 됨')
            print('버튼 클릭 됨')  
            st.write(doc_file.type)
              # 파일 넣어서 타입 확인 했더니 pdf 파일은 application/pdf 이렇게 
              # text 파일은  text/plain 로 나오니까 
              # #이걸 이용해서 데이터 타입이 이러하면 밑에처럼 출력해라 라고 할수있음




            if doc_file.type == 'application/pdf':   # 파일을 구분하는데 pdf 
                text = read_pdf(doc_file)  # 위에 pdf 파일을 텍스트로 받아온것을 text로 저장하고
                st.write(text)  # text 를 출력해라 

                save_uploaded_file('temp_files', doc_file) # pdf 파일로 저장 

            elif doc_file.type == 'text/plain' :   # 파일 구분 할때 TEXT 이면 
                    text = str( doc_file.read() , 'utf-8' )  # utf -8 파일로 읽어라 
                    st.write(text) 

                    save_uploaded_file('temp_files', doc_file) #  utf-8로 읽은것을 파일에 저장 

            else :
                st.error('PDF 나 TXT 가 아닌 파일은 업로드 불가')    ## 예외처리 함 이것 중요
                     



        


if __name__ == '__main__' :
    main()    