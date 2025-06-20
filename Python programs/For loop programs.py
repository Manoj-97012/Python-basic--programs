for i in range(0,21,2): # The 2 inside the range() function is called the "step" or "stride." It determines the increment between each consecutive value in the range. In this case, the loop will iterate over the numbers from 1 to 20, with a step of 2
    print(i)
# for i in range(10,0,-1): #
#     print(i)

curr_pop=10000
for i in range(10,1,-1):
    print(i,curr_pop)
    curr_pop /=1.1