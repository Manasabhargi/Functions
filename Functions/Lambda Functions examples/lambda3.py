#lambda function to use reduce for computing max element from the list

import functools

l = [40,30,80,50]
print("The maximum element from the list is : ",end="")
print(functools.reduce(lambda a,b: a if a>b else b,l))