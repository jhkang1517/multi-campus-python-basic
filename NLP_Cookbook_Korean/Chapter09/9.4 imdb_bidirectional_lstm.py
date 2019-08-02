# IMDB 감정 분류 작업에 양방향 LSTM으로 학습

from __future__ import print_function
import numpy as np
import pandas as pd

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Embedding, LSTM, Bidirectional
from keras.datasets import imdb

from sklearn.metrics import accuracy_score,classification_report


# 최대 피처 제한
max_features = 15000
max_len = 300
batch_size = 64

# 데이터 로딩
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
print(len(x_train), 'train observations')
print(len(x_test), 'test observations')

# 효율적인 연산을 위한 패드 배열
x_train_2 = sequence.pad_sequences(x_train, maxlen=max_len)
x_test_2 = sequence.pad_sequences(x_test, maxlen=max_len)
print('x_train shape:', x_train_2.shape)
print('x_test shape:', x_test_2.shape)
y_train = np.array(y_train)
y_test = np.array(y_test)

# 모델 구축
model = Sequential()
model.add(Embedding(max_features, 128, input_length=max_len))
model.add(Bidirectional(LSTM(64)))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile('adam', 'binary_crossentropy', metrics=['accuracy'])

# 모델 아키텍처 출력
print (model.summary())

# 모델 학습
model.fit(x_train_2, y_train,batch_size=batch_size,epochs=4,validation_split=0.2)

# 모델 예측
y_train_predclass = model.predict_classes(x_train_2,batch_size=100)
y_test_predclass = model.predict_classes(x_test_2,batch_size=100)

y_train_predclass.shape = y_train.shape
y_test_predclass.shape = y_test.shape


# 모델 정확도 및 메트릭 계산
print (("\n\nLSTM Bidirectional Sentiment Classification  - Train accuracy:"),(round(accuracy_score(y_train,y_train_predclass),3)))
print ("\nLSTM Bidirectional Sentiment Classification of Training data\n",classification_report(y_train, y_train_predclass))
print ("\nLSTM Bidirectional Sentiment Classification - Train Confusion Matrix\n\n",pd.crosstab(y_train, y_train_predclass,rownames = ["Actuall"],colnames = ["Predicted"]))      

print (("\nLSTM Bidirectional Sentiment Classification  - Test accuracy:"),(round(accuracy_score(y_test,y_test_predclass),3)))
print ("\nLSTM Bidirectional Sentiment Classification of Test data\n",classification_report(y_test, y_test_predclass))
print ("\nLSTM Bidirectional Sentiment Classification - Test Confusion Matrix\n\n",pd.crosstab(y_test, y_test_predclass,rownames = ["Actuall"],colnames = ["Predicted"]))      






