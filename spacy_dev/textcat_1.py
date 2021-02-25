import spacy

nlp = spacy.load("ja_core_news_sm")

doc = nlp("これは文章です。")

textcat = nlp.add_pipe("textcat")

print(textcat.labels)
