from bs4 import BeautifulSoup

html_doc = open('sample-html.html', 'r').read()
soup = BeautifulSoup(html_doc, 'html.parser')

print('\n\nHTML이 제거된 전체 텍스트 :')
print(soup.get_text())

print('<title> 태그에 액세스 :', end=' ')
print(soup.title)

print('<H1> 태그의 텍스트에 엑세스 :', end=' ')
print(soup.h1.string)

print('<img> 태그의 속성에 엑세스 :', end=' ')
print(soup.img['alt'])

print('\n존재하는 모든 <p> 태그에 엑세스 :')
for p in soup.find_all('p'):
    print(p.string)