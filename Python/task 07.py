def reverse_array(arr):
    return arr[::-1]

arr = input("Enter an array (space-separated values): ").split()
reversed_arr = reverse_array(arr)
print("Reversed array:", reversed_arr)