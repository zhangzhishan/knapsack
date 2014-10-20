#!/usr/bin/env python
# coding=utf-8

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

print greedydp(5, 20, [3, 4, 5, 7, 12], [3, 6, 8, 12, 11])

