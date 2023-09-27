

import math

class Circle:
    pass

def create(radius):
    c = Circle()
    c.radius = radius
    return c


def is_valid(c):
    return isinstance(c, Circle ) and c.radius > 0

def perimeter(c):
    return (2*math.pi*c.radius) if is_valid(c) else float('nan')
    
def area(c):
    return (math.pi*(c.radius**2)) if is_valid(c) else float('nan')

def get_info(c):
    return f'Circle Radius = <{c.radius}>' if is_valid(c) else '< Invalid Circle >'

def draw(c):
    print(get_info(c))

def test_circle(r):
    c = create(r)
    draw(c)
    print(f'Area = < {area(c)} >')
    print(f'Perimeter = < {perimeter(c)} >')

test_circle(5)





    


    
