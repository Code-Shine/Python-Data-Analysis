# 代码 6-17
## 加载所需的函数,
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
cancer = load_breast_cancer()
cancer_data = cancer['data']
cancer_target = cancer['target']
cancer_names = cancer['feature_names']
## 将数据划分为训练集测试集
cancer_data_train,cancer_data_test, \
cancer_target_train,cancer_target_test = \
train_test_split(cancer_data,cancer_target,test_size = 0.2,random_state = 22)
#print(cancer_target_test)
## 数据标准化
stdScaler = StandardScaler().fit(cancer_data_train)
cancer_trainStd = stdScaler.transform(cancer_data_train)
cancer_testStd = stdScaler.transform(cancer_data_test)
## 建立SVM模型
svm = SVC().fit(cancer_trainStd,cancer_target_train)## train  target
print('建立的SVM模型为：\n',svm)


## 预测训练集结果
cancer_target_pred = svm.predict(cancer_testStd)
print('预测前20个结果为：\n',cancer_target_pred[:20])


# 代码 6-18
## 求出预测和真实一样的数目
true = np.sum(cancer_target_pred == cancer_target_test )
print('预测对的结果数目为：', true)
print('预测错的的结果数目为：', cancer_target_test.shape[0]-true)
print('预测结果准确率为：', true/cancer_target_test.shape[0])

# 代码 6-19
from sklearn.metrics import accuracy_score,precision_score, \
recall_score,f1_score,cohen_kappa_score
print('使用SVM预测breast_cancer数据的准确率为：',
      accuracy_score(cancer_target_test,cancer_target_pred))
print('使用SVM预测breast_cancer数据的精确率为：',
      precision_score(cancer_target_test,cancer_target_pred))
print('使用SVM预测breast_cancer数据的召回率为：',
      recall_score(cancer_target_test,cancer_target_pred))
print('使用SVM预测breast_cancer数据的F1值为：',
      f1_score(cancer_target_test,cancer_target_pred))
print('使用SVM预测breast_cancer数据的Cohen’s Kappa系数为：',
      cohen_kappa_score(cancer_target_test,cancer_target_pred))



# 代码 6-20
from sklearn.metrics import classification_report
print('使用SVM预测iris数据的分类报告为：','\n',
      classification_report(cancer_target_test,
            cancer_target_pred))


# 代码 6-21
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
## 求出ROC曲线的x轴和y轴
fpr, tpr, thresholds = roc_curve(cancer_target_test,cancer_target_pred)
#fps和tps就是混淆矩阵中的FP和TP的值；thresholds就是 cancer_target_pred 逆序排列后的结果
# （由于保留的小数位数不同，所以表面上看上去不一样，其实是一样的）
print(fpr,'\n',tpr,'\n',thresholds)
plt.figure(figsize=(10,6))
plt.xlim(0,1) ##设定x轴的范围
plt.ylim(0.0,1.1) ## 设定y轴的范围
plt.xlabel('False Postive Rate')
plt.ylabel('True Postive Rate')
plt.plot(fpr,tpr,linewidth=2, linestyle="-",color='red')
plt.show()

# 代码 6-22
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
abalone = pd.read_csv('./data/abalone.data',sep=',')
## 将数据和标签拆开
abalone_data = abalone.iloc[:,:8]
abalone_target = abalone.iloc[:,8]
## 连续型特征离散化
sex = pd.get_dummies(abalone_data['sex'])
abalone_data = pd.concat([abalone_data,sex],axis = 1 )
abalone_data.drop('sex',axis = 1,inplace = True)
## 划分训练集，测试集
abalone_train,abalone_test, \
abalone_target_train,abalone_target_test = \
train_test_split(abalone_data,abalone_target,
      train_size = 0.8,random_state = 42)
## 标准化
stdScaler = StandardScaler().fit(abalone_train)
abalone_std_train = stdScaler.transform(abalone_train)
abalone_std_test = stdScaler.transform(abalone_test)
## 建模
svm_abalone = SVC().fit(abalone_std_train,abalone_target_train)
print('建立的SVM模型为：','\n',svm_abalone)

# 代码 6-23
abalone_target_pred = svm_abalone.predict(abalone_std_test)
print('abalone数据集的SVM分类报告为：\n',
      classification_report(abalone_target_test,abalone_target_pred))

# 代码 6-24
##加载所需函数
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
## 加载boston数据
boston = load_boston()
X = boston['data']
y = boston['target']
names = boston['feature_names']
## 将数据划分为训练集测试集
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state=125)
## 建立线性回归模型
clf = LinearRegression().fit(X_train,y_train)
print('建立的LinearRegression模型为：','\n',clf)

## 预测训练集结果
y_pred = clf.predict(X_test)
print('预测前20个结果为：','\n',y_pred[:20])


# 代码 6-25
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.sans-serif'] = 'SimHei'
fig = plt.figure(figsize=(10,6)) ##设定空白画布，并制定大小
##用不同的颜色表示不同数据
plt.plot(range(y_test.shape[0]),y_test,color="blue", linewidth=1.5, linestyle="-")
plt.plot(range(y_test.shape[0]),y_pred,color="red", linewidth=1.5, linestyle="-.")
plt.legend(['真实值','预测值'])
plt.savefig('./tmp/聚类结果.png')
plt.show() ##显示图片



# 代码 6-26
from sklearn.metrics import explained_variance_score,\
mean_absolute_error,\
mean_squared_error,\
median_absolute_error,r2_score
print('Boston数据线性回归模型的平均绝对误差为：',
     mean_absolute_error(y_test,y_pred))
print('Boston数据线性回归模型的均方误差为：',
     mean_squared_error(y_test,y_pred))
print('Boston数据线性回归模型的中值绝对误差为：',
     median_absolute_error(y_test,y_pred))
print('Boston数据线性回归模型的可解释方差值为：',
     explained_variance_score(y_test,y_pred))
print('Boston数据线性回归模型的R方值为：',
     r2_score(y_test,y_pred))


# 代码 6-27
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
house = pd.read_csv('./data/cal_housing.data',sep=',')
print(house.memory_usage())
house_data = house.iloc[:,:-1]
house_target = house.iloc[:,-1]
house_names = ['longitude','latitude',
    'housingMedianAge', 'totalRooms',
    'totalBedrooms','population',
    'households', 'medianIncome']
house_train,house_test,house_target_train,house_target_test = \
train_test_split(house_data,house_target,
    test_size = 0.2, random_state = 42)
GBR_house = GradientBoostingRegressor().fit(house_train,house_target_train)
print('建立的梯度提升回归模型为：','\n',GBR_house)

