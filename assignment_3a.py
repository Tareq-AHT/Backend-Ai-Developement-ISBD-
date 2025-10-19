# hw3 , write a python function that will clean an input text as below
# remove any special charecter,        
# replace any word related to  "bad" with "negative"
# replace any word related to "good" with "positive",
# print the modified text


# from autocorrect import Speller               # Failed to repair the words
# spell = Speller(lang='en')
# text = clean_text
# corrected_words = spell(clean_text)
# print(corrected_words)


# from textblob import TextBlob               # Failed to repair the words
# #text = "i dislik the mvie"
# word_repair = clean_text
# final_correction = TextBlob(word_repair).correct()
# print(final_correction)

import language_tool_python

input_text = input("Insert your thoughts here: ")
special_characters = "!@#$%^&*()_+-=[]};:'\"{,.<>/?\\|`~"           # definning the special charecters

# symbol_map = {
#     '@': 'a',
#     '$': 's',
#     '0': 'o',
#     '1': 'i'
# }

# for symbol, replacement in symbol_map.items():
#     input_text = input_text.replace(symbol, replacement)
    
# print("The imputed text was: ", input_text)


# clean_text = input_text
# for i in special_characters:
#     clean_text = clean_text.replace(i, "")

# print(f"The clean version of the text is- {clean_text}") 

# tool = language_tool_python.LanguageTool('en-US')
# text = clean_text
# find_matches = tool.check(text)
# corrected_text = language_tool_python.utils.correct(text, find_matches)


# print(f"After repairing the damaged words now the text is- {corrected_text}")


#     I @m T@req. I l@ve f@@d$. Food i$ good.
#     The mov!e was good, but the @cting was b@d...!

from autocorrect import Speller
import re

text = input_text

spell = Speller(lang='en')                                      # Create spell checker




cleaned_text = re.sub(r'["!@#$%^&*()_+-=};:]?', '', text)                 # Remove special characters (keep letters & spaces)


corrected_text = spell(cleaned_text)                            # Correct spelling


final_text = corrected_text.replace("good", "positive").replace("bad", "negative")           # Replace specific words


print(final_text)

