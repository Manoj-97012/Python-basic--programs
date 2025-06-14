# write a Grid pattern program
n = 4
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()

# Write a Right angled triangle 
n = 4
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

# Write a Right angled triangle inverted
n = 4 
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()

# write a Equilateral triangle (normal and inverted)
n = 4
for i in range(n):
    for j in range(n-1-i):
        print(' ', end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()
n=3
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for k in range(2*(n-i)-1):
        print("*", end=" ")
    print()

# write a Rhombus pattern
n = 5
for i in range(n):
    for j in range(2*(n-i)-1):
        print(" ", end=" ")
    for k in range(n):
        print("*", end=" ")
    print()


# Write Alphabetical patterns
n = 4
for i in range(n):
    for j in range(n):
        print(chr(65), end=" ")
    print()

n = 4
for i in range(n):
    for j in range(i+1):
        print(chr(65+i), end=" ")
    print()

n = 4
for i in range(n):
    for j in range(n-i):
        print(chr(65-i), end=" ")
    print()