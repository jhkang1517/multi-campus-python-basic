from __future__ import print_function

import os
""" 먼저 다음 디렉토리 링크를 모든 입력 파일이 있는 곳으로 변경하시오 """
os.chdir("C:/Users/[사용자이름]/Documents/book_codes/NLP_DL")

from sklearn.model_selection import train_test_split
import nltk
import numpy as np
import string


# 파일 읽기
with open('alice_in_wonderland.txt', 'r') as content_file:
    content = content_file.read()

content2 = " ".join("".join([" " if ch in string.punctuation else ch for ch in content]).split())
 
tokens = nltk.word_tokenize(content2)
tokens = [word.lower() for word in tokens if len(word)>=2]

# N-1이 마지막 N번째 단어를 예측하는 데 사용되는 N그램에 대한 N값 선택
N = 3
quads = list(nltk.ngrams(tokens,N))

newl_app = []
for ln in quads:
    newl = " ".join(ln)        
    newl_app.append(newl)

# 단어 벡터화
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()

x_trigm = []
y_trigm = []

for l in newl_app:
    x_str = " ".join(l.split()[0:N-1])
    y_str = l.split()[N-1]   
    x_trigm.append(x_str)
    y_trigm.append(y_str)

x_trigm_check = vectorizer.fit_transform(x_trigm).todense()
y_trigm_check = vectorizer.fit_transform(y_trigm).todense()

# 단어에서 정수, 정수에서 단어로 변환하기 위한 딕셔너리
dictnry = vectorizer.vocabulary_
rev_dictnry = {v:k for k,v in dictnry.items()}

X = np.array(x_trigm_check)
Y = np.array(y_trigm_check)

Xtrain, Xtest, Ytrain, Ytest,xtrain_tg,xtest_tg = train_test_split(X, Y,x_trigm, test_size=0.3,random_state=42)

print("X Train shape",Xtrain.shape, "Y Train shape" , Ytrain.shape)
print("X Test shape",Xtest.shape, "Y Test shape" , Ytest.shape)

# 모델 구축
from keras.layers import Input,Dense,Dropout
from keras.models import Model

np.random.seed(42)

BATCH_SIZE = 128
NUM_EPOCHS = 100

input_layer = Input(shape = (Xtrain.shape[1],),name="input")
first_layer = Dense(1000,activation='relu',name = "first")(input_layer)
first_dropout = Dropout(0.5,name="firstdout")(first_layer)

second_layer = Dense(800,activation='relu',name="second")(first_dropout)

third_layer = Dense(1000,activation='relu',name="third")(second_layer)
third_dropout = Dropout(0.5,name="thirdout")(third_layer)

fourth_layer = Dense(Ytrain.shape[1],activation='softmax',name = "fourth")(third_dropout)


history = Model(input_layer,fourth_layer)
history.compile(optimizer = "adam",loss="categorical_crossentropy",metrics=["accuracy"])

print (history.summary())

# 모델 학습
history.fit(Xtrain, Ytrain, batch_size=BATCH_SIZE,epochs=NUM_EPOCHS, verbose=1,validation_split = 0.2)

# 모델 예측
Y_pred = history.predict(Xtest)


# 테스트 데이터에 대한 샘플 확인
print ("Prior bigram words","|Actual","|Predicted","\n")

for i in range(10):
    print (i,xtest_tg[i],"|",rev_dictnry[np.argmax(Ytest[i])],"|",rev_dictnry[np.argmax(Y_pred[i])])

	
	
import random
	
	
NUM_DISPLAY = 10
   
for i in random.sample(range(len(xtest_tg)),NUM_DISPLAY):
	print (i,xtest_tg[i],"|",rev_dictnry[np.argmax(Ytest[i])],"|",rev_dictnry[np.argmax(Y_pred[i])])





