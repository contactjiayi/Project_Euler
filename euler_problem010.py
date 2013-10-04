# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def isPrime(num, primes_list):
	for i in primes_list:
		if num % i == 0:
			return False
	return True

def main(max):
	total = 0
	number = 2
	primes = []

	while number < max:
		if number == 2 or isPrime(number, primes):
			primes.append(number)
			total += number
		number += 1
	return total

print main(2*10**6)