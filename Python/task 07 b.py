def sum_of_digits(num):
    total_sum = 0
    while num > 0:
        digit = num % 10
        total_sum += digit
        num //= 10
    return total_sum

num = int(input("Enter a number: "))
digit_sum = sum_of_digits(num)
print("Sum of digits:", digit_sum)