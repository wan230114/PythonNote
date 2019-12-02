"""
demo11_ztsb.py 主题识别
"""
import numpy as np
import sklearn.datasets as sd
import sklearn.feature_extraction.text as ft
import sklearn.naive_bayes as nb

train = sd.load_files('../ml_data/20news', 
	encoding='latin1', shuffle=True, 
	random_state=7)
# train.data: 2968个样本，每个样本都是一篇邮件文档
print(np.array(train.data).shape)
# train.target: 2968个样本，每个样本都是文档对应的类别
print(np.array(train.target).shape)
print(train.target_names)

# 基于train.data训练集， 生成tfidf矩阵
cv = ft.CountVectorizer()
bow = cv.fit_transform(train.data)
tt = ft.TfidfTransformer()
tfidf = tt.fit_transform(bow)
print(tfidf.shape)
# 交给朴素贝叶斯模型，进行训练
model = nb.MultinomialNB()
model.fit(tfidf, train.target)


# 自定义测试集进行测试
test_data = [
    'The curveballs of right handed pitchers tend to curve to the left',
    'Caesar cipher is an ancient form of encryption',
    'This two-wheeler is really good on slippery roads']
# 怎么训练的，就必须怎么预测
bow = cv.transform(test_data)
tfidf = tt.transform(bow)
pred_y = model.predict(tfidf)

for sent, index in zip(test_data, pred_y):
	print(sent, '->', train.target_names[index])