#!/usr/bin/env python
# coding=utf-8

import time
import json
import test

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
#    print(critical_value(cap, weight, value, I))
    S, U = greedydp(cap, weight, value, I)
    print S
    print 'The total value:', U
#    print('$$$$\n')
    weight_sum = 0
    for i in S:
        weight_sum += weight[i]
#    print(cap)
#    print weight[i]
#    print weight_sum
    g = cap - weight_sum
    print 'gap: ', g
    print 'weight_sum: ', weight_sum
    # print time.time()
    timeused = time.time() - start
    print 'time cost', timeused
    return g

def critical_value(cap, weight=[], value=[], I=[]):
    S, U = greedydp(cap, weight, value, I)
    sum = 0
    j = 0
    for i in S:
        sum += value[i]
        j += 1
    #print '####' + str(sum) + '####'
    #print '$$$$$$$$' + str(value[j])
    return sum

if __name__ == "__main__":
    for i in range(50):
        test.test(100,20)
#        calcu_time()
        f = open('bg_result.txt', 'a')
        gap1 = calcu_time()
        print str(gap1)
        f.write(str(gap1) + '\n')
        f.close()
    #print time.clock()
