#!/usr/bin/env python
# coding=utf-8

import blind_greedy
import time
import json

def exhaustive_rollout(cap, weight=[], value=[], I=[]):
    S = []
    remaining_I = [i for i in I]
    remaining_cap = cap
    U = 0
    record = []
    num = len(I)
    for t in range(num):
        Ui = []
        for i in remaining_I:
        #if t == 1:
            #print 'ddddddddddd' 
            temp_I = [j for j in remaining_I]
            #print temp_I
            #print '%%' + str(i)
            #print temp_I
                #dd = temp_I.index(i)
                #print dd
            temp_I.pop(temp_I.index(i))
                #print remaining_I[remaining_I.index(i)]
            remaining_I_i_first = [remaining_I[remaining_I.index(i)]] + temp_I
            #print remaining_I_i_first
            #Ui.append(blind_greedy.greedydp(remaining_cap, weight, value, remaining_I_i_first))
            Si, temp_Ui = blind_greedy.greedydp(remaining_cap, weight, value, remaining_I_i_first)
            Ui.append(temp_Ui)
            record.append(i)
        #print max(Ui)
        if max(Ui) > 0:
            #print '****'
            i_star = record[Ui.index(max(Ui))]
            k = remaining_I[i_star]
            S.append(k)
            remaining_I = remaining_I[0:i_star] + remaining_I[i_star + 1:]
            remaining_cap = remaining_cap - weight[k]
            U = U + value[k]
            #print i_star
    #print remaining_I
    S = [i for i in I if i not in remaining_I]

    return S, U

def calcu_time():
    start = time.time()
    #print start
    num = 100
    cap = 10000
    f = open('weight.txt', 'r')
    weight = json.load(f)
    f.close()
    f = open('value.txt', 'r')
    value = json.load(f)
    f.close()
    I = [i for i in range(num)]
    print exhaustive_rollout(cap, weight, value, I)
    #print time.time()
    timeused = time.time() - start
    print '用时：', timeused

if __name__ == "__main__":
    calcu_time()
    #print time.clock()




