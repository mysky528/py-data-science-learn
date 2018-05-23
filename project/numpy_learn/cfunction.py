#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
#-------------------------------------------------------------------------------
# NumPy中的常用函数
# 1.数组相关函数
# 2.从文件中载入数据
# 3.将数据写入文件
# 4.简单的数学和统计分析函数
#-------------------------------------------------------------------------------
# 读写文件
outpath = '/Users/zhaolu/code/mygit/mycookcode/programming/py-data-science-learn/output'
datapath = '/Users/zhaolu/code/mygit/mycookcode/programming/py-data-science-learn/data'
i2 = np.eye(2)
print i2
np.savetxt(outpath+'/eye.txt',i2)
#-------------------------------------------------------------------------------
# 读入csv文件
c,v = np.loadtxt(datapath+'/600469.csv',delimiter=',',skiprows=0,usecols=(3,5),unpack=True)
#print c,v
#-------------------------------------------------------------------------------
# 计算成交量加权平均价格
vwap = np.average(c,weights=v)
print 'vwap = ',vwap
#-------------------------------------------------------------------------------
# 算数平均值的计算
print "mean = ",np.mean(c)
#-------------------------------------------------------------------------------
# 找到最大和最小值
h,l = np.loadtxt(datapath+'/600469.csv',delimiter=',',skiprows=0,usecols=(2,4),unpack=True)
print "highest =",np.max(h)
print "lowest =", np.min(l)
#-------------------------------------------------------------------------------
# 返回数组中最大值和最小值的差值
print "Spread high price",np.ptp(h)
print "Spread low price",np.ptp(l)
