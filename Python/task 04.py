def next_greater_number(num):
    num_str = str(num)
    digits = list(num_str)

    # Find the first digit from the right that is smaller than the digit to its right
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i == -1:
        return "Not possible"

    # Find the smallest digit to the right of digits[i] that is larger than digits[i]
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1

    # Swap digits[i] and digits[j]
    digits[i], digits[j] = digits[j], digits[i]

    # Reverse the digits to the right of i
    digits[i + 1:] = digits[i + 1:][::-1]

    next_greater = int(''.join(digits))
    return next_greater

num = int(input("Enter a number: "))
result = next_greater_number(num)
print("Next greater number:", result)