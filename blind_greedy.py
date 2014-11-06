#!/usr/bin/env python
# coding=utf-8

import time
import json


def greedydp(cap, weight=[], value=[], I=[]):
    S = []
    remaining_cap = cap
    U = 0
    for i in I:
        if weight[i] <= remaining_cap:
            S.append(i)
            remaining_cap = remaining_cap - weight[i]
            U = U + value[i]
        else:
            return S, U
    return S, U


def calcu_time():
    start = time.time()
    #print start
    #num = 100
    #cap = 10000
    f = open('weight.txt', 'r')
    weight = json.load(f)
    f.close()
    f = open('value.txt', 'r')
    value = json.load(f)
    f.close()
    f = open('cap.txt', 'r')
    cap = json.load(f)
    f.close()
    I = [i for i in range(len(weight))]
    S, U = greedydp(cap, weight, value, I)
    print S, U
    weight_sum = 0
    for i in S:
        weight_sum += weight[i]
    print 'weight_sum: ', weight_sum
    #print time.time()
    timeused = time.time() - start
    print '用时：', timeused

if __name__ == "__main__":
    calcu_time()
    #print time.clock()
