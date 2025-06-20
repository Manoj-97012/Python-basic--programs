


# class Mobile:
#     def __init__(self,Brand,battery,camera,price,ram):
#         self.Brand=Brand
#         self.battery=battery
#         self.camera=camera
#         self.price=price
#         self.ram=ram
#     def display(self):
#         print("Brand:", self.Brand)
#         print("battery:", self.battery)
#         print("camera:",self.camera)
#         print("price:",self.price)
#         print("ram:",self.ram)
#         print("-----------------------")
#
# obj=Mobile("apple","5000mah","50mp",100000,"8GB")
# obj.display()
#
# obj2=Mobile("oneplus","6000mah","100mp",10000,"8GB")
# obj2.display()
#
#
# class Teams:
#     def __init__(self, RCB, CSK, MI, LSG):
#         self.RCB=RCB
#         self.CSK=CSK
#         self.MI=MI
#         self.LSG=LSG
#     def display(self):
#         print("RCB:",self.RCB)
#         print("CSK:",self.CSK)
#         print("MI:",self.MI)
#         print("LSG:",self.LSG)
# obj=Teams("Virat","Dhoni","Rohit","Pant")
# obj.display()
#
#
# class Family:
#     def __init__(self,Father, mother, brother):
#         self.Father=Father
#         self.mother=mother
#         self.brother=brother
#     def fun1(self):
#         print("Father", self.Father)
#         print("mother", self.mother)
#         print("brother", self.brother)
# obj=Family("Bhaskar","Kavitha","Teja")
# obj.fun1()

# class Person():
#     def __init__(self,name,country,dob):
#         self.name=name
#         self.country=country
#         self.dob=dob
#     def display(self):
#         print("name :", self.name)
#         print("country :",self.country)
#         print("dob :", self.dob)
# obj=Person("Manoj","India","18/09/1998")
# obj.display()

#Calculator Class for Basic Arithmetic Operations using the class

class Calculator:
    def add(self,X,Y):
        return X + Y
    def sub(self,X,Y):
        return X - Y
    def mul(self,X,Y):
        return X * Y
obj=Calculator()
result = obj.add(6,7)
print("add :", result)
result = obj.sub(7,5)
print("sub :", result)
result = obj.mul(6,7)
print("mul :", result)

#Simple Student Class Example
class Student():
    def __init__(self,name,rollnumber):
        self.name=name
        self.rollnumber=rollnumber
    def display(self):
        print("Name:", self.name)
        print("rollnumber :",self.rollnumber)
obj=Student("Manoj","12")
obj.display()

# car class Example
class Car():
    def __init__(self,name,year,price):
        self.name=name
        self.year=year
        self.price=price
    def display(self):
        print("Car :", self.name, "year:", self.year, "price :",self.price)

C=Car("Kia", "2018","900000")
C1=Car("Toyata", "2011","800000")
C.display()
C1.display()


# Rectangle Area Calculation Example

class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length * self.breadth

rect1 = Rectangle(5, 10)
rect2 = Rectangle(7, 3)

print("Area of Rectangle 1:", rect1.area())
print("Area of Rectangle 2:", rect2.area())
print("-------------------")

#Movie Class Example
class Movie():
    def __init__(self,director,budget,Heroname):
        self.director=director
        self.budget=budget
        self.Heroname=Heroname
    def display(self):
        print("director name :", self.director)
        print("budget :", self.director)
        print("Heroname :", self.Heroname)
        print("-------------------")
M1 = Movie("Rajamouli","1000CR","Mahesh babu")
M2 = Movie("Harish","300CR","Pawan kalyan")
M1.display()
M2.display()



