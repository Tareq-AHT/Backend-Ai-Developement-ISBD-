# hw-3

# You have an image. Suppose it as a 2D list.
# Modify the list such that … (incomplete in image)

image = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]    
]

# flip

for row in image:
    row.reverse()

print(image)