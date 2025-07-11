#Remove all duplicates from a list.
list1 = [1, 2, 2, 3, 4, 4] 
d = []
for i in list1:
    if i not in d :
        d.append(i)
print(d)


#Rotate a list by 2 positions to the right.
def rotate_right(lst, k):
    n = len(lst)
    k = k % n  # In case k > n
    # let k = 7 and n = 5 , 7 % 5 = 2

    for _ in range(k):
        #We use _ because we don’t care about the loop index.
        last = lst.pop()     # Remove last element 
        lst.insert(0, last)  # Insert it at the beginning
    return lst

# Example usage
nums = [1, 2, 3, 4, 5]
rotated = rotate_right(nums, 2)
print("Rotated list:", rotated)


#Write a Flatten a nested list.
def Flatten_list(nested_list):
    flat_list=[]
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list
    

nested = [[1, 2], [3, 4], [5]]
Flat = Flatten_list(nested)
print("Flatten_list:", Flat)


#Find common elements in two lists.
def common_elements(list1,list2):
    result = []
    for item in list1:
        if item in list2 and list2 not in result:
            result.append(item)
    return result
 
list1= [1,2,3]
list2= [2,3,4]
two_commonelements = common_elements(list1,list2)
print(two_commonelements)
