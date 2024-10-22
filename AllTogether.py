### Part Four -- your code goes here. 

import random
list = random.sample(range(1, 100), 10)

for i in (list):
    while i % 2:
        list.pop(0)
    
print(list)