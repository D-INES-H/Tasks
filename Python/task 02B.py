def digit_to_word(digit):
    word_dict = {
        '0': 'Zero',
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine'
    }
    
    return word_dict.get(digit, 'Invalid Digit')

digit = input("Enter a digit (0-9): ")


word = digit_to_word(digit)
print(f"The word representation of {digit} is {word}.")
