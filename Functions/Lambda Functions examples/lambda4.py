#lambda function to find the numbers from the list which are divisible by 13

l = [13,45,67,36,38,26,27,95,38]

res = list(filter(lambda x:(x % 13 == 0),l))
print(res)