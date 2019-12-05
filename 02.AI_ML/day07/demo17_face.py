"""
1. 读取样本图片数据，整理图片的路径列表
2. 读取每张图片，基于haar裁剪每张人脸，把人脸数据
   放入train_x，作为训练数据。
   在整理train_y时，由于Bob、Sala、Roy是字符串，
   需要把字符串做一个标签编码 LabelEncoder
3. 遍历训练集，把训练集交给LBPH人脸识别模型进行训练。

4. 读取测试集数据，整理图片的路径列表
5. 遍历每张图片，把图片中的人脸使用相同的方式裁剪，
   把人脸数据交给LBPH模型进行类别预测，得到预测结果。
6. 以图像的方式输出结果。
"""
import os
import numpy as np
import cv2 as cv
import sklearn.preprocessing as sp

fd = cv.CascadeClassifier('../ml_data/haar/face.xml')

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
    '../ml_data/faces/training')
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
'''
训练集结构：
   train_x  train_y
 -------------------
 | face    | 0     |
 -------------------
 | face    | 1     |
 -------------------
 | face    | 2     |
 -------------------
 | face    | 1     |
 -------------------
'''
# 局部二值模式直方图人脸识别分类器
model = cv.face.LBPHFaceRecognizer_create()
model.train(train_x, train_y)

# 测试
test_faces = search_faces(
    '../ml_data/faces/testing')
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

print(codec.inverse_transform(test_y))
print(codec.inverse_transform(pred_test_y))


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