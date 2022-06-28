#lambda function to return even numbers from the list

l = [1,34,6,34,78,67,89,56,5,67,95,34,22]

res = list(filter(lambda x: x%2 == 0,l))
print(res)