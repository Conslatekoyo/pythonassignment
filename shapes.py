# Class Circle
# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the formula A=πr2
# It has a method to calculate circumference (c) using the formula C=2πr


class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area_of_the_circle(self):
        A=3.142*self.radius*self.radius
        return f"The area is {A}"
    
    def circumference(self):
        C=2*3.142*self.radius
        return f"The circumference is {C}"

# Class Square
# A Square instance accepts the attribute side (a)
# It has method area that returns the area (A) of the square using the formula A=a2
# It has a method to calculate the perimeter (P) of the square using the formula P=4a
class Square:
    def __init__(self,side):
        self.side=side

    def area_of_the_square(self):
        A2=self.side*self.side
        return f"The area of the square is {A2}"
    
    def perimeter_of_a_square(self):
        P=4*self.side
        return f"the perimeter of the square is {P}"



# # Class Rectangle
# # A Rectangle instance accepts two sides of a rectangle (w,l)
# # It has method to calculate the area (A) of the rectangle using the formula A=wl
# # It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)

class Rectangle:
    def __init__(self,w,l):
        self.w=w
        self.l=l
    def area_of_the_rec(self):
        A3=self.w*self.l
        return f"The area of the rectangle is {A3}"
    def perimeter_of_the_rec(self):
        total=self.w+self.l
        P3= 2*total
        return f"The perimeter of the rectangle is {P3}"


# # Class Sphere
# # A Sphere Instance accepts the radius of the sphere (r)
# # It has a method to calculate the surface area (A) using the formula A=4πr2
# # It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)

class Sphere():
    def __init__(self,radiussphere):
        self.radiussphere=radiussphere
    
    def surface_area(self):
        SA= 4*3.142*self.radiussphere**2
        return f"The surface area of the sphere is{SA}"

    def volume(self):
        V=1.333*3.142*self.radiussphere**3
        return f"The volume of the sphere is{V}"




