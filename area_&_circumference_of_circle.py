import math as m
def area(r):
    return (m.pi* (r**2))
def circumference(r):
    return (2* m.pi* r)
r = eval(input('Enter the randius : '))
Area = area(r)
Circumference = circumference(r)
print('Area of circle : ',Area)
print('Circumference of circle :',Circumference)
