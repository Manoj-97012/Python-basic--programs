# method overloading

class A:
    def sum(self,a,b):
        return a+b
class B:
    def sum(self,a,b,c=1):
        return a+b+c
obj=A
print(obj.sum(1,2,5))

# method over-riding

class A:
    def fun1(self):
        print("A is class")
class B(A):
    def fun2(self):
        print("B is class")
        super().fun1()

obj=B()
obj.fun2()