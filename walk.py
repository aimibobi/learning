'''
@Author: your name
@Date: 2020-05-25 17:21:46
@LastEditTime: 2020-05-25 18:00:45
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \opms\walk.py
'''
import numpy as np

nsteps = 1000
draws = np.random.randint(0,2,size=nsteps)
steps = np.where(draws>0,1,-1)
walk = steps.cumsum()
#print (steps)
#print (walk)