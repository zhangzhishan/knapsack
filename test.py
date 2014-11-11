
import json
import random
import time
import sys
def test(num, cap):
    num = int(num)
    cap = int(cap)
    f = open('cap.txt', 'w+')
    json.dump(cap, f)
    f.close()
    f = open('weight.txt', 'w+')
    weight = []
    random.seed(time.time())
    for i in range(num):
        weight.append(random.triangular(0, 1))
    json.dump(weight, f)
    f.close()
    f = open('value.txt', 'w+')
    value = []
    random.seed(time.time())
    for i in range(num):
        value.append(random.triangular(0, 1))
    json.dump(value, f)
    f.close()

if __name__ == '__main__':
    test(sys.argv[1], sys.argv[2])
