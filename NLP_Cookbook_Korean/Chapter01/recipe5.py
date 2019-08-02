from nltk.corpus import wordnet as wn

chair = 'chair'

chair_synsets = wn.synsets(chair)
print('의자(Chair)의 뜻 Synsets :', chair_synsets, '\n\n')

for synset in chair_synsets:
    print(synset, ': ')
    print('Definition: ', synset.definition())
    print('Lemmas/Synonymous words: ', synset.lemma_names())
    print('Example: ', synset.examples(), '\n')
