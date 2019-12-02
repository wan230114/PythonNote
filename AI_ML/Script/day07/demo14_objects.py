'''
1. 读取training文件夹中的训练图片样本，
   每个图片对应一个desc矩阵，每个desc都有一个类别（car）。
2. 把所有类别为car的desc合并在一起，形成训练集。
	| desc |       |
	| desc | car   |
	| desc |       |
	.....
	由上述训练集样本可以训练一个用于匹配car的HMM。
3. 训练3个HMM分别对应每个物体类别。 保存在列表中。
4. 读取testing文件夹中的测试样本，整理测试样本
	| desc | car   |
	| desc | moto  |

5. 针对每一个测试样本：
   1. 分别使用3个HMM模型，对测试样本计算score得分。
   2. 取3个模型中得分最高的模型所属类别作为预测类别。
'''
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
train_objects = search_files('../ml_data/objects/training')
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
test_objects = search_files('../ml_data/objects/testing')
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
pred_y = []
for descs, test_label in zip(test_x, test_y):
    best_score, best_label = None, None
    for pred_label, model in models.items():
        score = model.score(descs)
        if (best_score==None) or (best_score<score):
            best_score = score
            best_label = pred_label
        print(test_label, '->', pred_label, score)
    pred_y.append(best_label)

print(test_y)
print(pred_y)