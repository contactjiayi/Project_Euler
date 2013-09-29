# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that 
# the 6th prime is 13.

# What is the 10 001st prime number?

count = 0
index = 0
number = 2
primes = []

while count < 10001:
	while index < len(primes):
		if number % primes[index] == 0:
			number += 1
			index = 0
		else:
			index += 1

	if index == len(primes):
		primes.append(number)
		count += 1
		number += 1
		index = 0

print(number-1)