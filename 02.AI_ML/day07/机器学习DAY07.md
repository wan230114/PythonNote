### 自然语言处理（NLP）

#### nltk分类器

nltk提供了朴素贝叶斯分类器方便的处理自然语言相关的分类问题，并且可以自动处理词袋，完成TFIDF矩阵的整理，完成模型训练，最终实现类别预测。使用方法如下：

```python
import nltk.classify as cf
import nltk.classify.util as cu
'''
train_data的格式不再是样本矩阵，nltk要求的数据格式如下：
[ ({'How': 1, 'are': 1, 'you': 1}, 'ask'),
  ({'fine': 1, 'Thanks': 2}, 'answer') ]
'''
# 基于朴素贝叶斯分类器训练测试数据 
model = cf.NaiveBayesClassifier.train(train_data)
ac = cu.accuracy(model, test_data)
print(ac)
```

#### 情感分析

分析语料库中movie_reviews文档，通过正面及负面评价进行自然语言训练，实现情感分析。

```python
import nltk.corpus as nc
import nltk.classify as cf
import nltk.classify.util as cu
pdata = []

# pos文件夹中的每个文件的路径
fileids = nc.movie_reviews.fileids('pos')
# 整理所有正面评论单词，存入pdata列表
for fileid in fileids:
    sample = {}
    words = nc.movie_reviews.words(fileid)
    for word in words:
        sample[word] = True
    pdata.append((sample, 'POSITIVE'))
# 整理所有正面评论单词，存入ndata列表
ndata = []
fileids = nc.movie_reviews.fileids('neg')
for fileid in fileids:
    sample = {}
    words = nc.movie_reviews.words(fileid)
    for word in words:
        sample[word] = True
    ndata.append((sample, 'NEGATIVE'))

# 拆分测试集与训练集数量（80%作为训练集）
pnumb, nnumb = int(0.8 * len(pdata)), int(0.8 * len(ndata))
train_data = pdata[:pnumb] + ndata[:nnumb]
test_data = pdata[pnumb:] + ndata[nnumb:]
# 基于朴素贝叶斯分类器训练测试数据 
model = cf.NaiveBayesClassifier.train(train_data)
ac = cu.accuracy(model, test_data)
print(ac)

# 模拟业务场景
reviews = [
    'It is an amazing movie.',
    'This is a dull movie. I would never recommend it to anyone.',
    'The cinematography is pretty great in this movie.',
    'The direction was terrible and the story was all over the place.']
sents, probs = [], []
for review in reviews:
    sample = {}
    words = review.split()
    for word in words:
        sample[word] = True
    pcls = model.classify(sample)
    print(review, '->', pcls)
```

#### 主题抽取

经过分词、单词清洗、词干提取后，基于TF-IDF算法可以抽取一段文本中的核心主题词汇，从而判断出当前文本的主题。属于无监督学习。gensim模块提供了主题抽取的常用工具 。

主题抽取相关API：

```python
import gensim.models.ldamodel as gm
import gensim.corpora as gc

# 把lines_tokens中出现的单词都存入gc提供的词典对象，对每一个单词做编码。
line_tokens = ['hello', 'world', ...]
dic = gc.Dictionary(line_tokens)
# 通过字典构建词袋
bow = dic.doc2bow(line_tokens) 

# 构建LDA模型
# bow: 词袋
# num_topics: 分类数
# id2word: 词典
# passes: 每个主题保留的最大主题词个数
model = gm.LdaModel(bow, num_topics=n_topics, id2word=dic, passes=25)
# 输出每个类别中对类别贡献最大的4个主题词
topics = model.print_topics(num_topics=n_topics, num_words=4)
```

案例：

```python
import nltk.tokenize as tk
import nltk.corpus as nc
import nltk.stem.snowball as sb
import gensim.models.ldamodel as gm
import gensim.corpora as gc
doc = []
with open('../data/topic.txt', 'r') as f:
    for line in f.readlines():
        doc.append(line[:-1])
tokenizer = tk.WordPunctTokenizer() 
stopwords = nc.stopwords.words('english')
signs = [',', '.', '!']
stemmer = sb.SnowballStemmer('english')
lines_tokens = []
for line in doc:
    tokens = tokenizer.tokenize(line.lower())
    line_tokens = []
    for token in tokens:
        if token not in stopwords and token not in signs:
            token = stemmer.stem(token)
            line_tokens.append(token)
    lines_tokens.append(line_tokens)
# 把lines_tokens中出现的单词都存入gc提供的词典对象，对每一个单词做编码。
dic = gc.Dictionary(lines_tokens)
# 遍历每一行，构建词袋列表
bow = []
for line_tokens in lines_tokens:
    row = dic.doc2bow(line_tokens)
    bow.append(row)
n_topics = 2
# 通过词袋、分类数、词典、每个主题保留的最大主题词个数构建LDA模型
model = gm.LdaModel(bow, num_topics=n_topics, id2word=dic, passes=25)
# 输出每个类别中对类别贡献最大的4个主题词
topics = model.print_topics(num_topics=n_topics, num_words=4)
print(topics)
```

### 语音识别

声音的本质是震动，震动的本质是位移关于时间的函数，波形文件(.wav)中记录了不同采样时刻的位移。

通过傅里叶变换，可以将时间域的声音函数分解为一系列不同频率的正弦函数的叠加，通过频率谱线的特殊分布，建立音频内容和文本的对应关系，以此作为模型训练的基础。

案例：

```python
import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf
import matplotlib.pyplot as mp

sample_rate, sigs = wf.read('../data/freq.wav')
print(sample_rate)
print(sigs.shape, sigs.dtype)
sigs = sigs / 2 ** 15
times = np.arange(len(sigs)) / sample_rate
freqs = nf.fftfreq(sigs.size, 1 / sample_rate)
ffts = nf.fft(sigs)
pows = np.abs(ffts)
mp.figure('Audio', facecolor='lightgray')
mp.subplot(121)
mp.title('Time Domain', fontsize=16)
mp.xlabel('Time', fontsize=12)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times, sigs, c='dodgerblue', label='Signal')
mp.legend()
mp.subplot(122)
mp.title('Frequency Domain', fontsize=16)
mp.xlabel('Frequency', fontsize=12)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(freqs[freqs >= 0], pows[freqs >= 0], c='orangered', label='Power')
mp.legend()
mp.tight_layout()
mp.show()
```

#### 语音识别

梅尔频率倒谱系数(MFCC)通过与声音内容密切相关的13个特殊频率所对应的能量分布，可以使用梅尔频率倒谱系数矩阵作为语音识别的特征。基于隐马尔科夫模型进行模式识别，找到测试样本最匹配的声音模型，从而识别语音内容。

梅尔频率倒谱系数相关API：

```python
import scipy.io.wavfile as wf
import python_speech_features as sf

sample_rate, sigs = wf.read('../data/freq.wav')
mfcc = sf.mfcc(sigs, sample_rate)
```

案例：

```python -m pip install python_speech_features```

```python
"""
demo04_mfcc.py  mfcc矩阵
"""
import scipy.io.wavfile as wf
import python_speech_features as sf
import matplotlib.pyplot as mp

sample_rate, sigs = wf.read(
	'../ml_data/speeches/training/banana/banana01.wav')
mfcc = sf.mfcc(sigs, sample_rate)

mp.matshow(mfcc.T, cmap='gist_rainbow')
mp.show()
```

隐马尔科夫模型相关API：

```python
import hmmlearn.hmm as hl
# n_components: 用几个高斯分布函数拟合样本数据
# covariance_type: 相关矩阵的辅对角线进行相关性比较
# n_iter: 最大迭代上限
model = hl.GaussianHMM(n_components=4, covariance_type='diag', n_iter=1000)
model.fit(mfccs)
# 使用模型匹配测试mfcc矩阵的分值
score = model.score(test_mfccs)
```

案例：训练training文件夹下的音频，对testing文件夹下的音频文件做分类

```python

```

#### 声音合成

根据需求获取某个声音的模型频域数据，根据业务需要可以修改模型数据，逆向生成时域数据，完成声音的合成。

案例：

```python
import json
import numpy as np
import scipy.io.wavfile as wf
with open('../data/12.json', 'r') as f:
    freqs = json.loads(f.read())
tones = [
    ('G5', 1.5),
    ('A5', 0.5),
    ('G5', 1.5),
    ('E5', 0.5),
    ('D5', 0.5),
    ('E5', 0.25),
    ('D5', 0.25),
    ('C5', 0.5),
    ('A4', 0.5),
    ('C5', 0.75)]
sample_rate = 44100
music = np.empty(shape=1)
for tone, duration in tones:
    times = np.linspace(0, duration, duration * sample_rate)
    sound = np.sin(2 * np.pi * freqs[tone] * times)
    music = np.append(music, sound)
music *= 2 ** 15
music = music.astype(np.int16)
wf.write('../data/music.wav', sample_rate, music)
```

### 图像识别

#### OpenCV基础

OpenCV是一个开源的计算机视觉库。提供了很多图像处理常用的工具。

案例：

```python
import numpy as np
import cv2 as cv
# 读取图片并显示
original = cv.imread('../data/forest.jpg')
cv.imshow('Original', original)
# 显示图片某个颜色通道的图像
blue = np.zeros_like(original)
blue[:, :, 0] = original[:, :, 0]  # 0 - 蓝色通道
cv.imshow('Blue', blue)
green = np.zeros_like(original)
green[:, :, 1] = original[:, :, 1]  # 1 - 绿色通道
cv.imshow('Green', green)
red = np.zeros_like(original)
red[:, :, 2] = original[:, :, 2]  # 2 - 红色通道
cv.imshow('Red', red)
# 图像裁剪
h, w = original.shape[:2]
l, t = int(w / 4), int(h / 4)
r, b = int(w * 3 / 4), int(h * 3 / 4)
cropped = original[t:b, l:r]
cv.imshow('Cropped', cropped)
#图像缩放 interpolation=线型插值
scaled1 = cv.resize(original, (int(w / 4), int(h / 4)),
    interpolation=cv.INTER_LINEAR)
cv.imshow('Scaled1', scaled1)
scaled2 = cv.resize(
    scaled1, None, fx=4, fy=4,
    interpolation=cv.INTER_LINEAR)
cv.imshow('Scaled2', scaled2)
cv.waitKey()
# 图像文件保存
cv.imwrite('../../data/blue.jpg', blue)
cv.imwrite('../../data/green.jpg', green)
cv.imwrite('../../data/red.jpg', red)
cv.imwrite('../../data/cropped.jpg', cropped)
cv.imwrite('../../data/scaled1.jpg', scaled1)
cv.imwrite('../../data/scaled2.jpg', scaled2)
```

#### 边缘检测

物体的边缘检测是物体识别常用的手段。边缘检测常用亮度梯度方法。通过识别亮度梯度变化最大的像素点从而检测出物体的边缘。

常用边缘检测算法相关API：

```python
# 索贝尔边缘识别
# cv.CV_64F：卷积运算使用数据类型为64位浮点型（保证微分的精度）
# 1：水平方向索贝尔偏微分
# 0：垂直方向索贝尔偏微分
# ksize：卷积核为5*5的方阵
cv.Sobel(original, cv.CV_64F, 1, 0, ksize=5)
# 拉普拉斯边缘识别
cv.Laplacian(original, cv.CV_64F)
# Canny边缘识别
# 50:水平方向阈值  240:垂直方向阈值
cv.Canny(original, 50, 240)
```

案例：

```python
import cv2 as cv

original = cv.imread( '../data/chair.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('Original', original)
hsobel = cv.Sobel(original, cv.CV_64F, 1, 0, ksize=5)
cv.imshow('H-Sobel', hsobel)
vsobel = cv.Sobel(original, cv.CV_64F, 0, 1, ksize=5)
cv.imshow('V-Sobel', vsobel)
sobel = cv.Sobel(original, cv.CV_64F, 1, 1, ksize=5)
cv.imshow('Sobel', sobel)
laplacian = cv.Laplacian(original, cv.CV_64F)
cv.imshow('Laplacian', laplacian)
canny = cv.Canny(original, 50, 240)
cv.imshow('Canny', canny)
cv.waitKey()

```

#### 亮度提升

OpenCV提供了直方图均衡化的方式实现亮度提升，更有利于边缘识别与物体识别模型的训练。

OpenCV直方图均衡化相关API：

```python
# 彩色图转为灰度图
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
# 直方图均衡化
equalized_gray = cv.equalizeHist(gray)
```

案例：

```python
import cv2 as cv

original = cv.imread('../../data/sunrise.jpg')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
equalized_gray = cv.equalizeHist(gray)
cv.imshow('Equalized Gray', equalized_gray)
# YUV：亮度，色度，饱和度
yuv = cv.cvtColor(original, cv.COLOR_BGR2YUV)
yuv[..., 0] = cv.equalizeHist(yuv[..., 0])
equalized_color = cv.cvtColor(yuv, cv.COLOR_YUV2BGR)
cv.imshow('Equalized Color', equalized_color)
cv.waitKey()
```

#### 角点检测

平直棱线的交汇点（颜色梯度方向改变的像素点的位置）

OpenCV提供的角点检测相关API：

```python
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
# Harris角点检测器
# 边缘水平方向、垂直方向颜色值改变超过阈值7、5时即为边缘
# 边缘线方向改变超过阈值0.04弧度即为一个角点。
corners = cv.cornerHarris(gray, 7, 5, 0.04)
```

案例：

```python
import cv2 as cv

original = cv.imread('../data/box.png')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
corners = cv.cornerHarris(gray, 7, 5, 0.04)
mixture = original.copy()
mixture[corners > corners.max() * 0.01] = [0, 0, 255]
cv.imshow('Corner', mixture)
cv.waitKey()
```

### 图像识别

#### 特征点检测

常用特征点检测有：STAR特征点检测 / SIFT特征点检测

特征点检测结合了边缘检测与角点检测从而识别出图形的特征点。

STAR特征点检测相关API如下：

```python
import cv2 as cv
# 创建STAR特征点检测器
star = cv.xfeatures2d.StarDetector_create()
# 检测出gray图像所有的特征点
keypoints = star.detect(gray)
# drawKeypoints方法可以把所有的特征点绘制在mixture图像中
cv.drawKeypoints(original, keypoints, mixture,
    			 flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('Mixture', mixture)
```

案例：

```python
import cv2 as cv
original = cv.imread('../data/table.jpg')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
star = cv.xfeatures2d.StarDetector_create()
keypoints = star.detect(gray)
mixture = original.copy()
cv.drawKeypoints(
    original, keypoints, mixture,
    flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('Mixture', mixture)
cv.waitKey()
```

SIFT特征点检测相关API：

```python
import cv2 as cv

# 创建SIFT特征点检测器
sift = cv.xfeatures2d.SIFT_create()
keypoints = sift.detect(gray)
```

案例：

```python
import cv2 as cv

original = cv.imread('../data/table.jpg')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
sift = cv.xfeatures2d.SIFT_create()
keypoints = sift.detect(gray)
mixture = original.copy()
cv.drawKeypoints(original, keypoints, mixture,
    flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('Mixture', mixture)
cv.waitKey()
```

#### 特征值矩阵

图像特征值矩阵（描述）记录了图像的特征点以及每个特征点的梯度信息，相似图像的特征值矩阵也相似。这样只要有足够多的样本，就可以基于隐马尔科夫模型进行图像内容的识别。

特征值矩阵相关API：

```python
sift = cv.xfeatures2d.SIFT_create()
keypoints = sift.detect(gray)
_, desc = sift.compute(gray, keypoints)
```

案例：

```python
import cv2 as cv

import matplotlib.pyplot as mp
original = cv.imread('../data/table.jpg')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
sift = cv.xfeatures2d.SIFT_create()
keypoints = sift.detect(gray)
_, desc = sift.compute(gray, keypoints)
print(desc.shape)
mp.matshow(desc, cmap='jet', fignum='Description')
mp.title('Description', fontsize=20)
mp.xlabel('Feature', fontsize=14)
mp.ylabel('Sample', fontsize=14)
mp.tick_params(which='both', top=False, labeltop=False, labelbottom=True, labelsize=10)
mp.show()
```

#### 物体识别

```python
import os
import numpy as np
import cv2 as cv
import hmmlearn.hmm as hl

def search_files(directory):
    directory = os.path.normpath(directory)

    objects = {}
    for curdir, subdirs, files in os.walk(directory):
        for file in files:
            if(file.endswith('.jpg')):
                label = curdir.split(os.path.sep)[-1]
                if label not in objects:
                    objects[label] = []
                path = os.path.join(curdir, file)
                objects[label].append(path)
    return objects
	
#加载训练集样本数据，训练模型，模型存储
train_objects = search_files('../data/objects/training')
train_x, train_y = [], []
for label, filenames in train_objects.items():
    descs = np.array([])
    for filename in filenames:
        image = cv.imread(filename)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        #范围缩放，使特征描述矩阵样本数量一致
        h, w = gray.shape[:2]
        f = 200 / min(h, w)
        gray = cv.resize(gray, None, fx=f, fy=f)
        sift = cv.xfeatures2d.SIFT_create()
        keypoints = sift.detect(gray)
        _, desc = sift.compute(gray, keypoints)
        if len(descs) == 0:
            descs = desc
        else:
            descs = np.append(descs, desc, axis=0)
    train_x.append(descs)
    train_y.append(label)
models = {}
for descs, label in zip(train_x, train_y):
    model = hl.GaussianHMM(n_components=4, covariance_type='diag', n_iter=100)
    models[label] = model.fit(descs)


#测试模型
test_objects = search_files('../data/objects/testing')
test_x, test_y = [], []
for label, filenames in test_objects.items():
    descs = np.array([])
    for filename in filenames:
        image = cv.imread(filename)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        sift = cv.xfeatures2d.SIFT_create()
        keypoints = sift.detect(gray)
        _, desc = sift.compute(gray, keypoints)
        if len(descs) == 0:
            descs = desc
        else:
            descs = np.append(descs, desc, axis=0)
    test_x.append(descs)
    test_y.append(label)

# 遍历所有测试样本  使用model匹配测试样本查看每个模型的匹配分数
for descs, test_label in zip(test_x, test_y):
    for pred_label, model in models.items():
        score = model.score(descs)
        print(test_label, '->', pred_label, score)
```

### 人脸识别

人脸识别与图像识别的区别在于人脸识别需要识别出两个人的不同点。 

#### 视频捕捉

通过OpenCV访问视频捕捉设备（视频头），从而获取图像帧。

视频捕捉相关API：

```python
import cv2 as cv

# 获取视频捕捉设备
video_capture = cv.VideoCapture(0)
# 读取一帧
frame = video_capture.read()[1]
cv.imshow('VideoCapture', frame)
# 释放视频捕捉设备
video_capture.release()
# 销毁cv的所有窗口
cv.destroyAllWindows()
```

案例：

```python
import cv2 as cv
vc = cv.VideoCapture(0)
while True:
    frame = vc.read()[1]
    cv.imshow('VideoCapture', frame)
    if cv.waitKey(33) == 27:
        break
vc.release()
cv.destroyAllWindows()
```

#### 人脸定位

哈尔级联人脸定位

```python
import cv2 as cv
# 通过特征描述文件构建哈尔级联人脸识别器
fd = cv.CascadeClassifier('../data/haar/face.xml')
# 从一个图像中识别出所有的人脸区域
# 	1.3：为最小的人脸尺寸
# 	5：最多找5张脸
# 返回：
# 	faces: 抓取人脸（矩形区域）列表 [(l,t,w,h),(),()..]
faces = fd.detectMultiScale(frame, 1.3, 5)
face = faces[0] # 第一张脸
# 绘制椭圆
cv.ellipse(
    face, 				# 图像
    (l + a, t + b), 	# 椭圆心
    (a, b), 			# 半径
    0, 					# 椭圆旋转角度
    0, 360, 			# 起始角, 终止角
    (255, 0, 255), 		# 颜色
    2					# 线宽
)
```

案例：

```python
import cv2 as cv
# 哈尔级联人脸定位器
fd = cv.CascadeClassifier('../../data/haar/face.xml')
ed = cv.CascadeClassifier('../../data/haar/eye.xml')
nd = cv.CascadeClassifier('../../data/haar/nose.xml')
vc = cv.VideoCapture(0)
while True:
    frame = vc.read()[1]
    faces = fd.detectMultiScale(frame, 1.3, 5)
    for l, t, w, h in faces:
        a, b = int(w / 2), int(h / 2)
        cv.ellipse(frame, (l + a, t + b), (a, b), 0, 0, 360, (255, 0, 255), 2)
        face = frame[t:t + h, l:l + w]
        eyes = ed.detectMultiScale(face, 1.3, 5)
        for l, t, w, h in eyes:
            a, b = int(w / 2), int(h / 2)
            cv.ellipse(face, (l + a, t + b), (a, b), 0, 0, 360, (0, 255, 0), 2)
        noses = nd.detectMultiScale(face, 1.3, 5)
        for l, t, w, h in noses:
            a, b = int(w / 2), int(h / 2)
            cv.ellipse(face, (l + a, t + b), (a, b), 0, 0, 360, (0, 255, 255), 2)
    cv.imshow('VideoCapture', frame)
    if cv.waitKey(33) == 27:
        break
vc.release()
cv.destroyAllWindows()
```

#### 人脸识别

简单人脸识别：OpenCV的LBPH(局部二值模式直方图)

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import numpy as np
import cv2 as cv
import sklearn.preprocessing as sp
fd = cv.CascadeClassifier('../../data/haar/face.xml')


def search_faces(directory):
    directory = os.path.normpath(directory)

    faces = {}
    for curdir, subdirs, files in os.walk(directory):
        for jpeg in (file for file in files
                     if file.endswith('.jpg')):
            path = os.path.join(curdir, jpeg)
            label = path.split(os.path.sep)[-2]
            if label not in faces:
                faces[label] = []
            faces[label].append(path)
    return faces


train_faces = search_faces(
    '../../data/faces/training')
codec = sp.LabelEncoder()
codec.fit(list(train_faces.keys()))
train_x, train_y = [], []
for label, filenames in train_faces.items():
    for filename in filenames:
        image = cv.imread(filename)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        faces = fd.detectMultiScale(gray, 1.1, 2,
                                    minSize=(100, 100))
        for l, t, w, h in faces:
            train_x.append(
                gray[t:t + h, l:l + w])
            train_y.append(
                codec.transform([label])[0])
train_y = np.array(train_y)
# 局部二值模式直方图人脸识别分类器
model = cv.face.LBPHFaceRecognizer_create()
model.train(train_x, train_y)
test_faces = search_faces(
    '../../data/faces/testing')
test_x, test_y, test_z = [], [], []
for label, filenames in test_faces.items():
    for filename in filenames:
        image = cv.imread(filename)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        faces = fd.detectMultiScale(gray, 1.1, 2,
                                    minSize=(100, 100))
        for l, t, w, h in faces:
            test_x.append(
                gray[t:t + h, l:l + w])
            test_y.append(
                codec.transform([label])[0])
            a, b = int(w / 2), int(h / 2)
            cv.ellipse(image, (l + a, t + b),
                       (a, b), 0, 0, 360,
                       (255, 0, 255), 2)
            test_z.append(image)
test_y = np.array(test_y)
pred_test_y = []
for face in test_x:
    pred_code = model.predict(face)[0]
    pred_test_y.append(pred_code)
escape = False
while not escape:
    for code, pred_code, image in zip(
            test_y, pred_test_y, test_z):
        label, pred_label = \
            codec.inverse_transform([code, pred_code])
        text = '{} {} {}'.format(
            label,
            '==' if code == pred_code else '!=',
            pred_label)
        cv.putText(image, text, (10, 60),
                   cv.FONT_HERSHEY_SIMPLEX, 2,
                   (255, 255, 255), 6)
        cv.imshow('Recognizing...', image)
        if cv.waitKey(1000) == 27:
            escape = True
            break
```

