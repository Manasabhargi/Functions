#lambda function to check for palindromes

l = ['sanas','heya','john','keaaek']

res = list(filter(lambda x:(x == "".join(reversed(x))),l))
print(res)