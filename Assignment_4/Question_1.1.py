"""
1.1 Write a Python Program(with class concepts) to find the area of the triangle 
using the below formula.area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined 
in the parent class and function to calculate the area should be defined in subclass.

"""
# Parent Class
class Length_of_Sides_of_Traingle:
    
    def __init__(self):
        self.a = int(input("Enter the length of side a: "))
        self.b = int(input("Enter the length of side b: "))
        self.c = int(input("Enter the length of side c: "))

        
# Child class inheriting the properties of Parent class
class Area_of_Triangle(Length_of_Sides_of_Traingle):
    
    def area(self):
        s = (self.a + self.b + self.c) /2
        area =  (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        return area
    

a1=Area_of_Triangle() # Creating an object for child class
print("The area of traingle is", a1.area())
        
    