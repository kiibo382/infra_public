import spacy

nlp = spacy.load("ja_core_news_sm")
doc = nlp("ハンズオン順調ですか。手を動かすの楽しいですよね")

for token in doc:
    print(token.text, token.pos_, token.dep_)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

print(type(doc.ents))
for i in dir(doc):
    print(i)
