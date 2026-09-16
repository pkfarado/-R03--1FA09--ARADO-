import math

print("Type in the coordinates for the first coordinate, put X coordinate first then Y coordinate accordingly")
x1 = float(input("Give a number for x1: "))
y1 = float(input("Give a number for y1: "))

print("Type in the coordinates for the second coordinate, put X coordinate first then Y coordinate accordingly")
x2 = float(input("Give a number for x2: "))
y2 = float(input("Give a number for y2: "))

distance = math.hypot(x2 - x1, y2 - y1)

print(f"The distance of the two points is {distance}")