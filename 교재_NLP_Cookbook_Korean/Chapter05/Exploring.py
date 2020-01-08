import nltk
simpleSentence = "Seoul is the capital of Korea."
wordsInSentence = nltk.word_tokenize(simpleSentence)
print(wordsInSentence)
partsOfSpeechTags = nltk.pos_tag(wordsInSentence)
print(partsOfSpeechTags)
