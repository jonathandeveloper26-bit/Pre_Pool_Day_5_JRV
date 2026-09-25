### Challenge: Create a list of 1000000 random integers. Then, sort this list as fast as possible.
import random
import time

rand_list_dot_sort = [random.randint(1,10000000) for i in range(0,10000)]
rand_list_bubble = rand_list_dot_sort
rand_list_merge = rand_list_dot_sort

### Using .sort()

start_time = time.time()
rand_list_dot_sort.sort()
end_time = time.time()
print(f".sort() Time Elapsed: {end_time-start_time}")

### Bubble Sort Implementation: (Don't run with > 100 elements.)
start_time = time.time()
for iteration in range(len(rand_list_bubble)-1,0,-1):
    for index in range(iteration):
        if rand_list_bubble[index] > rand_list_bubble[index+1]:
            temp = rand_list_bubble[index+1]
            rand_list_bubble[index+1] = rand_list_bubble[index]
            rand_list_bubble[index] = temp
end_time = time.time()
print(f"Bubble Sort Time Elapsed: {end_time-start_time}")

### Merge Sort Implementation:
def merge_sort(unsorted_list):

    # Base Case
    if len(unsorted_list) <= 1:
        return unsorted_list

    # Split the unsorted list in two
    first_half = unsorted_list[:len(unsorted_list)//2]
    second_half = unsorted_list[len(unsorted_list)//2:]

    # Recursively call function to get down to 1 or 0 unsorted elements in each list
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)

    #Merge the lists as a list
    intermediate_result = list(merge(first_half, second_half))
    # print(intermediate_result)
    return intermediate_result

def merge(first_half, second_half):
    # Final Sorted List
    result = []

    # Taking both halves, while both have items, it appends the lesser to the result and removes it from the half that contained it.
    while len(first_half) != 0 and len(second_half) != 0:
        if first_half[0] < second_half[0]:
            result.append(first_half[0])
            first_half.remove(first_half[0])
        else:
            result.append(second_half[0])
            second_half.remove(second_half[0])

    # If either of the halves is empty, the result just gets the other half, nothing left to merge
    if len(first_half) == 0:
        result = result + second_half
    else:
        result = result + first_half

    return result

start_time = time.time()
merge_sort(rand_list_merge)
end_time = time.time()

print(f"Time Elapsed: {end_time-start_time}")