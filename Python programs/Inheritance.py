# single inheritance
class Parent:
    def func1(self):
        print("This parent class")
class Child(Parent):
    def func2(self):
        print("This child class")

obj=Child()
obj.func2()
obj.func1()

# mutiple inheritance
class Parent:
    def func1(self):
        print("This parent class")
class Child(Parent):
    def func2(self):
        print("This child class")
class GrandChild(Child):
    def func3(self):
        print("this parent class")
obj= GrandChild()
obj.func3()

# hierarchical inheritance
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def bow(self):
        print("dog is bow")
class Cat(Animal):
    def meow(self):
        print("cat is shouting")

dog = Dog()
cat = Cat()

dog.bow()
cat.meow()

# Multiple inheritance
class Father:
    def func1(self):
        print("This father class")
class Mother:
    def fun2(self):
        print("This Mother class")
class Children(Father,Mother):
    def fun3(self):
        print("this Child class")
obj=Children()
obj.func1()
obj.fun2()
obj.fun3()

