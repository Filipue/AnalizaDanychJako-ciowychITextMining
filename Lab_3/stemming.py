from nltk import PorterStemmer, word_tokenize


def stemmer(text: str) -> list:
    porter = PorterStemmer()
    t_words = word_tokenize(text)
    stem = list(text.split(" "))
    for word in t_words:
        stem.append(porter.stem(word))
    return stem
