"""
demo05_speech.py  语音识别
1. 读取training文件夹中的训练音频样本，
   每个音频对应一个mfcc矩阵，每个mfcc都有一个类别（apple）。
2. 把所有类别为apple的mfcc合并在一起，形成训练集。
	| mfcc |       |
	| mfcc | apple |
	| mfcc |       |
	.....
	由上述训练集样本可以训练一个用于匹配apple的HMM。
3. 训练7个HMM分别对应每个水果类别。 保存在列表中。
4. 读取testing文件夹中的测试样本，针对每一个测试样本：
   1. 分别使用7个HMM模型，对测试样本计算score得分。
   2. 取7个模型中得分最高的模型所属类别作为预测类别。
"""

import os
import numpy as np
import scipy.io.wavfile as wf
import python_speech_features as sf
# import hmmlearn.hmm as hl

#1. 读取training文件夹中的训练音频样本，每个音频对应一个mfcc矩阵，每个mfcc都有一个类别（apple）。
def search_file(directory):
	# 使传过来的directory匹配当前操作系统
	# {'apple':[url, url, url ... ], 'banana':[...]}	
	directory = os.path.normpath(directory)
	objects = {}
	# curdir：当前目录 
	# subdirs: 当前目录下的所有子目录
	# files: 当前目录下的所有文件名
	for curdir, subdirs, files in os.walk(directory):
		for file in files:
			if file.endswith('.wav'):
				label = curdir.split(os.path.sep)[-1]
				if label not in objects:
					objects[label] = []
				# 把路径添加到label对应的列表中
				path = os.path.join(curdir, file)
				objects[label].append(path)
	return objects

#读取训练集数据
train_samples = \
	search_file('../ml_data/speeches/training')
print(train_samples)

'''
2. 把所有类别为apple的mfcc合并在一起，形成训练集。
	| mfcc |       |
	| mfcc | apple |
	| mfcc |       |
	.....
	由上述训练集样本可以训练一个用于匹配apple的HMM。
'''
train_x, train_y = [], []
# 遍历7次  apple/banana/...
for label, filenames in train_samples.items():
	mfccs = np.array([])
	for filename in filenames:
		sample_rate, sigs = wf.read(filename)
		mfcc = sf.mfcc(sigs, sample_rate)
		if len(mfccs)==0:
			mfccs = mfcc
		else:
			mfccs = np.append(mfccs, mfcc, axis=0)
	train_x.append(mfccs)
	train_y.append(label)
'''
train_x:
    ----------------
	| mfcc |       |
	| mfcc | apple |
	| mfcc |       |
	----------------
	| mfcc |        |
	| mfcc | banana |
	| mfcc |        |
	-----------------
	| mfcc |        |
	| mfcc | lime   |
	| mfcc |        |
	-----------------


'''
