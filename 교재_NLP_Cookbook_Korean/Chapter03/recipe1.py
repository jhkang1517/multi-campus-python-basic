## 토큰화 ##
'''
NLTK	tokenizer	비교
- LineTokenizer	:	개행문자(/n)를 기준으로 토큰화.	마침표나 문장 단위가 아님
- SpaceTokenizer	:	공백을 기준으로 토큰화
- TweetTokenizer	:	트위터에 특화한 토큰화.	이모티콘도 하나의 토큰으로 인지
- word_tokenize	:	단어 기준 토큰화
'''
from nltk.tokenize import LineTokenizer, SpaceTokenizer, TweetTokenizer
from nltk import word_tokenize
# 줄로 자름
lTokenizer = LineTokenizer();
print("Line tokenizer 출력 : ", lTokenizer.tokenize("My name is Maximus Decimus Meridius, commander of the Armies of the North, General of the Felix Legions and loyal servant to the true emperor, Marcus Aurelius.\nFather to a murdered son, husband to a murdered wife. \nAnd I will have my vengeance, in this life or the next."))
# 공백으로 자름
rawText = "By 11 o'clock on Sunday, the doctor shall open the dispensary."
sTokenizer = SpaceTokenizer()
print("Space Tokenizer 출력 :", sTokenizer.tokenize(rawText))
# 단어로 자름
print("Word Tokenizer 출력 : ", word_tokenize(rawText))
# 트윗에 특화됨, 이모티콘도 잡음
tTokenizer = TweetTokenizer()
print("Tweet Tokenizer 출력 : ", tTokenizer.tokenize("This is a cooool #dummysmiley: :-) :-P <3"))