str = 'NLTK Dolly Python'
print('다음의 인덱스에서 끝나는 부분 문자열:',str[:4])

print('다음의 인덱스에서 시작하는 부분 문자열:',str[11:] )
print('부분 문자열:',str[5:10])
print('복잡한 방식의 부분 문자열:', str[-12:-7])

if 'NLTK' in str:
    print('NLTK를 찾았습니다.')

replaced = str.replace('Dolly', 'Dorothy')
print('대체된 문자열:', replaced)

print('각 문자(character) 액세스:')
for s in replaced:
    print(s)