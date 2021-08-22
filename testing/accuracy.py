import spacy
nlp = spacy.load("ja_core_news_md")
doc = nlp(u"サンプル文章です")
doc2 = nlp(u"サンプルの二文目です")
print(doc.similarity(doc2))
