# -*- coding: utf-8 -*-
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
'''
 计算真实波幅均值ATR
 n:计算的周期
 h:最高价
 l:最低价
 c:收盘价
 PATR:前一个交易日的ATR
 ATR计算公式：((N-1)PATR+TR)/N
'''
datapath = '/Users/zhaolu/code/mygit/mycookcode/programming/py-data-science-learn/data'

def calATR(n,h,l,c):
    #取最近20个交易日的最高价和最低价
    h = h[-n:]
    l = l[-n:]
    print "len(h)",len(h),"len(l)",len(l)
    print "Close",c
    #计算前一个交易日的收盘价
    previousclose = c[-n-1:-1]
    print "len(previousclose)", len(previousclose)
    print "Previous close", previousclose
    '''
    计算TR指标:
    1. h-l 当日股价范围
    2. h-previousclose 当日最高价和前一个交易日收盘价之差
    3. previousclose-l 前一个交易日和当日最低价之差
    4. 使用maximum函数计算三个数组之间的最大值
    '''
    truerange = np.maximum(h - l,h - previousclose,previousclose - l)
    print "True range", truerange
    #创建一个长度为n的数组atr,并初始化数组为0
    atr = np.zeros(n)
    atr[0] = np.mean(truerange)
    for i in range(1,n):
        atr[i] = (n-1)*atr[i-1] + truerange[i]
        atr[i]/=n
    print "ATR",atr,'atr数量：',len(atr)
    return atr


'''
计算简单移动平均线sma：
n:计算周期
c:收盘价
'''
def calSMA(n,c):
    #使用ones函数创建一个长度为N的元素均初始化为1的数组，然后对整个数组除以N，即 可得到权重
    weights = np.ones(n)/n
    print "weights",weights
    sma = np.convolve(weights,c)[n-1:-n+1]
    t = np.arange(n-1,len(c))
    return t,sma

if __name__ == "__main__":
    h,l,c = np.loadtxt(datapath+'/600469.csv',delimiter=',',skiprows=0,usecols=(2,4,3),unpack=True)
    calATR(20,h,l,c)
    t,sma = calSMA(20,c)
    plot(t,c[20-1:],lw=1.0)
    plot(t,sma,lw=2.0)
    show()
