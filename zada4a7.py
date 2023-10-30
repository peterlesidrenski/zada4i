import math
shape = input("enter shape (square, rectangle, circle, triangle): ")
if shape == "square":
    side_length = float(input("Enter square lenght: "))
    area = side_length ** 2
elif shape == "rectangle":
    length = float(input("Enter rectangle lenght: "))
    width = float(input("Enter rectangle widht: "))
    area = length * width
elif shape == "circle":
    radius = float(input("enter radius of circle: "))
    area = math.pi * radius ** 2
elif shape == "triangle":
    base = float(input("enter base of triangle: "))
    height = float(input("enter height of trangle: "))
    area = 0.5 * base * height
else:
    print("Wrong figure.")
if area is not None:
    print(f"area of {shape} is: {area:.2f}")
