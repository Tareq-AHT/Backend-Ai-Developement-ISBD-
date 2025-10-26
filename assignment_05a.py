# # problem 1: write a program that takes a list of integers and finds all the numbers that appear more than once
# print the repeated numbers and their frequencies

numbers = [1, 2, 3, 2, 4, 5, 6, 5, 5, 7, 8]

count_dict = {}  

for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

print("Repeated numbers and their counts are:")
for key, value in count_dict.items():
    if value > 1:
        print(f"{key}: {value}")
