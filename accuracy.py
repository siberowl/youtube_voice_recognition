import spacy
import speechrecognition as sr

nlp = spacy.load("ja_core_news_md")
for i in range(6):
    print(i)
    filename = "./sample_audio/sample" + str(i + 1) + ".wav"
    f = open("./sample_audio/sample" + str(i + 1) + ".txt", "r")
    answer_text = f.read().strip()
    gen_text = sr.getText(filename)
    print("answer: " + answer_text)
    print("generated: " + gen_text)
    answer_doc = nlp(answer_text)
    gen_doc = nlp(gen_text)
    answer_doc_nsw = nlp(" ".join([str(t) for t in answer_doc if not t.is_stop]))
    gen_doc_nsw = nlp(" ".join([str(t) for t in gen_doc if not t.is_stop]))
    print("answer no stop words: " + str(answer_doc_nsw))
    print("generated no stop words: " + str(gen_doc_nsw))
    print("similarity: " + str(answer_doc_nsw.similarity(gen_doc_nsw)))
