# 案例，构建单颗决策树
# %% step01.导入模块或数据
import sklearn.datasets as sd  # 数据集datasets，数据质量经过处理的
import sklearn.utils as su  # 辅助工具，非学习模型
import sklearn.tree as st  # 决策树
import sklearn.ensemble as se  # 集合算法（聚合？）
import sklearn.metrics as sm  # 模型评估

boston = sd.load_boston()  # 关于美国房价的一组数据集
# 查看属性
print(boston.feature_names)
# |CRIM|ZN|INDUS|CHAS|NOX|RM|AGE|DIS|RAD|TAX|PTRATIO|B|LSTAT|
# 犯罪率|住宅用地比例|商业用地比例|是否靠河|空气质量|房间数|年限|距中心区距离|路网密度|房产税|师生比|黑人比例|低地位人口比例|
# 打乱原始数据集的输入和输出
# %% step02.数据预处理
# 训练之前，应将有序的数据打乱。否则训练时，可能只能用到一部分规律样本
# 1.指定随机种子(否则每次运行结果都不一样)，并同步打乱样本顺序
x, y = su.shuffle(boston.data, boston.target, random_state=7)
# 2.区分训练集和测试集
train_size = int(len(x) * 0.8)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:], \
    y[:train_size], y[train_size:]

# %% 03.训练
# 决策树回归器
model = st.DecisionTreeRegressor(max_depth=4)  # 只选择4列划分
model.fit(train_x, train_y)  # 训练
pred_test_y = model.predict(test_x)  # 预测
print(sm.r2_score(test_y, pred_test_y))

# %% 04.正向激励
# 基于决策树的正向激励回归器
model = se.AdaBoostRegressor(
    st.DecisionTreeRegressor(max_depth=4),
    n_estimators=400, random_state=7)  # 创建400个树
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
# %%
