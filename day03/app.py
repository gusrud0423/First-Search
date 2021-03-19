# 이미지 처리

import streamlit as st

from PIL import Image, ImageFilter, ImageEnhance



# def main()  : 

#     img = Image.open('data/birds.jpg')  # 이미지 가져오기 
#     st.image(img)  

#     option_list =  [ 'Show Image', 'Rotate Image', 'Creat Thumbnail',
#                      'Crop Image', 'Merge Images', 'Flip Image', 'Black & White',
#                       'Filters - Sharpen', 'Filters - Edge Enhance',
#                       'Contrast Image'  ]
#                      # 이러한 기능을 하도록 만든다

#     option =  st.selectbox('옵션을 선택하세요', option_list)

#     if option == 'Show Image' :
#         st.image(img)

#     elif option == 'Rotate Image' :
#         rotated_img = img.rotate(90) # 90 도 회전
#         img.save('data/rotate.png')
#         st.image(rotated_img)                        
    
#     elif option == 'Create Thumbnail' :
#          = (300,300)
#         img.thumbnail( size )
#         img.save('data/thumb.png') 
#         st.image(img)                # 원본 사이즈 바꾸고 data에 thumb.png 로 저장했다   (다른것도 가능 )

#     elif option == 'Crop Image' :      # 이미지 자를 때
#         # 왼쪽 윗부분 부터, 오른쪽 아래 부분 까지 잘라라
#         # 왼쪽 윗부분 좌표 ( 50,100 )
#         # 오른쪽 아래부분 좌표 ( 200,200 )
#         box = ( 50,100,200,200 )
#         cropped_img = img.crop(box)
#         img.save('data/crop.png')
#         st.image(cropped_img)


#     elif option == 'Merge Image' :  # 두개합치는 것
#         pass

#     elif option == 'Flip Image' :   #  이미지 뒤집기 
#         flipped_img = img.transpose( Image.FLIP_LEFT_RIGHT )  
#         st.image(flipped_img)

#     elif option == 'Black & White' :  # 이미지 색상 바꾸기
#         bw = img.convert('1')  # "L" 로쓰면 그레이스케일됨
#         st.image( bw )

#     elif option == 'Filters - Sharpen' :   # 이미지 선명하게
#         sharp_img = img.filter(ImageFilter.SHARPEN)
#         st.image( sharp_img )

#     elif  option == 'Filters - Edge Enhance'  :  # 윤곽선이 진해진다 
#         edge_img = img.filter(ImageFilter.EDGE_ENHANCE)
#         st.image(edge_img)

#     elif option == 'Contrast Image' :        # 대비가 세진다 
#         contrast_img = ImageEnhance.Contrast(img).enhance( 2 )
#         st.image(contrast_img)    

#     # 1.  이미지를 내가 마음대로 올릴 수 있어야 한다 .
#     # 조건 : 이미지는 1장
    

#     # 2.  하드코딩된 코드를, 유저한테 입력 받아서 처리 할 수 있도록 바꾼다 










#if __name__ == '__main__' :
#    main()



def load_image(image_file) :
    img = Image.open(image_file)
    return img
                     # 이미지 파일 만들어내는 함수

def main()  : 
    

    #1. 파일 업로드 하기
    image_file = st.file_uploader('Upload Image', type = ['png', 'jpg', 'jpeg']) 

    if image_file is not None :  # 유저가 입력한 파일이 있으면

        img = load_image(image_file)  # 다운로드한게 이미지파일에 있으면 이미지로 오픈하라
      

        option_list =  [ 'Show Image', 'Rotate Image', 'Creat Thumbnail',
                     'Crop Image', 'Merge Images', 'Flip Image', 'Change color',
                      'Filters - Sharpen', 'Filters - Edge Enhance',
                      'Contrast Image'  ]
                     # 이러한 기능을 하도록 만든다

        option =  st.selectbox('옵션을 선택하세요', option_list)

        if option == 'Show Image' :
            st.image(img)

        elif option == 'Rotate Image' :
            degree =  st.number_input('각도입력', 0,360 )   # 0부터 360까지 정수로 입력받을수 있음
            rotated_img = img.rotate(degree) # 90 도 회전
            img.save('data/rotate.png')
            st.image(rotated_img)                        
    
        elif option == 'Create Thumbnail' :   # 오류
            # 이미지의 사이즈를 알아야겠다.
            print(img.size)  
            #st.write(img.size) # 둘다 똑같음

            width = st.number_input('width 입력', 1, img.size[0] )  # 가로 세로 사이즈가 다르니 이렇게 해야함 
            height =  st.number_input( 'height 입력', 1, img.size[1] )
            size = ( width, height )

    
            img.thumbnail( size )
            img.save('data/thumb.png') 
            st.image(img)                # 원본 사이즈 바꾸고 data에 thumb.png 로 저장했다   (다른것도 가능 )

        elif option == 'Crop Image' :      # 이미지 자를 때
        # 왼쪽 윗부분 부터, 오른쪽 아래 부분 까지 잘라라
        # 왼쪽 윗부분 좌표 ( 50,10 )
        # 너비 x축으로, 깊이 y축으로 계산한 종료좌표(200,200)
        # 시작 좌표 + ( 너비 , 높이 ) =>  크랍 종료 좌표
            start_x = st.number_input('시작 x 좌표', 0, img.size[0]-1 )  # 가로 세로 사이즈가 다르니 이렇게 해야함 
            start_y =  st.number_input( '시작 y 좌표', 0, img.size[1]-1 ) 
            # start_x가 0~0까지 이고 start_y가 0~1 까지 면 이미지를 자를 때 전체다 자를 수도 있으니 예외처리를 한것
            max_width = img.size[0] - start_x
            max_height = img.size[0] - start_y   # 예외처리 한것 
            
            width = st.number_input('width 입력', 1, max_width ) # 너비가 0부터 시작일수는 없으니 1 임
            height =  st.number_input( 'height 입력', 1, max_height )    



            box = ( start_x, start_y, start_x + width, start_y + height )
            st.write(box)  # crop 이미지가 왜 안보여지는 지 확인한다
            cropped_img = img.crop(box)
            # img.save('data/crop.png')
            st.image(cropped_img)


        elif option == 'Merge Image' :  # 두개합치는 것    # 오류 

            merge_file = st.file_uploader('Upload Image', type = ['png', 'jpg', 'jpeg'], key='merge')    
                                                                                 # 위에 업로더 쓴것과 충돌이 일어나지 않게 키를 머지로 한것
           

            if merge_img is not None :
                  # 유저가 입력한 머지 이미지가 있으면      # 오류

                merge_img =  Image.open(merge_file)  # 이미지로 바꿔라 

                start_x = st.number_input('시작 x 좌표', 0, img.size[0]-1 )  # 가로 세로 사이즈가 다르니 이렇게 해야함 
                start_y =  st.number_input( '시작 y 좌표', 0, img.size[1]-1 )

                position =  (start_x, start_y)  # 원래 이미지 안쪽에 추가되는게 들어가게 y축 이 원본이미지 y축보다 작아야함 
                img.paste(merge_img, position)
                st.image(img)

        elif option == 'Flip Image' :   #  이미지 뒤집기    

            status = st.('플립 선택', ['FLIP_TOP_BOTTOM', 'FLIP_LEFT_RIGHT'])
            
            if status == 'FLIP_TOP_BOTTOM' :
                flipped_img = img.transpose( Image.FLIP_TOP_BOTTOM )  
            
            elif status == 'FLIP_LEFT_RIGHT' :
                flipped_img = img.transpose( Image.FLIP_LEFT_RIGHT )  
            
            st.image(flipped_img)  # 탑 바텀 이나 왼쪽오른쪽 나오게   # 셀렉트박스 써도됨

        elif option == 'Change Color' :  # 이미지 색상 바꾸기  # 오류

             status = st.radio('색 변경',
            ['Color', 'Gray Scale', 'Black & White'] )
            
            if status == 'Color' :
                color = 'RGB'
            elif status == 'Gray Scale' :
                color = 'L'
            elif status == 'Black & White' :
                color = '1'
            
            bw = img.convert('1')  # "L" 로쓰면 그레이스케일됨
            st.image( bw )

        elif option == 'Filters - Sharpen' :   # 이미지 선명하게
            sharp_img = img.filter(ImageFilter.SHARPEN)
            st.image( sharp_img )

        elif  option == 'Filters - Edge Enhance'  :  # 윤곽선이 진해진다 
            edge_img = img.filter(ImageFilter.EDGE_ENHANCE)
            st.image(edge_img)

        elif option == 'Contrast Image' :        # 대비가 세진다 
            contrast_img = ImageEnhance.Contrast(img).enhance( 2 )
            st.image(contrast_img)    

#3. 여러파일을 변환 할 수 있도록 수정
#    각 옵션마다 저장하기 버튼이 잇어서 ,
#    버튼 누르면 저장되도록
#    저장시에는, 디렉토리 이름을 유저가 직접 입력하여 저장
   
   
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



if __name__ == '__main__' :
    main()
