from __future__ import print_function

from keras.models import Sequential
from keras.layers import Dense, LSTM,Activation,Dropout

from keras.optimizers import RMSprop

import numpy as np
import random
import sys


path = 'shakespeare_final.txt'
text = open(path).read().lower()

print('corpus length:', len(text))
characters = sorted(list(set(text)))
print('total chars:', len(characters))


char2indices = dict((c, i) for i, c in enumerate(characters))
indices2char = dict((i, c) for i, c in enumerate(characters))




# 텍스트를 어느정도 불필요한 부분은 최대길이(maxlen) 문자로 일련의 문자열씩 자른다.
maxlen = 40
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
print('nb sequences:', len(sentences))



# 인덱스를 벡터화된 형태로 변환
X = np.zeros((len(sentences), maxlen, len(characters)), dtype=np.bool)
y = np.zeros((len(sentences), len(characters)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char2indices[char]] = 1
    y[i, char2indices[next_chars[i]]] = 1



	
# 모델 구축
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(characters))))

model.add(Dense(len(characters)))

model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer=RMSprop(lr=0.01))

print (model.summary())


# 예측을 인덱스로 변환하는 함수
def pred_indices(preds, metric=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / metric
    exp_preds = np.exp(preds)
    preds = exp_preds/np.sum(exp_preds)
    probs = np.random.multinomial(1, preds, 1)
    return np.argmax(probs)



# 모델 학습 및 평가
for iteration in range(1, 30):
    print('-' * 40)
    print('Iteration', iteration)
    model.fit(X, y,batch_size=128,epochs=1)

    start_index = random.randint(0, len(text) - maxlen - 1)

    for diversity in [0.2, 0.7,1.2]:

        print('\n----- diversity:', diversity)

        generated = ''
        sentence = text[start_index: start_index + maxlen]
        generated += sentence
        print('----- Generating with seed: "' + sentence + '"')
        sys.stdout.write(generated)

        for i in range(400):
            x = np.zeros((1, maxlen, len(characters)))
            for t, char in enumerate(sentence):
                x[0, t, char2indices[char]] = 1.

            preds = model.predict(x, verbose=0)[0]
            next_index = pred_indices(preds, diversity)
            pred_char = indices2char[next_index]

            generated += pred_char
            sentence = sentence[1:] + pred_char

            sys.stdout.write(pred_char)
            sys.stdout.flush()
        print("\n하나의 조합 완료\n")
        
        
        






        
