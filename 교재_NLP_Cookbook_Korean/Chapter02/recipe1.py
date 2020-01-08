namesList =  ['유나', '지은', '스튜어트', '케빈']
sentence = '우리 강아지는 소파 위에서 잔다'

names = ';'.join(namesList)
print(type(names), ':', names)
wordList = sentence.split(' ')
print((type(wordList)), ':', wordList)

additionExample = '파이썬' + '파이썬' + '파이썬'
multiplicationExample = '파이썬' * 2
print('텍스트 덧셈 :', additionExample)
print('텍스트 곱셈 :', multiplicationExample)

str = 'Python NLTK'
print(str[1])
print(str[-3])