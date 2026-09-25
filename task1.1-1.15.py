### Task 1.1: Create a list of 5 elements. Then, print its first element.
print("Task 1.1: Create a list of 5 elements. Then, print its first element.")
tl1 = ["a", "b", "c", "d", "e"]
print(tl1[0])

### Task 1.2: Display the last element of your list.

print("Task 1.2: Display the last element of your list.")
print(tl1[-1])

### Task 1.3: Add the integer 42 at the end of your list. Then, add the string forty-two at the end of your list.

print("Task 1.3: No Print Statement - appending (42) and (forty-two)")
tl1.append(42)
tl1.append("forty-two")

### Task 1.4: Display your entire list. Then, display each element of your list one by one.
print("Task 1.4: Display your entire list. Then, display each element of your list one by one.")
print(tl1)

for item in tl1:
    print(item)

### Task 1.5: Delete the last element of your list. Then, display your list to check if you did it properly.
print("Task 1.5: Delete the last element of your list. Then, display your list to check if you did it properly.")
tl1.pop(-1)
print(tl1)

### Task 1.6: Add an element at the beginning of the list and display all its elements.
print("Task 1.6: Add an element at the beginning of the list and display all its elements.")
tl1.insert(0,"insert")
print(tl1)

### Task 1.7: Display the sub-list from the second to the fourth element (included).
# Can you do it in one line?
print("Task 1.7: Display the sub-list from the second to the fourth element (included).")
print(tl1[1:4]) 

### Task 1.8A: Create and Display a new reversed list of your previous list, starting from the end.
print("Task 1.8: Create and Display a new reversed list of your previous list, starting from the end.")
tl1.reverse()
print(tl1)

### Task1.8B: Not using reverse
# First re-reversing to get into original order
tl1.reverse()
# Applying new reversion
tel1 = tl1[::-1]
print(tel1)


### Task 1.9: Add the ten integers from 11 to 20 at the end of your list.
print("Task 1.9: Add the ten integers from 11 to 20 at the end of your list.")
tl1.extend(range(11,21))
print(tl1)

### Task 1.10:  What does the commented code do?
print("Task 1.10: What does the commented code do?")
my_first_list = [4, 5, 6]
my_second_list = [1, 2, 3]
my_first_list.extend(my_second_list)
print(my_first_list)

print("Every element in the second list is appended to the first list.")
## Answer: every element in the second list will be appended to the first list (i.e. my_first_list = [4, 5, 6, 1, 2, 3])

my_first_list = [7, 8, 9]
my_second_list = [4, 5, 6]
my_first_list = [*my_first_list, *my_second_list]
print(my_first_list)
print("my_first_list contains all elements in my_first_list and my_second_list: the *operator unpacks the lists individually so that we dont' get [[my_first_list],[my_second_list]]")
## Answer: the * operator 'unpacks' the list into it's individual elements - which are then joined together and assigned back to my_first_list (i.e my_first_list = [7, 8, 9, 4, 5, 6])

### Task 1.11: Create a list of 5 numbers. Then, print the result of the multiplication of all of its elements.
print("Task 1.11: Create a list of 5 numbers. Then, print the result of the multiplication of all of its elements.")
my_list = [1, 2, 3, 4, 5]
print(f"My list: {my_list}")
result = 1
for element in my_list:
    result *= element
print(result)

### Task 1.12: Test this code and try to explain it: [x + 10 for x in [3, 2, 6, 7, 1, 4]]
print("Task 1.12: Test this code and try to explain it: [x + 10 for x in [3, 2, 6, 7, 1, 4]]")
print([x + 10 for x in [3, 2, 6, 7, 1, 4]])
print("This code adds 10 to every element in the list.")

### Task 1.13: Create a list of 5 numbers. Then, display the smallest element. Finally, display the biggest element.
print("Task 1.13A: Create a list of 5 numbers. Then, display the smallest element. Finally, display the biggest element. (looping through)")
my_list = [24, 58, 39, 25, 8]

min_value = my_list[0]
max_value = my_list[0]

for ele in my_list:
    if ele < min_value:
        min_value = ele
    if ele > max_value:
        max_value = ele

print(f"Min: {min_value}")
print(f"Max: {max_value}")

# Or just use: 
print("Task 1.13B: min(my_list), max(my_list)")
print(f"Min: {min(my_list)}")
print(f"Max: {max(my_list)}")

### Task 1.14 Sort your list in descending order
print("Task 1.14")
print(f"Orignal List: {my_list}")
my_list.sort(reverse=True)
print(f"Sorted List: {my_list}")

### Task 1.15 
print("Task 1.15: My Guess [21, 6, 2, 9, 6, 5]")
print([x // 2 if x %2 == 0 else x*2 for x in [42, 3, 4, 18, 3, 10]])
## my Guess: goes through the list [42, 3, 4, 18, 3, 10] - every even number is divided by two (floor division) and every odd number is multiplied by two
## Correct



