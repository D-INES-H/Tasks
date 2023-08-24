def is_anagram(n, m):
    # Remove spaces and convert to lowercase for accurate comparison
    n = n.replace(" ", "").lower()
    m = m.replace(" ", "").lower()
    
    # Check if the sorted characters of both strings are the same
    return sorted(n) == sorted(m)

# Taking input from the user
n = input("Enter the first string: ")
m = input("Enter the second string: ")

if is_anagram(n, m):
    print(f"{m} is an anagram of {n}.")
else:
    print(f"{m} is not an anagram of {n}.")