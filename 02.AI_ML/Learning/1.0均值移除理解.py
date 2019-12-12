import math
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])

std_samples = sp.scale(raw_samples)
print(std_samples)
print(std_samples.mean(axis=0))
print(std_samples.std(axis=0))


def myscale(raw_samples):
    '''
    均值移除，是对每一个特征进行均值移除，对应位置返回给每一个样本的值。
    '''
    deal_samples = raw_samples.copy()
    for x in deal_samples.T:
        print('\n样本：', x)
        print('平均值', x.mean(), x-x.mean())
        print('标准差', math.sqrt(((x-x.mean())**2).sum() / len(x)))
        x = (x-x.mean()) / (math.sqrt(((x-x.mean())**2).sum() / len(x)))
        print('均值移除', x)
        print(deal_samples)
    return deal_samples


r = myscale(raw_samples)
print(r)
