## 편집거리 측정 ##
'''
편집거리(edit	distance)
- 레벤슈타인 거리(Levenshtein	distance)라고도 부름
- 두 문서간의 유사성을 측정하는데 사용
'''
from nltk.metrics.distance import edit_distance

def my_edit_distance(str1, str2):
    m= len(str1) + 1
    n= len(str2) + 1

    table = {}
    for i in range(m): table[i,0]=i
    for j in range(n): table[0,j]=j

    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            table[i,j] = min(table[i, j-1]+1, table[i-1, j]+1, table[i-1, j-1]+cost)

    return table[i,j]

print("Our Algorithm :",my_edit_distance("michel jackson", "mnd"))
print("NLTK Algorithm :",edit_distance("watssup man", "bamm"))

# 유사성의 숫자 범위는 어찌 되나?: cost 개념.
## 실제로 이 유사도보다는 코사인 유사도를 많이 씀.