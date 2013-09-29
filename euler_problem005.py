# 2520 is the smallest number that can be divided by each of the numbers from 1 to 
# 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?

# alternative implementation making use of prime factors
def isPrime(number):
	for i in range(2, number):
		if number % i == 0:
			return False
	return True

primes = []
for i in range(2,21):
	if isPrime(i):
		primes.append(i)

factors = []
count = 1

for i in primes:
	while i ** count < 20:
		factors.append(i)
		count += 1

	if i ** count > 20:
		count = 1

print(factors)

smallest_multiple = 1

for j in factors:
	smallest_multiple *= j

print(smallest_multiple)

# original implementation
# num = 1
# multiples_list = []

# for divisor in range(1,21):
# 	multiples_list.append(divisor)

# index = len(multiples_list) - 2

# while index > 0:
# 	multiple = 20 * num

# 	if multiple % multiples_list[index] == 0:
# 		index -= 1
# 	else:
# 		num += 1
# 		index = len(multiples_list) - 2

# if index == 0:
# 	print(multiple)