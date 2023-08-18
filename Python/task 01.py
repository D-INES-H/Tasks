def add(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x

def subtract(x, y):
    while y != 0:
        borrow = (~x) & y
        x = x ^ y
        y = borrow << 1
    return x

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum_result = add(num1, num2)
print("Sum:", sum_result)

difference_result = subtract(num1, num2)
print("Difference:", difference_result)