# -*- coding: utf-8 -*-
import tushare as ts

df = ts.get_hist_data('600469')
df.to_csv('/Users/zhaolu/code/mygit/mycookcode/programming/py-data-science-learn/data/600469.csv',header=None)
