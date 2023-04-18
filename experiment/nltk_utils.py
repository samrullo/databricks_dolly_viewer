import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def get_eng_stop_words():
    stop_words=set(stopwords.words('english'))
    return stop_words

def get_pos_tags(text,stop_words):
    words=word_tokenize(text)
    filtered_words=[word.lower() for word in words if word.lower() not in stop_words]
    pos_tags=pos_tag(filtered_words)
    return pos_tags


def extract_nouns(text):
    stop_words=get_eng_stop_words()
    pos_tags=get_pos_tags(text,stop_words)
    nouns=[word for word,pos_tag in pos_tags if pos_tag=='NN']
    nouns=list(set(nouns))
    return nouns