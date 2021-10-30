from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import pandas as pd
import win32com.client
import re

word = win32com.client.Dispatch("Word.Application")
word.Visible = 0

 
doc1 = word.Documents.Open("C:/Users/seoyo/Desktop/2021-2학기/머신러닝/수업/데이터셋/ML-2021-text-1-vectorspace-dataset.docx")
doc = list()
sentences= str(doc1.Content)
sentences= sentences.replace('\r','\n')
print(sentences)
doc.append(sentences.split())
print(doc)
word.Quit()

#sentences= str(doc1.Content)
#print(sentences)
#doc = list()
#for line in sentences:
#    for i in re.split(':\r|\r\r|.\r|\r',line):
 #       if i: doc.append(i)

#print(doc)

cvec = CountVectorizer(stop_words = "english", min_df=3, max_df = 0.5, ngram_range=(1, 2), lowercase=False)
sf = cvec.fit_transform(str(doc))

transformer = TfidfTransformer(smooth_idf=False)
transformed_weights = transformer.fit_transform(sf)
weights = np.asarray(transformed_weights.mean(axis = 0)).ravel().tolist()
weights_df = pd.DataFrame({'term':cvec.get_feature_names_out(), 'weight':weights})
print(weights_df.sort_values(by = 'weight', ascending = False).head(10))
