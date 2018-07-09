# -*- coding: utf-8 -*-
'''
股票相关性分析
'''
import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
datapath = '/Users/zhaolu/code/mygit/mycookcode/programming/py-data-science-learn/data'
N = int(sys.argv[1])
#读取风神股份股价 并取前N条记录
fsgf = np.loadtxt(datapath+'/600469_4.csv',delimiter=',',skiprows=0,usecols=(3,),unpack=True)
fsgf = fsgf[-N:]
fsgf = fsgf[::-1]
#计算风神股份收益率
fsgf_returns = np.diff(fsgf)/fsgf[:-1]
#读取三角轮胎股价 并取前N条记录
lglt = np.loadtxt(datapath+'/601163_4.csv',delimiter=',',skiprows=0,usecols=(3,),unpack=True)
lglt = lglt[-N:]
lglt = lglt[::-1]
#计算三角轮胎股票收益率
lglt_returns = np.diff(lglt)/lglt[:-1]
#计算收益率的协方差。使用cov函 数计算股票收益率的协方差矩阵
covariance = np.cov(fsgf_returns,lglt_returns)
print "Covariance", covariance
#使用diagonal函数查看对角线上的元素
print "Covariance diagonal", covariance.diagonal()
#使用trace函数计算矩阵的轨迹，即对角线上元素之和
print "Covariance trace", covariance.trace()
#两个向量的相关系数被定义为协方差除以各自标准差的乘积
print covariance/(fsgf_returns.std() * lglt_returns.std())
#使用相关系数来度量两只股票的相关程度。关系数的取值范围在-1到1之间。 根据定义，一组数值与自身的相关系数等于1。
print "Correlation coefficient", np.corrcoef(fsgf_returns, lglt_returns)

#计算两只股票的收盘价价差，判断两只股票的价格走势是否同步。
difference = fsgf - lglt
avg = np.mean(difference)
dev = np.std(difference)
#检查最后一次收盘价是否在同步状态
print "Out of sync", np.abs(difference[-1] - avg) >= 2 * dev
t = np.arange(len(fsgf_returns))
plot(t, fsgf_returns, lw=1)
plot(t, lglt_returns, lw=2)
show()
