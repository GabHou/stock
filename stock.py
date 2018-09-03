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
    if e is None :
        return 0, 0
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

def get_all_maxmin(codeType, start, end) :
	for index in range(start, end) :
		if index == 257 or index == 525 or index == 704 or index == 710 or index == 720 or index == 744:
			continue
    		code = codeType + '%03d'%index
		maxVal, minVal = get_max_min(code, '2017-08-10', '2018-08-31')
    		if maxVal == 0 :
        		print index,'no value'
    		else :
        		print index,maxVal, minVal, (maxVal - minVal)/maxVal

#get_all_maxmin('002', 745, 983) #983
get_all_maxmin('300', 1, 748)#1~748

#for test
#e = ts.get_hist_data('300061', start='2017-08-10', end='2018-08-31')
#if e is None :
#	print '++++++++++'
#print e == None
#n1, n2 = get_max_min('300060', '2017-08-10', '2018-08-31')
#print n1,n2
