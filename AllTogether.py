### Part Four -- your code goes here. 

import random
list = random.sample(range(1, 100), 10)
result = []

for n in list:
    k = 1
    while n % 2 != 0:
        result.append(n)
        break
print(result)