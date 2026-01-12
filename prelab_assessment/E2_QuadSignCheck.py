#determines quadratic roots given a, b, c
#determines the sign of the roots, and if they are the same (both + or both -)
#error code if both roots are not real numbers

import math

print("This program determines if the roots of a quadratic equation are real and of same or different signs")
numbers = input("Enter a, b, c: ").replace(",", "").split()
a, b, c = map(float, numbers)

discriminant = b**2 - 4*a*c

def calculate_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)

    print("root 1: ",root1, ", root 2: ",root2)
    return root1, root2

def is_positive(number):  #true if number is + or 0
    return bool(number >= 0)

def same_sign(root1, root2):
    sign1 = is_positive(root1)
    sign2 = is_positive(root2)
    if sign1 == sign2:
        return print("Both roots have the same sign")
    else:
        return print("Roots have different signs")

try:
    if discriminant == 0:
        print("Both roots are the same (double root). Please re-run with different a, b, c")
    else:
        root1, root2 = calculate_roots(a, b, c)
        same_sign(root1, root2)

except:
    if discriminant < 0:
        print("Error: Roots are not real numbers. Please re-run with different a, b, c")