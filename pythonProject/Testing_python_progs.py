# This function checks whether three sides of given lengths can build a triangle.
def is_a_triangle(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return None
    elif a + b > c and b + c > a and \
            c + a > b:
        return True
    else:
        print(" It can't be a triangle")
        return False


# This function checks if the triangle is a right angled triangle
def is_a_right_angle_triangle(a, b, c):
    if is_a_triangle(a, b, c):
        if a > b and a > c:
            return a ** 2 == b ** 2 + c ** 2
        elif b > a and b > c:
            return b ** 2 == c ** 2 + a ** 2
        else:
            return c ** 2 == a ** 2 + b ** 2
    else:
        #print("It can't be a right angle triangle")
        return False


my_triangle_list = [(1, 3, 4), (3, 4, 5), (3, 12, 14.5)]
for a, b, c in my_triangle_list:
    if is_a_right_angle_triangle(a,b,c):
        print("This is a right angle triangle.")
    else:
        print("This is not a right angle triangle.")




