# Problem 6: Write a program that iterate through the numbers from a given list.
# Print "even" for even numbers and "odd" for odd numbers.


numbers = [4, 2, 7, 8, 1]

for i in numbers:
    if i % 2 == 0:
        print(i, ": even")
    else:
        print(i, ": odd")

