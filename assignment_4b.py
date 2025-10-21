# capitalize all the first character of each sentence

#new_text = text.upper()            # did not work
#new_text = text.capitalize()       # did not work
#new_text = text.casefold()         # did not work
#new_text = text.title()            # did not work
#new_text = text.strip()            # did not work
#new_text = text.split('.')         # did not work
#print(new_text)

text = ''' i am syz. i am learning python innovativeskills. i am feeling positive about it.
i do not feel negative about my past. '''

new_text1 = [s.strip().capitalize() for s in text.split('.')]
print(new_text1)

new_text_join = '. '.join(new_text1)

#new_text1 = new_text[2].capitalize()
print(new_text_join)
