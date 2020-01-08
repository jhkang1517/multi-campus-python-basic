

from sklearn.datasets import fetch_20newsgroups

newsgroups_train = fetch_20newsgroups(subset='train')
newsgroups_test = fetch_20newsgroups(subset='test')

x_train = newsgroups_train.data
x_test = newsgroups_test.data

y_train = newsgroups_train.target
y_test = newsgroups_test.target

print ("20개 카테고리 전체 목록:")
print (newsgroups_train.target_names)
print ("\n")
print ("샘플 이메일:")
print (x_train[0])
print ("샘플 타깃 카테고리:")
print (y_train[0])
print (newsgroups_train.target_names[y_train[0]])


# 데이터 전처리에 사용
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import pandas as pd
from nltk import pos_tag
from nltk.stem import PorterStemmer


def preprocessing(text):
    text2 = " ".join("".join([" " if ch in string.punctuation else ch for ch in text]).split())

    tokens = [word for sent in nltk.sent_tokenize(text2) for word in
              nltk.word_tokenize(sent)]
    
    tokens = [word.lower() for word in tokens]
    
    stopwds = stopwords.words('english')
    tokens = [token for token in tokens if token not in stopwds]
    
    tokens = [word for word in tokens if len(word)>=3]
    
    stemmer = PorterStemmer()
    try:
        tokens = [stemmer.stem(word) for word in tokens]

    except:
        tokens = tokens
        
    tagged_corpus = pos_tag(tokens)    
    
    Noun_tags = ['NN','NNP','NNPS','NNS']
    Verb_tags = ['VB','VBD','VBG','VBN','VBP','VBZ']

    lemmatizer = WordNetLemmatizer()

    def prat_lemmatize(token,tag):
        if tag in Noun_tags:
            return lemmatizer.lemmatize(token,'n')
        elif tag in Verb_tags:
            return lemmatizer.lemmatize(token,'v')
        else:
            return lemmatizer.lemmatize(token,'n')
    
    pre_proc_text =  " ".join([prat_lemmatize(token,tag) for token,tag in tagged_corpus])             

    return pre_proc_text

	
x_train_preprocessed  = []
for i in x_train:
	x_train_preprocessed .append(preprocessing(i))

x_test_preprocessed = []
for i in x_test:
	x_test_preprocessed.append(preprocessing(i))

# TFIDF 벡터라이저(vectorizer) 구축 
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(min_df=2, ngram_range=(1, 2),  stop_words='english', 
                             max_features= 10000,strip_accents='unicode',  norm='l2')

x_train_2 = vectorizer.fit_transform(x_train_preprocessed).todense()
x_test_2 = vectorizer.transform(x_test_preprocessed).todense()


# 딥러닝 모듈
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adadelta,Adam,RMSprop
from keras.utils import np_utils

# 하이퍼 파라미터 정의
np.random.seed(1337) 
nb_classes = 20
batch_size = 64
nb_epochs = 20

Y_train = np_utils.to_categorical(y_train, nb_classes)

# 케라스에서의 딥 레이어(심층) 모델 구축
model = Sequential()

model.add(Dense(1000,input_shape= (10000,)))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(500))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(50))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(nb_classes))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')

print (model.summary())

# 모델 학습
model.fit(x_train_2, Y_train, batch_size=batch_size, epochs=nb_epochs,verbose=1)

# 모델 예측
y_train_predclass = model.predict_classes(x_train_2,batch_size=batch_size)
y_test_predclass = model.predict_classes(x_test_2,batch_size=batch_size)

from sklearn.metrics import accuracy_score,classification_report

print ("\n\n딥 뉴럴 네트워크  - 학습 정확도:"),(round(accuracy_score(y_train,y_train_predclass),3))
print ("\n딥 뉴럴 네트워크  - 테스트 정확도:"),(round(accuracy_score(y_test,y_test_predclass),3))

print ("\n딥 뉴럴 네트워크  - 학습 분류 리포트(Train Classification Report)")
print (classification_report(y_train,y_train_predclass))

print ("\n딥 뉴럴 네트워크  - 테스트 분류 리포트(Test Classification Report)")
print (classification_report(y_test,y_test_predclass))
							 