# Car_Purchase_Amount  
import streamlit as st
import pandas as pd
import numpy as np



def main() :
    st.title('자동차 구매 가격 예측')

    menu = ['Dataset', 'X_data, y_data']  # 메뉴 카테고리
    choice = st.sidebar.selectbox('메뉴', menu)  # 메뉴를 표시해라
    print(choice)  # 사람이 볼수있게 디버깅함
    

    df =  pd.read_csv('data/Car_Purchasing_Data.csv')
    st.dataframe(df)

    X = X = df.iloc[ : , 3 : -2+1] 
    y = df['Car Purchase Amount']

    from sklearn.preprocessing import MinMaxScaler
    sc = MinMaxScaler()
    X= sc.fit_transform(X)

    y= y.reshape(-1,1)

    from sklearn.preprocessing import MinMaxScaler
    sc1 = MinMaxScaler()
    y = sc1.fit_transform(y)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size =0.2, random_state = 0)
    
    import tensorflow.keras
    from keras.models import Sequential
    from keras.layers import Dense
    from sklearn.preprocessing import MinMaxScaler

    model = Sequential()
    model.add( Dense( input_dim=5 , units = 32  ,  activation = 'relu' ) )
    model.add( Dense( units= 64   , activation= 'relu' ) )
    model.add(Dropout(0.2))
    model.add( Dense( units= 128  , activation= 'relu' ) )
    model.add( Dense( units= 1, activation= 'linear') )
    model.summary()
    
    model.compile( optimizer= 'adam', loss = 'mean_squared_error' )

    # 최적의 모델은 벨리데이션 정확도가 높고 로스는 적은 것이 좋은것 

    import h5py
    from tensorflow.keras.callbacks import ModelCheckpoint, CSVLogger
    import pickle

    cp = ModelCheckpoint( filepath= 'car_ai.h5', monitor = 'val_loss', save_best_only= True, verbose= 1 )

    epochs_hist = model.fit( X_train, y_train, epochs= 30 ,batch_size= 30 , validation_data= (X_test, y_test), verbose= 1, callbacks= [cp])



  
    
    
   

            


            
        



    
    








if __name__ == '__main__' :
    main()