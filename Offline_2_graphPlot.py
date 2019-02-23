# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 15:25:13 2018

@author: sakib
"""

import matplotlib.pyplot as plt

x = [10, 100, 1000, 10000, 100000, 1000000]
y = [0, 0, 0, 54, 203, 2764]
p = [0, 0, 1, 13.29, 166.10, 1993.26]

plt.plot(x,y)
plt.plot(x, p)
plt.show()