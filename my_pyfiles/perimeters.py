import math

def calculate_circle_perimeter(radius):
    perimeter = 2 * math.pi * radius
    return perimeter

radius = float(input("Enter the radius of the circle: "))
perimeter = calculate_circle_perimeter(radius)
print("The perimeter of the circle is:", perimeter)
