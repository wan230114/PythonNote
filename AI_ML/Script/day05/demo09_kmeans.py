import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp
import scipy.misc as sm

# 通过K均值聚类量化图像中的颜色
def quant(image, n_clusters):
	# x代表所有图片像素点的亮度值数组
    x = image.reshape(-1, 1)
    model = sc.KMeans(n_clusters=n_clusters)
    model.fit(x)
    # 每个像素的亮度所属的聚类类别标签： 0/1/2/3
    # y = [0,1,3,0,1,2,3,1,2,0,3,2,1,3,1,0,2...]
    y = model.labels_
    # 获取聚类中心 [30, 70, 110, 190]
    centers = model.cluster_centers_.ravel()
    return centers[y].reshape(image.shape)



original = sm.imread('../ml_data/lily.jpg', True)
quant4 = quant(original, 4)
quant3 = quant(original, 3)
quant2 = quant(original, 2)
mp.figure('Image Quant', facecolor='lightgray')
mp.subplot(221)
mp.title('Original', fontsize=16)
mp.axis('off')
mp.imshow(original, cmap='gray')
mp.subplot(222)
mp.title('Quant-4', fontsize=16)
mp.axis('off')
mp.imshow(quant4, cmap='gray')
mp.subplot(223)
mp.title('Quant-3', fontsize=16)
mp.axis('off')
mp.imshow(quant3, cmap='gray')
mp.subplot(224)
mp.title('Quant-2', fontsize=16)
mp.axis('off')
mp.imshow(quant2, cmap='gray')
mp.tight_layout()
mp.show()