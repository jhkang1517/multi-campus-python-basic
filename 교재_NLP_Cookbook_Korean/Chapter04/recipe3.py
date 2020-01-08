import re

#search for literal strings in sentence
patterns = [ 'Tuffy', 'Pie', 'Loki' ]
text = 'Tuffy eats pie, Loki eats peas!'
for pattern in patterns:
    print('"%s"에서 "%s" 검색 중 ->' % (text, pattern),)
    if re.search(pattern,  text):
        print('찾았습니다!')
    else:
        print('찾을 수 없습니다!')

#search a substring and find it's location too

text = 'Diwali is a festival of lights, Holi is a festival of colors!'
pattern = 'festival'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('%d:%d에서 "%s"을(를) 찾았습니다.' % (s, e, text[s:e]))