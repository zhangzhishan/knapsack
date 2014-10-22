#!/usr/bin/env python
# coding=utf-8
import time
import json

def greedydp(num, cap, weight = [], value = []):
    p = [0] * num
    q = [0] * num
    for i in range(num):
        p[i] = weight[i] / value[i]
        q[i] = i
    for i in range(num):
        j = i + 1
        while j > i and j < num:
            if p[i] > p[j]:
                t = q[i]
                q[i] = j
                q[j] = t
                t = p[i]
                p[i] = p[j]
                p [j] = t
            j += 1
    sumwei = sum = 0
    for i in range(num):
        for j in range(num):
            if p[j] == i:
                if weight[j] + sumwei <= cap:
                    sum += value[j]
                    sumwei += weight[j]
    return sum

start = time.clock()
num = 100
cap = 10000
f = open('weight.txt', 'r')
weight = json.load(f)
f.close()
f = open('value.txt', 'r')
value = json.load(f)
f.close()

print greedydp(num, cap, weight, value)
timeused = time.clock() - start
print '用时：', timeused


