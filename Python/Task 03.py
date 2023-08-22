def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def count_coprimes(n):
    count = 0
    for x in range(1, n):
        if gcd(x, n) == 1:
            count += 1
    return count

n = int(input("Enter a number: "))
result = count_coprimes(n)
print("Number of co-primes of", n, "is", result)