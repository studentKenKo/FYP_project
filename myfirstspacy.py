# Load a spacy model and check if it has ner
import spacy

nlp = spacy.load("en_core_web_sm")

article_text = """
Tom Holland actor marvel superhero spiderman
"""

doc = nlp(article_text)


print(doc.text)
print(doc.ents)

for token in doc:
    print(token.text, token.pos_, token.dep_)
for ent in doc.ents:
    print(ent.text, ent.label_)