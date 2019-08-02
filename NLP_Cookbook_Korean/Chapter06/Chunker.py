import nltk

text = "Namsan Botanical Garden is a well known botanical gardenin Seoul, Korea."
sentences = nltk.sent_tokenize(text)
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    chunks = nltk.ne_chunk(tags)
    print(chunks)
