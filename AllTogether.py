### Part Four -- your code goes here. 

import random
list = random.sample(range(1, 100), 10)
result = []

for i in list:
    while i % 2 != 0:
        result.append(i)
        break

print(result)