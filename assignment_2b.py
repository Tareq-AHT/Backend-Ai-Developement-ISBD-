
# write a paython script,
# find the area of a circle
# radius

print("Let's calculate the Area of a circle of your choice")

r = float(input("Insert a value of Radius: "))  # radius is a variable selected by the users
radius = r*r
pi = 3.1416         # pi is a math constant

area = pi*radius    # formula A = pi * (r**2)

print(f"The area of your given radius is {area:.2f}")