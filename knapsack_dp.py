#!/usr/bin/env python
# coding=utf-8
import time
import json


def knapsack(num, cap, wei = [], val = []):
    d = [[i for i in range(cap + 1)]for j in range(num + 1)]
    wei.insert(0, 0)
    val.insert(0, 0)
    for i in range(num + 1):
        d[i][0] = 0
    for i in range(cap + 1):
        try:
            d[0][i] = 0
        except:
            pass
#            print i
    for i in range(1, num + 1):
        for j in range(1, cap + 1):
            d[i][j] = d[i - 1][j]
            if wei[i] <= j:
                temp = val[i] + d[i - 1][j - wei[i]]
                if temp > d[i - 1][j]:
                    d[i][j] = temp
    return d[num][cap]

start = time.clock()
num = 100
cap = 10000
f = open('weight.txt', 'r')
weight = json.load(f)
f.close()
f = open('value.txt', 'r')
value = json.load(f)
f.close()

print knapsack(num, cap, weight, value)
timeused = time.clock() - start
print '用时：', timeused

