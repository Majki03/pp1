def num_of_words(text):
    words = text.split()
    return len(words)

def ordered(text):
    words = text.split()
    sorted_words = sorted(words, key = len, reverse = True)
    return sorted_words

def alfabetical(text):
    words = text.split()
    sorted_words = sorted(words, key = str.lower)
    return sorted_words