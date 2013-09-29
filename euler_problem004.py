# A palindromic number reads the same both ways. The largest palindrome made from 
# the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(number):
	number = list(str(number))
	position = 0
	while position + 1 <= len(number) / 2:
		if number[position] != number[len(number) - 1 - position]:
			return False
		position += 1
	return True

num1 = 999
num2 = 999
max = 0

while num2 > 99 and num1 > 99:
	product = num1 * num2
	
	if product > max:
		if isPalindrome(product):
			max = product

	num2 -= 1

	if num2 == 99:
		num1 -= 1
		num2 = num1

print(max)