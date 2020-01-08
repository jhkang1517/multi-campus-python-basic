## 표제어 추출(Lemmatization) ##
'''
표제어 추출(Lemmatization)
- 사전에 기반한 표제어 추출.
- 품사 정보를 보존하여 표준화 하는 작업
- 사전에 등록되지 않은 단어는 표준화 되지 않는 문제점이 있음
'''
from nltk import word_tokenize, PorterStemmer, WordNetLemmatizer

raw = "My name is Maximus Decimus Meridius, commander of the armies of the north, General of the Felix legions and loyal servant to the true emperor, Marcus Aurelius. Father to a murdered son, husband to a murdered wife. And I will have my vengeance, in this life or the next."
tokens = word_tokenize(raw) # 단어로 토큰화 하고,

porter = PorterStemmer() # PorterStemmer 불러오고
stems = [porter.stem(t) for t in tokens] # 토큰마다 실행
print(stems)

lemmatizer = WordNetLemmatizer() # WordNet 가져와서
lemmas = [lemmatizer.lemmatize(t) for t in tokens] # 토큰마다 실행
print(lemmas)


## 두 스테머의 차이는?