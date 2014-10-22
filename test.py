import json
import random
import time
num = 100
f = open('weight.txt', 'w+')
weight = []
random.seed(time.time())
for i in range(num):
	weight.append(int(random.triangular(1, 5 * num)))
json.dump(weight, f)
f.close()
f = open('value.txt', 'w+')
value = []
random.seed(time.time())
for i in range(num):
	value.append(int(random.triangular(1, 5 * num)))
json.dump(value, f)
f.close()

