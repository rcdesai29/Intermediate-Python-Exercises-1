def count_letters(input_string):
    letter_count = {}
    for char in input_string:
        if char.isalpha():
            char = char.lower()
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count

user_input = input("Enter a string: ")
result = count_letters(user_input)
print(result)
