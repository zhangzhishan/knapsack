#!/usr/bin/env python
# coding=utf-8

import blind_greedy
import time
import json
import test

def consecutive_rollout(cap, weight=[], value=[], I=[]):
    S = []
    remaining_I = [i for i in I]
    remaining_cap = cap
    U = 0
    num = len(I)
    for i in range(num):
        #print i
        S1, U1 = blind_greedy.greedydp(remaining_cap, weight, value, remaining_I)
        #print U1
        remaining_I.remove(i) 
        S2, U2 = blind_greedy.greedydp(remaining_cap, weight, value, remaining_I)
        #print U2
        if U1 > U2:
            S.append(i)
            remaining_cap = remaining_cap - weight[i]
            U = U + value[i]
        #print remaining_I
    return S, U

def calcu_time():
    start = time.time()
    #print start
    #num = 100
    #cap = 10
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
    S, U = consecutive_rollout(cap, weight, value, I)

    #print time.time()
    print S
    print 'The total value:', U

    weight_sum = 0
    value_sum = 0
    #print '####'
    #print S, U
    #print '&&&&&&&&&&'
    for i in S:
        weight_sum += weight[i]
    print 'weight_sum: ', weight_sum
    #print cap, I, blind_greedy.critical_value(cap, weight, value, I)
    weight_plus = [i for i in weight]
    weight_plus.pop(0)
    weight_plus.append(0)
    value_plus = [i for i in value]
    value_plus.pop(0)
    value_plus.append(0)
#    print weight
#    print weight_plus
    gain = blind_greedy.critical_value(cap, weight_plus, value_plus, I) - blind_greedy.critical_value(cap, weight, value, I)
    if gain < 0:
        gain = 0
    print 'gain:', gain
    timeused = time.time() - start
    print 'time cost', timeused
    return gain

if __name__ == "__main__":
    for i in range(50):
        test.test(100,1)
    #        calcu_time()
        f = open('cr_result.txt', 'a')
        gap1 = calcu_time()
        print str(gap1)
        f.write(str(gap1) + '\n')
        f.close()
    
    #print time.clock()
