### Task 1.16 - Write a program that deletes duplicated elements in a list

## Lists to Use
example_list_1 = [1,1,1,1,1,2,2,2,2,2]
example_list_2 = [42, "42", 42.0, 21+21, 42*10/10]

# List to Test
test_list = example_list_2

# Empty List to store values (without duplication)
non_duplicate_list = []

# Increments through the test_list and checks if the element already exists in non_duplicate_list. If yes, continue, if not, add it.
for i in range(len(test_list)):
    if test_list[i] in non_duplicate_list:
        continue
    else:
        non_duplicate_list.append(test_list[i])

print(non_duplicate_list)
