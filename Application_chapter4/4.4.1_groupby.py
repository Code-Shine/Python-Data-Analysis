from sqlalchemy import create_engine
import numpy as np
import pandas as pd
## 创建一个mysql连接器，用户名为root，密码为1234
## 地址为127.0.0.1，数据库名称为testdb，编码为utf-8
engine = create_engine('mysql+pymysql://root:root@localhost/testdb?charset=utf8')
detail=pd.read_sql_table('meal_order_detail1',con = engine)
detailGroup = detail[['order_id','counts','amounts']].groupby(by = 'order_id')
print('分组后的订单详情表为：',detailGroup)

# 代码 4-52
print('订单详情表分组后前5组每组的均值为：\n', detailGroup.mean().head())
print('订单详情表分组后前5组每组的标准差为：\n', detailGroup.std().head())
print('订单详情表分组后前5组每组的大小为：','\n', detailGroup.size().head())

# 代码 4-53
print('test;',detail['counts'].agg(np.sum))
print('订单详情表的菜品销量与售价的和与均值为：\n',
      detail[['counts','amounts']].agg([np.sum,np.mean]))

# 代码 4-54
print('订单详情表的菜品销量总和与售价的均值为：\n',detail.agg({'counts':np.sum,'amounts':np.mean}))
print(detail.agg({'counts':np.sum,'amounts':[np.mean,np.sum]}))


# 代码 4-56
##自定义函数求两倍的和
def DoubleSum(data):
    s = data.sum() * 2
    return s
print('菜品订单详情表的菜品销量两倍总和为：', '\n',
      detail.agg({'counts': DoubleSum}, axis=0))


# 代码 4-57
##自定义函数求两倍的和
def DoubleSum1(data):
    s = np.sum(data) * 2
    return s

print('订单详情表的菜品销量两倍总和为：\n',detail.agg({'counts': DoubleSum1}, axis=0).head())
print('订单详情表的菜品销量与售价的和的两倍为：\n',detail[['counts','amounts']].agg(DoubleSum1))

# 代码 4-58
print('订单详情表分组后前3组每组的均值为：\n', detailGroup.agg(np.mean).head(3))
print('订单详情表分组后前3组每组的标准差为：\n', detailGroup.agg(np.std).head(3))

# 代码 4-59
print('订单详情分组前3组每组菜品总数和售价均值为：\n', detailGroup.agg({'counts':np.sum,'amounts':np.mean}).head(3))

# 代码 4-62
print('订单详情表的菜品销量与售价的两倍为：\n',detail[['counts','amounts']].transform(lambda x:x*2).head(4))
# 代码 4-63
print('订单详情表分组后实现组内离差标准化后前五行为：\n',
      detailGroup.transform(lambda x:(x.mean()-x.min())/(x.max()-x.min())).head())

detail['place_order_time'] = pd.to_datetime(detail['place_order_time'])
#print(detail['place_order_time'])
detail['date'] = [i.date() for i in detail['place_order_time']]
#print(detail['date'])
detailGroup = detail[['date','counts','amounts']].groupby(by='date')
print('订单详情表前5组每组的数目为：\n',detailGroup.size().head())

# 代码 4-65
dayMean = detailGroup.agg({'amounts':np.mean})
print('订单详情表前五组每日菜品均价为：\n',dayMean.head())

dayMedian = detailGroup.agg({'amounts':np.median})
print('订单详情表前五组每日菜品售价中位数为：\n',dayMedian.head())

daySaleSum=detailGroup.agg({'counts':np.sum}).head()
print('订单详情表前五组每日菜品售出数目为：\n',daySaleSum)



