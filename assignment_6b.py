# hw-2

# You are given a list of numbers.
# Your output will be a list containing the indices of the odd numbers.

lst = [1, 3, 4,5, 13, 16, 27, 33, 46, 59]

odd_numbers_indx= []

for index, value in enumerate(lst):
    if value%2!= 0:
        odd_numbers_indx.append(index)
    
    
print(odd_numbers_indx)
