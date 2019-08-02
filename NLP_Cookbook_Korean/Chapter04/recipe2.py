import re

def text_match(text, patterns):
    if re.search(patterns, text):
        return('일치하는 항목을 찾았습니다!')
    else:
        return('일치하지 않음!')

print("테스트 패턴은 다음으로 시작하고 끝남")
print(text_match("abbc", "^a.*c$"))

print("단어로 시작함")
print(text_match("Tuffy eats pie, Loki eats peas!", "^\w+"))

print("단어와 선택적 문장부호로 끝남")
print(text_match("Tuffy eats pie, Loki eats peas!", "\w+\S*?$"))

print("단어의 시작이나 끝이 아닌 문자가 포함된 단어 찾기")
print(text_match("Tuffy eats pie, Loki eats peas!", "\Bu\B"))