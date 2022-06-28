#lambda function to find anagrams from the given list

from collections import Counter
l = ['heya','john','secure','smith','rescue']
str = "eeucrs"

res = list(filter(lambda x: (Counter(str) == Counter(x)),l))
print(res)