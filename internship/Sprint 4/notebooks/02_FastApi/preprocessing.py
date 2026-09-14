import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


stop_words = set(
    stopwords.words("english")
)

stop_words.discard("not")
stop_words.discard("no")
stop_words.discard("nor")

lemmatizer = WordNetLemmatizer()


def preprocess_text(text):

    tokens = word_tokenize(text)

    tokens = [
        token.lower()
        for token in tokens
    ]

    tokens = [
        token
        for token in tokens
        if token not in string.punctuation
    ]

    tokens = [
        token
        for token in tokens
        if token not in stop_words
    ]

    tokens = [
        lemmatizer.lemmatize(token)
        for token in tokens
    ]

    return " ".join(tokens)