"""
demo09_cv.py 词袋模型
"""
import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft

doc = 'The brown dog is running. ' \
      'The black dog is in the black room. ' \
      'Running in the room is forbidden.'

# 对doc按照句子进行拆分
sents = tk.sent_tokenize(doc)

# 构建词袋模型
cv = ft.CountVectorizer()
bow = cv.fit_transform(sents)
print(bow.toarray())