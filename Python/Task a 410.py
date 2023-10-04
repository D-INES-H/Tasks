def is_valid_parenthesis(expression):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return "Invalid"
        else:
            return "Invalid"

    return "Valid" if not stack else "Invalid"

# Test Case 1
test_case_1 = "(( ))"
print(f"Test Case 1: Input: \"{test_case_1}\" Output: {is_valid_parenthesis(test_case_1)}")

# Test Case 2
test_case_2 = "()(("
print(f"Test Case 2: Input: \"{test_case_2}\" Output: {is_valid_parenthesis(test_case_2)}")
