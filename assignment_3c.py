# Assignment_3c. make a function that will take a text and retrun list of 
# word from the text. the text may contain punctuation,  special characters and newlines

input_text = input("Write your text here: ")
#print(input_text)
special_characters = "!@#$%^&*()_+-=[]};:'\"{,.<>/?\\|`~" 

def return_text(input_text):
    input_text = input_text.replace('\\n', '\n')
    clean_text = input_text.replace('\\n', ' ')
    
    for ch in special_characters:
        clean_text = clean_text.replace(ch, '')
    
    word_list = clean_text.split()
    
    return word_list

words = return_text(input_text)
print(words)

# Hello, world! This\\nis @AI & ML.
