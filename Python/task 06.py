def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def reverse_digits(num):
    return int(str(num)[::-1])

def check_prime_with_twist(n, m):
    if is_prime(m) or is_prime(reverse_digits(m)):
        return True
    return False

n = int(input("Enter first number: "))
m = int(input("Enter second number: "))

if check_prime_with_twist(n, m):
    print(f"{m} is a prime number or becomes prime when digits are reversed.")
else:
    print(f"{m} is not a prime number and does not become prime when digits are reversed.")