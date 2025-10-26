# problem 4: You are given a list of tuples, where each tuple contains two items:
# a name (string) and a score (integer). 
# Write a program that sorts the list of tuples based on the score in increasing order.

students = [('John', 85), ('Jane', 92), ('David', 78), ('Emily', 92)]

def score(x):
    return x[1]

sorted_students = sorted(students, key= score)

print("Sorted list:", sorted_students)