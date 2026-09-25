
scrabble_value = {
    1: ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"],
}

scrabble_value_dict_2 = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10,
}

user_input = input("Enter a Word: ")

word_value_dict1 = 0
for letter in user_input:
    for key in scrabble_value:
        if letter.upper() in scrabble_value[key]:
            word_value_dict1 += int(key)
        else:
            continue

print(f"Word Value: {word_value_dict1}")

word_value_dict_2 = 0
for letter in user_input.upper():
    word_value_dict_2 += scrabble_value_dict_2[letter]
print(f"Word Value: {word_value_dict_2}")


