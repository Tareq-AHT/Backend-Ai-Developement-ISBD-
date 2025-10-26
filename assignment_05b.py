# problem 2: write a program that takes two lists of integers. Then find and print:
                                # 1. the elements common to both.
                                # 2. the elements that are unique to each.

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common_values = []
unique_values_list1 = []
unique_values_list2 = []

for x in list1:
    if x in list2:
        common_values.append(x)


for x in list1:
    if x not in list2:
        unique_values_list1.append(x)


for x in list2:
    if x not in list1:
        unique_values_list2.append(x)

print("Common elements:", set(common_values))
print("Unique of list1:", set(unique_values_list1))
print("Unique of list2:", set(unique_values_list2))
