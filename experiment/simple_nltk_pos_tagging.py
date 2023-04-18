import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

sentence="The quick brown fox jumps over the lazy dog"

words = word_tokenize(sentence)
stop_words=set(stopwords.words('english'))
filtered_words=[word for word in words if word.lower() not in stop_words]

pos_tags=pos_tag(filtered_words)

print(f"Filtered words : {filtered_words}")
print(f"POS tags : {pos_tags}")