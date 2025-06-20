from piglet.compilexml import make_i18n_substitution


# class Car:
#     wheels = 4
#
#     def __init__(self,):
#         self.mil = 10
#         self.car_name = "BMW"
#
#
# c1 = Car()
# c2 = Car()
#
# c1.mil = 9
# print(c1.mil, c2.car_name,c1.wheels )
# print(c2.mil, c2.car_name,c2.wheels )


class Average:
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def number(self):
        print(self.m1, self.m2, self.m3)/3

b1 = Average(23,34,56)
b2 = Average(34,56,78)

