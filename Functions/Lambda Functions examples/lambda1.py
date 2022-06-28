#to change all animal names to uppercase using map and lambda function

animals = ['dog','cat','monkey','peacock']

uppercase = list(map(lambda animal: str.upper(animal), animals))
print(uppercase)