 # -*- coding: utf8 -*-
import nltk

# http://www.smbc-comics.com/?id=2779

def nurbleize(sentence):
     allowed=["NNP","NNS","NN"]
     punct=[".",","]
     result = []
     tk=nltk.word_tokenize(sentence)
     tg=nltk.pos_tag(tk)
     for (w,p) in tg:
             if p in allowed:
                     result +=[" "+w.upper()]
             elif p in punct:
                     result +=[w]
             else:
                     result +=[" nurble"]
     return "".join(result)[1:]

example = "Bedrich Smetana was a Czech composer who pioneered the development of a musical style which became closely identified with his country's aspirations to independent statehood. He is thus widely regarded in his homeland as the father of Czech music. Internationally he is best known for his opera The Bartered Bride, for the symphonic cycle Ma vlast ('My Fatherland'), which portrays the history, legends and landscape of the composer's native land, and for his First String Quartet From My Life."

print(nurbleize(example))
