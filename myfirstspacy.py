# Load a spacy model and check if it has ner
import spacy
import re
from spacy.lang.en.stop_words import STOP_WORDS

nlp = spacy.load("en_core_web_sm")

article_text = """
Tom Holland 2016
Who is peter parker
toooom holand
"""
"""
doc = nlp(article_text)
print(doc)
# print(doc.text)
# print(doc.ents)

for token in doc:
    print(token)
    # print(token.text, token.pos_, token.dep_)
for ent in doc.ents:
    print(ent.text, ent.label_)
"""
# create list of punctuations and stopwords
# punctuations = string.punctuation
stop_words = spacy.lang.en.stop_words.STOP_WORDS


# function for data cleaning and processing
# This can be further enhanced by adding / removing reg-exps as desired.


def spacy_tokenizer(sentence):
    # remove distracting single quotes
    sentence = re.sub('\'', '', sentence)

    # remove digits and words containing digits
    sentence = re.sub('\w*\d\w*', '', sentence)

    # replace extra spaces with single space
    sentence = re.sub(' +', ' ', sentence)

    # remove unwanted lines starting from special charcters
    sentence = re.sub(r'\n: \'\'.*', '', sentence)
    sentence = re.sub(r'\n!.*', '', sentence)
    sentence = re.sub(r'^:\'\'.*', '', sentence)

    # remove non-breaking new line characters
    sentence = re.sub(r'\n', ' ', sentence)

    # remove punctunations
    sentence = re.sub(r'[^\w\s]', ' ', sentence)

    # creating token object
    tokens = nlp(sentence)

    # lower, strip and lemmatize
    tokens = [word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in tokens]

    # remove stopwords, and exclude words less than 2 characters
    tokens = [word for word in tokens if word not in stop_words and word and len(word) > 2]

    # return tokens
    return tokens


sentence = """
Tom Holland 2016
Who is peter parker
toooom holand
"""
result = spacy_tokenizer(sentence)
print(result)