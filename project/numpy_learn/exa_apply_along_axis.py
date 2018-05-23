# -*- coding: utf-8 -*-

import numpy as np

def my_func(a):
    print '-----',a[0],'------',a[-1]
    return  (a[0] + a[-1]) * 0.5


b=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print np.apply_along_axis(my_func, 0, b)

print np.apply_along_axis(my_func, 1, b)
