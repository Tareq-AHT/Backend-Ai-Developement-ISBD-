# Problem-3: write a function that accepts a string count the number of vowels (a, e, i, o, u, and case insensetive). 


def count_vowels(text):
    vowels = ('a', 'e', 'i', 'o', 'u')
    text = text.lower()  
    count = 0

    for i in text:
        if i in vowels:
            count = count + 1

    print("Number of vowels are: ", count)

text = input("Enter the sentence: ")
count_vowels(text)

# Hello World from Python