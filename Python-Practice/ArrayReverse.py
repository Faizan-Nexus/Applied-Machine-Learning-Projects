# #All methods of array reversing
from collections import defaultdict
from sympy import true


# arr = [nums for nums in range(0,11)]
# print("Array: ",arr)

# copy_arr = arr.copy()

# #Using builtin method
# copy_arr.reverse()
# print("Array Reversed (Using Builit Method): ",copy_arr)

# #Using indexing
# print("Array Reversed (Using Indexing)",arr[::-1])

# #Using Pointers
# left ,right = 0,(len(arr)-1)

# while True:
#     arr[right],arr[left] = arr[left], arr[right]
#     left +=  1
#     right -= 1
#     if right <= left:
#         break

# print("Array Reversed (Using Logic)",arr)


#Using Recurssion

nums = [2,4,6,8,10,12]

# def recursive(num,left,right):
#     if left < 0 or right == len(num):
#         print("Incorrect Values for indexing")
#         return
#     if left >= right:
#         return
#     num[right],num[left] = num[left],num[right]
#     recursive(num,left+1,right-1)
#     return num
   
# print("Using Recurssion",recursive(nums,2,6))

#Anagram
#Numbers that follows the following eat, ate, tea (differnt words with same letters)

