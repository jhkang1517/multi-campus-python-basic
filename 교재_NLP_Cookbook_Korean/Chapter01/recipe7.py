from nltk.corpus import wordnet as wn
type = 'n'

synsets = wn.all_synsets(type)

lemmas = []
for synset in synsets:
    for lemma in synset.lemmas():
        lemmas.append(lemma.name())

print(len(lemmas))
lemmas = set(lemmas)
print('개별 기본형 합계: ', len(lemmas))

count = 0
for lemma in lemmas:
    count = count + len(wn.synsets(lemma, type))

print('총 뜻: ', count)
print(type, '(명사)의 다의어 평균: ', count/len(lemmas))
