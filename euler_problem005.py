# 2520 is the smallest number that can be divided by each of the numbers from 1 to 
# 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?

num = 1
multiples_list = []

for divisor in range(1,21):
	multiples_list.append(divisor)

index = len(multiples_list) - 2

while index > 0:
	multiple = 20 * num

	if multiple % multiples_list[index] == 0:
		index -= 1
	else:
		num += 1
		index = len(multiples_list) - 2

if index == 0:
	print(multiple)