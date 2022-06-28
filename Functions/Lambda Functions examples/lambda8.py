#lambda function to check if the element is present in the list or not

l = [1,2,3,4,5,6]
v = 9

x = lambda l,v : True if v in l else False

if(x(l,v)):
    print("Element is present in the list")
else:
    print("Element is not present in the list")