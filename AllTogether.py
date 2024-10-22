### Part Four -- your code goes here. 

import random
list = random.sample(range(1, 100), 10)
result = []
result2 = []
print(list)

for i in (list):
        if i % 2 != 0: 
            result.append(i)
    
print(result) 

# EVERYTHING ABOVE WORKS, JUST DOESN'T USE A WHILE LOOP#


for n in list:
    k = 1
    while k < 2:
         if n % 2 != 0:
              result2.append(n)
              k += 1
print(result2)