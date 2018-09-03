# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tushare as ts

def get_max_min(code, start, end) :
    maxVal = 0.0
    minVal = 9999.0
    maxIndex = 0
    e = ts.get_hist_data(code, start=start, end=end)
    highSer = e.high
    lowSer = e.low
    count = highSer.size
    for index in range(0, count-1) :
        curVal = highSer[index]
        if curVal > maxVal :
            maxVal = curVal
            maxIndex = index
    count = lowSer.size       
    for index in range(0, count-1) :
        curVal = lowSer[index]
        if curVal < minVal :
            minVal = curVal
    return maxVal, minVal

for index in range(1, 938) :
    if index == 257 :
        continue
    code = '002' + '%03d'%index
    maxVal, minVal = get_max_min(code, '2017-08-10', '2018-08-31')
    if maxVal == 0 :
        print index,'no value'
    else :
        print index,maxVal, minVal, (maxVal - minVal)/maxVal
