#!/usr/bin/env python
# coding=utf-8

import blind_greedy
import time
import json
import test

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
            temp_I = [j for j in remaining_I]
            temp_I.pop(temp_I.index(i))
            remaining_I_i_first = [remaining_I[remaining_I.index(i)]] + temp_I
            Si, temp_Ui = blind_greedy.greedydp(remaining_cap, weight, value, remaining_I_i_first)
            Ui.append(temp_Ui)
            record.append(i)
        if max(Ui) > 0:
            i_star = record[Ui.index(max(Ui))]
            k = remaining_I[i_star]
            S.append(k)
            remaining_I = remaining_I[0:i_star] + remaining_I[i_star + 1:]
            remaining_cap = remaining_cap - weight[k]
            U = U + value[k]
    S = [i for i in I if i not in remaining_I]
    return S, U

def calcu_time():
    start = time.time()
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
    S, U = exhaustive_rollout(cap, weight, value, I)
    print S
    print 'The total value:', U
    weight_sum = 0
    value_sum = 0
    for i in S:
        weight_sum += weight[i]
    print 'weight_sum: ', weight_sum
    max = 0
    #print cap, I, blind_greedy.critical_value(cap, weight, value, I)
    for i in range(len(I)):
        copy_weight = []
        copy_value = []
        copy_weight.append(weight[i])
        copy_value.append(value[i])
        for j in I:
            if j != i:
                copy_weight.append(weight[j])
                copy_value.append(value[j])
        gain = blind_greedy.critical_value(cap, copy_weight, copy_value, I) - \
                                               blind_greedy.critical_value(cap, weight, value, I)
        if gain > max:
            max = gain        
#        if i == 2:
#            print copy_weight
#            print copy_value
#        copy_weight.extend([weight[j] for j in I and j != i)
        
    
    print 'gain:', max
    timeused = time.time() - start
    print 'time_used:', timeused
    return max

if __name__ == "__main__":
    f = open('er_result.txt', 'w')
    for i in range(50):
            test.test(50,10)
        #        calcu_time()
            
            gap1 = calcu_time()
#            print str(gap1)
            f.write(str(gap1) + '\n')
    f.close()
    




