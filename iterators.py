from random import randint

count = 0 
l = [6,8,2,4,8,3,5,2]

#Example 1 
for num in l: 
    count += num 
print(count)

#Example2
for num in range(10):
    count += num 
print(count)

#Example 3
l1 = [randint(1,10) for num in range(13)]
i = 0
num_search = 2

while i < len(l1):
    if l1[i] == num_search:
        print (f"{num_search} found at index {i}")
    i+=1



 