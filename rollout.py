#!/usr/bin/env python
# coding=utf-8

import random
import json
import time

def sort2(num, weight = [], value = []):
    x = [[] for i in range(num)]
    #print x
    for i in range(num):
        x[i].append(weight[i])
        x[i].append(value[i])
        x[i].append(float(value[i])/weight[i])
    for i in range(num):
        for j in range(i, num):
            if x[i][2] < x[j][2]:
                t = x[i]
                x[i] = x[j]
                x[j] = t
    for i in range(num):
        weight[i] = x[i][0]
        value[i] = x[i][1]

    return weight, value

def greedy(num, cap, weight=[], value=[]):
#    weight, value = sort2(num, weight, value)
    sumwei = sum = 0
    for i in range(num):
        if weight[i] + sumwei <= cap:
            sum += value[i]
            sumwei += weight[i]
    return sum


def rollout(num, cap, weight=[], value=[]):
#    weight, value = sort2(num, weight, value)
#    print weight, value
    leftweight = [i for i in weight]
    leftvalue = [i for i in value]
    notchoose = [i for i in range(num)]
    choose = []
    choosenum = 1
    choosedig = -1
    choosevalue = 0
    summax = 0
    valueatlast = 0
    i = 0
#    print len(notchoose)
#    print notchoose
#    print value[4]
    for t in range(num):
#        print t
        flag = -1
        for i in notchoose:
#            print i
            flag += 1
            if weight[i] <= cap:
                cap -= weight[i]
                choose.append(i)
#                temp1 = leftvalue.index(value[i])
#                leftvalue.pop(temp1)  #采用此种方式有问题  考虑数组有重复情况
                leftvalue.pop(flag)
                leftweight.pop(flag) 
#                print value
#                print leftvalue
#                print str(i) + '*********'
#                print value[4]
#                print value[i]
                tempsum = choosevalue + value[i] + greedy(num - len(choose), cap, leftweight, leftvalue)
#                print '*** ', tempsum
                leftweight.insert(flag, weight[i])
                leftvalue.insert(flag, value[i])
                cap += weight[i]
                choose.pop()
                if tempsum >= summax:
                    summax = tempsum
                    choosedig = i
        if choosedig >= 0:
#                    print choosedig
                    choose.append(choosedig)
                    notchoose.remove(choosedig)
                    leftvalue.remove(value[choosedig])
                    leftweight.remove(weight[choosedig])
                    cap -= weight[choosedig]
                    choosevalue += value[choosedig]
                    choosedig = -1        
       
#    for i in choose:
#        valueatlast += value[i]
#    print valueatlast
#    print choose
    return summax

start = time.clock()
num = 100
cap = 10000
f = open('weight.txt', 'r')
weight = json.load(f)
f.close()
f = open('value.txt', 'r')
value = json.load(f)
f.close()

print rollout(num, cap, weight, value)
timeused = time.clock() - start
print '用时：', timeused
