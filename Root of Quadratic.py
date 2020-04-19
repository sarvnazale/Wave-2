from math import sqrt
a = int(input("Enter the 'a' value: "))
b = int(input("Enter the 'b' value: "))
c = int(input("Enter the 'c' value: "))
discriminant = b ** 2 - (4 * a * c)
if discriminant > 0: 
    root_1 = (-b + sqrt(discriminant) / (2 * a))
    root_2 = (-b - sqrt(discriminant) / (2 * a))
    print("This equation has two distinct real roots: %f and %f " % (root_1, root_2))
elif discriminant == 0:
    root_1 = (-b) / (2 * a)
    print("This equation has one real root:", root_1)
else:
    print("This equation has no real roots.")