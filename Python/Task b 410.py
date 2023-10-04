def sort_array(arr):
    # Ascending order
    ascending_order = sorted(arr)
    print("Ascending Order:", ' '.join(map(str, ascending_order)))

    # Descending order
    descending_order = sorted(arr, reverse=True)
    print("Descending Order:", ' '.join(map(str, descending_order)))

# Input array
input_array = [5, 8, 6, 2, 9, 7]

# Output
sort_array(input_array)
