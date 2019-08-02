## 어간 추출 ##
'''
어간추출(Stemming)
- 단어의 어근을 중심으로 규칙에 기반하여 어미를 제거 혹은 변화하여 표준화
- PorterStemmer	에 비교하여	LancasterStemmer의 예문에서 더 많은 제거가 일어났음을 확인할 수 있음	(name	->	na
- 규칙에 기반하여 표준화 하여 새로운 단어도 처리가 가능함	=>	규칙에만 일치하면 처리가 가능
'''
from nltk import PorterStemmer, LancasterStemmer, word_tokenize

raw = "My name is Maximus Decimus Meridius, commander of the Armies of the North, General of the Felix Legions and loyal servant to the true emperor, Marcus Aurelius. Father to a murdered son, husband to a murdered wife. And I will have my vengeance, in this life or the next."
tokens = word_tokenize(raw)

porter = PorterStemmer()
pStems = [porter.stem(t) for t in tokens]
print(pStems)

lancaster = LancasterStemmer()
lStems = [lancaster.stem(t) for t in tokens]
print(lStems)