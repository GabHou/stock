# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 14:11:14 2018

@author: Administrator
"""
import pandas as pd
"""
with open('peek_persent.txt','r') as f :
	lines = f.readlines()
	print type(lines[0].split())
	for line in lines :
		print line
"""

df = pd.read_csv('peek_persent.csv',header=None)
print df.sort_values(by=1)