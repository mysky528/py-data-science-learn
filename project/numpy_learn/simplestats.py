# -*- coding: utf-8 -*-
import numpy as np

import datetime

def datestr2num(s):
        #print datetime.datetime.strptime(s, "%Y-%m-%d").date().weekday()
        return datetime.datetime.strptime(s, "%Y-%m-%d").date().weekday()

'''
该函数将为每一周的数据返回一个元组，包含这一周的开盘价、
最高价、最低价和收盘价，类似于每天的盘后数据
'''
def summarize(a,o,h,l,c):
    monday_open = o[a[0]]
    week_high = np.max(np.take(h,a))
    week_low = np.min(np.take(l,a))
    friday_close = c[a[-1]]
    return("600469", monday_open, week_high, week_low, friday_close)
#-------------------------------------------------------------------------------
# 简单统计分析
#-------------------------------------------------------------------------------
# 计算收盘价的中位数
outpath = '/Users/zhaolu/code/mygit/mycookcode/programming/py-data-science-learn/output'
datapath = '/Users/zhaolu/code/mygit/mycookcode/programming/py-data-science-learn/data'
c = np.loadtxt(datapath+'/600469.csv',delimiter=',',skiprows=0,usecols=(3,),unpack=True)
print 'median =',np.median(c)
#获得排序后的数组
sorted_close = np.msort(c)
print 'sorted =',sorted_close
#计算收盘价的方差
print 'variance =',np.var(c)
print "variance from definition =", np.mean((c - c.mean())**2)
#-------------------------------------------------------------------------------
# 分析收益率
returns = np.diff(c)/c[:-1]
print '简单收益率=',returns
#计算简单收益率的标准差
print 'Standard deviation =',np.std(returns)
logreturns = np.diff(np.log(c))
print '对数收益率=',logreturns
#获得收益率为正的数组
posretindices = np.where(returns > 0)
print "Indices with positive returns", posretindices
#计算波动率:年波动 率等于对数收益率的标准差除以其均值，再除以交易日倒数的平方根，通常交易日取252天
annual_volatility = np.std(logreturns)/np.mean(logreturns)
annual_volatility = annual_volatility / np.sqrt(1./252.)
print '年波动率：',annual_volatility
#计算月波动率
print "Monthly volatility", annual_volatility * np.sqrt(1./12.)
#-------------------------------------------------------------------------------
# 分析日期数据
dates,open,high,low,close = np.loadtxt(datapath+'/600469.csv',delimiter=',',usecols=(0,3),converters={0:datestr2num},unpack=True)
#print "Dates =", dates
averages = np.zeros(5)

for i in range(5):
    indices = np.where(dates == i)
    #take函数可以按照这些索引值从数组中取出相应的元素
    prices = np.take(close, indices)
    avg = np.mean(prices)
    print "Day", i, "prices", prices, "Average", avg
    averages[i] = avg

top = np.max(averages)
print "Highest average", top
#argmax函数返回的是averages数组中最大元素的索引值
print "Top day of the week", np.argmax(averages)
bottom = np.min(averages)
print "Lowest average", bottom
#argmin函数返回的是averages数组中最小元素的索引值
print "Bottom day of the week", np.argmin(averages)
#-------------------------------------------------------------------------------
# 分析周数据 暂时考虑前三周的数据
close = close[:16]
dates = dates[:16]
print dates
first_monday = np.ravel(np.where(dates == 0))[-1]
print "The first Monday index is", first_monday
last_friday = np.ravel(np.where(dates == 4)) [0]
print "The last Friday index is", last_friday
#创建一个数组，用来存储三周内每天的索引值
weeks_indices = np.arange(last_friday,first_monday + 1)
print "Weeks indices initial", weeks_indices
#按照每个子数组5个元素，用split函数切分数组
weeks_indices = np.split(weeks_indices,3)
print "Weeks indices after split", weeks_indices
weeksummary = np.apply_along_axis(summarize,1,weeks_indices,open,high,low,close)
print "Week summary", weeksummary
