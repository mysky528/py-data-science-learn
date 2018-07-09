# -*- coding: utf-8 -*-
import numpy as np
import sys

datapath = '/Users/zhaolu/code/mygit/mycookcode/programming/py-data-science-learn/data'
N = int(sys.argv[1])

h,l,c = np.loadtxt(datapath+'/600469_3.csv',delimiter=',',skiprows=0,usecols=(2,4,3),unpack=True)
#获得包含N个股价的向量b
b = c[-N:]
b = b[::-1]
print b
#初始化一个N*N的二维数组A，元素全部为0
A = np.zeros((N,N),float)
print "Zeros N by N", A
#使用b向量中的n个股价填充数组A
for i in range(N):
      A[i, ] = c[-N - 1 - i: - 1 - i]

print "A",A
#返回值为系数向量x、残差数组、A的秩以及A的奇异值
(x,residuals,rank,s) = np.linalg.lstsq(A,b)
print x,residuals,rank,s
#dot函数计算系数向量与最近N个价格构成的线性组合
print np.dot(b,x)
