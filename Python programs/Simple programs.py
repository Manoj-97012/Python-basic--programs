# num = int(input("Enter a number : "))
# fact = 1
# while num >= 1:
#     fact = fact * num
#     num = num - 1
# print(fact)

num = int(input("Enter a number : "))
for i in range(2,num):
    if num % i == 0:
        print("Not a prime number")
        break
else:
    print("prime number")

