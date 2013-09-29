# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# More efficient implementation
largest = 0
n = 600851475143
i = 2
while True:
    if n % i == 0:
        largest = i
        if n == i:
            # finished
            break
        n = n / i
    else:
        i += 1

print("The largest prime factor is", largest)

# original implementation
# def isPrime(n):
#     for i in range(2,n-1):
#         if n % i == 0:
#             return False
#     return True

# largest = 0
# n = 52
# for i in range(2,n-1):
#     print("Checking if", i, "divides", n)
#     if isPrime(i) and n % i == 0:
#         largest = i
#         if i == n:
#             break
#         n = n / i


# print("The largest prime factor is", largest)
