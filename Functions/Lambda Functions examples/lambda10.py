#lambda function to return cube of a numbers

l = [1,2,3,4,5]

res = list(map(lambda x: pow(x,3),l))
print(res)