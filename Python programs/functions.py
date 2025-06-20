def is_function(fname):
    print(fname, "My name is Manoj")

is_function("John")
is_function("Kumar")

def greet(a,b):
    print("this function", a+b)

greet(1,2)

# arbitrary function
def greet(**a):
    print("this function", a)

greet(a=1,b=2)

#Nested function
def outer():
    print("Hello")
    def inner():
        print("World")
    inner()
outer()

def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)

def find_min_of_three(a, b, c):
    if a > b or a > c:
        print("a is greater than")
    elif b > a or b > c:
        print("b is greater than")
    else:
        print("c is greater than")
find_min_of_three(11,23,45)


def find_max_of_three(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

# Example usage:
max_value = find_max_of_three(11, 23, 45)
print("Minimum value is:", max_value)

def list(a,b,c,d,e):
    print(a+b+c+d+e)
    print(a*b*c*e*d)
list(8, 2, 3, 0, 7)
list(8, 2, 3, -1, 7)

def reverse(s):
    return s[::-1]
s="1234abcd"

input_str=reverse(s)
print("Enter reverse string:",input_str)

def fun1(a,b):
    return a + b
    return a - b
print(fun1(10,9))

def greet_user():
     print("Hello!")

greet_user()









