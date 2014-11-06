#!/usr/bin/env python
# coding=utf-8

import blind_greedy
import time
import json

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
    print S, U
    sum = 0
    for i in S:
        sum += weight[i]
    print sum
    timeused = time.time() - start
    print 'time cost', timeused

if __name__ == "__main__":
    calcu_time()
    #print time.clock()
