# Problem 5: Write a function that merges two dictionaries. Keys can be different.
# If a key exists in both dictionaries, sum their values.

# Problem-5: Merge two dictionaries

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

merged = {}

# step 1: copy d1 to merged
for key in d1:
    merged[key] = d1[key]

# step 2: add d2 keys
for key in d2:
    if key in merged:
        merged[key] += d2[key]  # same key => add values
    else:
        merged[key] = d2[key]

print("Merged dictionary:", merged)
