import nltk, matplotlib
from nltk.corpus import webtext
print(webtext.fileids())

fileid = 'singles.txt'
wbt_words = webtext.words(fileid)
fdist = nltk.FreqDist(wbt_words)

print('최대 발생 토큰 "',fdist.max(),'" 수 : ', fdist[fdist.max()])
print('말뭉치 내 총 고유 토큰 수 : ', fdist.N())
print('말뭉치에서 가장 흔한 10개 단어는 다음과 같습니다.')
print(fdist.most_common(10))
print('개인 광고의 빈도 분포')
print(fdist.tabulate())
fdist.plot(cumulative=True)