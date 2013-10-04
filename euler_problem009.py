# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# since a+b+c = 1000, c = 1000-a-b
for a in range(2, 1000):
	for b in range(1, a):
		if a**2 + b**2 == (1000 - a - b)**2:
			print a*b*c

print main()